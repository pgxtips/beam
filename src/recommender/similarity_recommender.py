from .abc_recommender import Recommender

class LogisticRecommender(Recommender):
    def train(self, user_id, interactions):
        pass

    def recommend(self, user_id, k=10):
        pass

    def add_user_preferences(self, user_id, preferred_tags):
        pass
