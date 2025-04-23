from src.globals import app_data

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

        self.id_to_index = {cid: i for i, cid in enumerate(content_ids)}

    def train(self, session_id):
        """
        interactions: list of (content_id, label) where label is 1 (like) or 0 (dislike)
        """

        assert session_id in self.classifiers

        session_data = app_data.get_session_data(session_id)
        assert session_data

        liked = session_data.likes
        disliked = session_data.dislikes

        X = []
        y = []
        
        for cid in liked:
            if cid not in self.id_to_index:
                continue
            idx = self.id_to_index[cid]
            content_vector = self.content_matrix[idx]
            X.append(content_vector)
            y.append(1.0)

        for cid in disliked:
            if cid not in self.id_to_index:
                continue
            idx = self.id_to_index[cid]
            content_vector = self.content_matrix[idx]
            X.append(content_vector)
            y.append(0.0)

        if X:
            X_stack = np.vstack([x.toarray() for x in X])
            self.classifiers[session_id].partial_fit(
                X_stack, y, classes=[0, 1]
            )

    def recommend(self, session_id, k=10):
        
        session_data = app_data.get_session_data(session_id)

        if not session_data:
            print("Error: No session data found for id:", session_id)
            return 
        
        if session_id in self.classifiers and hasattr(self.classifiers[session_id], "coef_"):
            # Trained model exists
            model = self.classifiers[session_id]
            X = self.content_matrix
            probs = model.predict_proba(X)[:, 1]
            ranked_indices = np.argsort(probs)[::-1]
        else:
            # cold-start: rank by tag similarity with preferred_tags
            if session_id not in self.vector_preferences:
                raise Exception(f"User {session_id} has no calculated preferences or model.")
            user_vec = self.vector_preferences[session_id]
            sim_scores = (self.content_matrix @ user_vec.T).toarray().flatten()
            ranked_indices = np.argsort(sim_scores)[::-1]

        recommended_ids = []

        for idx in ranked_indices:
            cid = self.content_ids[idx]
            if cid not in recommended_ids:
                recommended_ids.append(cid)
            if len(recommended_ids) == k:
                break
        return recommended_ids

    def add_user_preferences(self, session_id):

        session_data = app_data.get_session_data(session_id)
        assert session_data

        vocab = self.vectorizer.vocabulary_
        vector = lil_matrix((1, self.content_matrix.shape[1]), dtype=float)

        for tag in session_data.preferences:
            if tag in vocab:
                vector[0, vocab[tag]] = 1.0

        self.vector_preferences[session_id] = vector.tocsr()
        # uses SGDClassifier as it allows for online learning
        # it allows handles sparse data well
        self.classifiers[session_id] = SGDClassifier(
            loss='log_loss',
            max_iter=1000,
        )
