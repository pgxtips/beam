from .abc_recommender import Recommender

class LogisticRecommender(Recommender):
    def train(self, session_id):
        pass

    def recommend(self, session_id, k=10) -> list:
        pass

    def add_user_preferences(self, session_id):
        pass
