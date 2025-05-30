import uuid
from typing import Optional
from src.models.session_data import SessionData

class SessionHandler:
    def __init__(self):
        # session_id : session
        self.__sessions: dict[str, SessionData] = {}

    def create_new(self) -> str:
        """
        @returns uuid of new session created
        """
        # create a uuid
        id = str(uuid.uuid4())

        # create a new instance of session
        self.__sessions[id] = SessionData()

        import src.globals as globals
        globals.APP_DATA.save_app_data()

        return str(id)


    def get_sessions(self):
        return self.__sessions

    def get_session_data(self, session_id: str) -> Optional[SessionData]:
        return self.__sessions.get(session_id)

    def get_count(self):
        return len(self.__sessions)
     
    def get_preferences(self, session_id: str):
        session_data = self.__sessions[session_id] 
        return session_data.get_preferences()

    def get_preprocessed_likes(self, session_id: str):
        session_data = self.__sessions[session_id] 
        return session_data.get_preprocessed_likes()

    def get_preprocessed_dislikes(self, session_id: str):
        session_data = self.__sessions[session_id] 
        return session_data.get_preprocessed_dislikes()

    def set_preferences(self, session_id: str, prefs: list[str]):
        session_data = self.__sessions[session_id] 
        session_data.add_prefs(prefs)

    def process_likes(self, session_id: str):
        session_data = self.__sessions[session_id] 
        session_data.process_likes()

    def process_dislikes(self, session_id: str):
        session_data = self.__sessions[session_id] 
        session_data.process_dislikes()

    def like_content(self, session_id: str, cid:str):
        session_data = self.__sessions[session_id] 
        session_data.add_like(cid)

    def dislike_content(self, session_id:str, cid:str):
        session_data = self.__sessions[session_id] 
        session_data.add_dislike(cid)
