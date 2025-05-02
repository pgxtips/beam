from src.models import session_handler

from .abc_recommender import Recommender

from sklearn.linear_model import SGDClassifier
from scipy.sparse import lil_matrix
import numpy as np

class LogisticRecommender(Recommender):
    def __init__(self, content_matrix, content_ids, vectorizer):
        """
        content_matrix: sparse matrix (n_items x n_tags)
        content_ids: list of content item ids, aligned with rows in content_matrix
        vectorizer: CountVectorizer used to map tag names to indices
        """
        self.content_matrix = content_matrix
        self.content_ids = content_ids
        self.vectorizer = vectorizer

        self.classifiers = {}  # session_id -> SGDClassifier
        self.vector_preferences = {}  # session_id -> vector preferences 
        self.session_preferences = {}  # session_id -> session preferences 

        self.id_to_index = {cid: i for i, cid in enumerate(content_ids)}

    def train(self, session_id):
        import src.globals as globals

        assert globals.APP_DATA
        SESSION_HANDLER = globals.APP_DATA.get_session_handler()

        liked = SESSION_HANDLER.get_preprocessed_likes(session_id)
        disliked = SESSION_HANDLER.get_preprocessed_dislikes(session_id)

        interactions = (
            [[cid, 1] for cid in liked] +
            [[cid, 0] for cid in disliked]
        )

        X, y = [], []

        for cid, status in interactions:
            if cid not in self.id_to_index:
                continue
            idx = self.id_to_index[cid]
            content_vector = self.content_matrix[idx]
            X.append(content_vector)
            y.append(status)

        if X:
            X_stack = np.vstack([x.toarray() for x in X])
            self.classifiers[session_id].partial_fit(
                X_stack, y, classes=[0, 1]
            )
            SESSION_HANDLER.process_likes(session_id)
            SESSION_HANDLER.process_dislikes(session_id)

    def recommend(self, session_id, k=10):
        import src.globals as globals

        self.__sync_session_model(session_id)

        assert globals.APP_DATA

        SESSION_HANDLER = globals.APP_DATA.get_session_handler()
        assert SESSION_HANDLER

        session_data = SESSION_HANDLER.get_session_data(session_id)

        model = self.classifiers[session_id]
        X = self.content_matrix
        probs = model.predict_proba(X)[:, 1]
        ranked_indices = np.argsort(probs)[::-1]

        rec_ids = []

        history_ids = session_data.get_history()

        for idx in ranked_indices:
            cid = self.content_ids[idx]
            if cid not in history_ids and cid not in rec_ids:
                rec_ids.append(cid)
            if len(rec_ids) == k:
                break

        assert session_data 

        for cid in rec_ids:
            session_data.add_history(cid)

        globals.APP_DATA.save_app_data()

        return rec_ids

    def __create_classifier(self, session_id):

        import src.globals as globals

        assert globals.APP_DATA
        SESSION_HANDLER = globals.APP_DATA.get_session_handler()

        vocab = self.vectorizer.vocabulary_
        vector = lil_matrix((1, self.content_matrix.shape[1]), dtype=float)

        prefs = SESSION_HANDLER.get_preferences(session_id)

        for tag in prefs:
            if tag in vocab:
                vector[0, vocab[tag]] = 1.0

        pref_v = vector.tocsr()
        self.vector_preferences[session_id] = pref_v

        # uses SGDClassifier as it allows for online learning
        # it allows handles sparse data well
        clf = SGDClassifier(loss='log_loss', max_iter=1000)
        self.classifiers[session_id] = clf
        clf.partial_fit(np.zeros((1, self.content_matrix.shape[1])), [0], classes=[0, 1])

    def __sync_session_model(self, session_id: str):
        import src.globals as globals

        assert globals.APP_DATA
        SESSION_HANDLER = globals.APP_DATA.get_session_handler()

        # ensure a classifier has been created for current session
        if (not self.classifiers.get(session_id)):
            self.__create_classifier(session_id)

        # ensure the model has update to date preferences
        old_prefs = self.session_preferences.get(session_id, set())
        new_prefs = SESSION_HANDLER.get_preferences(session_id)

        if (old_prefs != new_prefs):
            vocab = self.vectorizer.vocabulary_
            vector = lil_matrix((1, self.content_matrix.shape[1]), dtype=float)

            prefs = new_prefs
            for tag in prefs:
                if tag in vocab:
                    vector[0, vocab[tag]] = 1.0

            pref_v = vector.tocsr()
            self.vector_preferences[session_id] = pref_v

            clf = self.classifiers[session_id]

            # seed with synthetic samples
            pos = pref_v.toarray()
            neg = np.zeros_like(pos)

            X_seed = np.vstack([pos, neg])          # shape (2, n_tags)
            y_seed = np.array([1, 0])               # like, dislike

            clf.partial_fit(X_seed, y_seed, classes=[0, 1])
            self.session_preferences[session_id] = new_prefs

        # ensure that unprocessed likes and dislikes are processed
        self.train(session_id)
