import uuid
from typing import Optional

from src.models.session_data import SessionData

class AppData:
    def __init__(self):
        # session_id : session_data
        self.session_data = {}

    def create_new_session(self) -> str:
        """
        @returns uuid of new session created
        """
        # create a uuid
        id = str(uuid.uuid4())

        # create a new instance of session_data
        self.session_data[id] = SessionData()
        return str(id)

    def set_session_preferences(self, session_id, prefs):
        if not (self.session_data.get(session_id)): 
            print("Error: could not find session data")
            return

        self.session_data[session_id].preferences = prefs

    def get_session_data(self, session_id) -> Optional[SessionData]:
        return self.session_data.get(session_id)
