from datetime import datetime 

class SessionData:
    def __init__(self):
        from src.globals import APP_DATA 
        self.__model: str = APP_DATA.get_default_model()
        # list of content_ids 
        self.__preferences: set[str] = set()
        self.__history = {}
        self.__likes: set[str] = set()
        self.__dislikes: set[str] = set()

        self.__preprocessed_likes: set[str] = set()
        self.__preprocessed_dislikes: set[str] = set()

        self.__last_train: datetime = datetime.now()
        self.__last_seen: datetime = datetime.now()
        self.__created: datetime = datetime.now()

    def get_model(self):
        return self.__model

    def get_last_seen(self):
        return self.__last_seen

    def get_created(self):
        return self.__created

    def get_last_train(self):
        return self.__last_train

    def get_preferences(self):
        return self.__preferences

    def get_preprocessed_likes(self):
        return self.__preprocessed_likes

    def get_preprocessed_dislikes(self):
        return self.__preprocessed_dislikes

    def get_all_likes(self):
        return self.__likes | self.__preprocessed_likes

    def get_all_dislikes(self):
        return self.__dislikes | self.__preprocessed_dislikes

    def process_likes(self):
        for cid in self.__preprocessed_likes:
            self.__likes.add(cid)
        self.__preprocessed_likes.clear()

    def process_dislikes(self):
        for cid in self.__preprocessed_dislikes:
            self.__dislikes.add(cid)
        self.__preprocessed_dislikes.clear()

    def add_prefs(self, prefs: list[str]):
        for pref in prefs:
            self.__preferences.add(pref)

    def add_like(self, cid: str):
        self.__preprocessed_likes.add(cid)

    def add_dislike(self, cid: str):
        self.__preprocessed_dislikes.add(cid)
