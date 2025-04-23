class SessionData:
    def __init__(self):
        # list of content_ids 
        self.__preferences: set[str] = set()
        self.__history = {}
        self.__likes: set[str] = set()
        self.__dislikes: set[str] = set()

        self.__preprocessed_likes: set[str] = set()
        self.__preprocessed_dislikes: set[str] = set()

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
