from abc import ABC, abstractmethod

class Recommender(ABC):
    @abstractmethod
    def train(self, session_id, interactions):
        pass

    @abstractmethod
    def recommend(self, session_id, k=10) -> list:
        pass

    @abstractmethod
    def add_user_preferences(self, session_id, preferred_tags):
        pass
