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
        self.session_classifiers = {}  # session_id -> SGDClassifier
        self.session_preferences = {}  # session_id -> sparse tag vector
        self.session_previous_cids = {}  # session_id -> set(content id)

        self.id_to_index = {cid: i for i, cid in enumerate(content_ids)}

    def train(self, session_id, interactions):
        """
        interactions: list of (content_id, label) where label is 1 (like) or 0 (dislike)
        """

        if session_id not in self.session_classifiers:
            raise Exception(f"Session {session_id} has no initialized model. Call add_user_preferences first.")

        X = []
        y = []

        for content_id, label in interactions:
            if content_id not in self.id_to_index:
                continue
            idx = self.id_to_index[content_id]
            content_vector = self.content_matrix[idx]
            X.append(content_vector)
            y.append(label)

        if X:
            X_stack = np.vstack([x.toarray() for x in X])
            self.session_classifiers[session_id].partial_fit(
                X_stack, y, classes=[0, 1]
            )

    def recommend(self, session_id, k=10):
        if session_id in self.session_classifiers and hasattr(self.session_classifiers[session_id], "coef_"):
            # Trained model exists
            model = self.session_classifiers[session_id]
            X = self.content_matrix
            probs = model.predict_proba(X)[:, 1]
            ranked_indices = np.argsort(probs)[::-1]
        else:
            # cold-start: rank by tag similarity with preferred_tags
            if session_id not in self.session_preferences:
                raise Exception(f"User {session_id} has no preferences or model.")
            user_vec = self.session_preferences[session_id]
            sim_scores = (self.content_matrix @ user_vec.T).toarray().flatten()
            ranked_indices = np.argsort(sim_scores)[::-1]

        recommended_ids = []

        if not self.session_previous_cids.get(session_id):
            self.session_previous_cids[session_id] = set() 
            
        for idx in ranked_indices:
            cid = self.content_ids[idx]
            if cid not in self.session_previous_cids[session_id]:
                recommended_ids.append(cid)
                self.session_previous_cids[session_id].add(cid)
            if len(recommended_ids) == k:
                break
        return recommended_ids

    def add_user_preferences(self, session_id, preferred_tags):
        vocab = self.vectorizer.vocabulary_
        vector = lil_matrix((1, self.content_matrix.shape[1]), dtype=float)

        for tag in preferred_tags:
            if tag in vocab:
                vector[0, vocab[tag]] = 1.0

        self.session_preferences[session_id] = vector.tocsr()
        # uses SGDClassifier as it allows for online learning
        # it allows handles sparse data well
        self.session_classifiers[session_id] = SGDClassifier(
            loss='log_loss',
            max_iter=1000,
        )
