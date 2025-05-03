from .abc_recommender import Recommender
import random

class NoneRecommender(Recommender):
    def __init__(self, content_ids):
        """
        content_ids: list of content item ids, aligned with rows in content_matrix
        """
        self.content_ids = content_ids
        # session_id -> str[]
        self.rec_history = {} 

    def train(self, session_id):
        pass

    def recommend(self, session_id, k=10) -> list:
        import src.globals as globals

        assert globals.APP_DATA
        SESSION_HANDLER = globals.APP_DATA.get_session_handler()
        session_data = SESSION_HANDLER.get_session_data(session_id)

        assert session_data

        # filter out already watched content
        history_ids = session_data.get_history()
        unseen_ids = [cid for cid in self.content_ids if cid not in history_ids]

        # choose up to k items randomly
        recommended = random.sample(unseen_ids, min(k, len(unseen_ids)))

        # update session history
        for cid in recommended:
            session_data.add_history(cid)
            
        if (self.rec_history.get(session_id)):
            self.rec_history[session_id].append(recommended)
        else:
            self.rec_history[session_id] = recommended

        globals.APP_DATA.save_app_data()

        return recommended
