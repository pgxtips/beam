from abc import ABC, abstractmethod

class Recommender(ABC):
    @abstractmethod
    def train(self, session_id):
        pass

    @abstractmethod
    def recommend(self, session_id, k=10) -> list:
        pass
