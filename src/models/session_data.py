class SessionData:
    def __init__(self):
        # list of tags
        self.preferences = []

        self.likes = {}
        self.dislikes = [] 

        # watch time > 70%
        self.retained = [] 

        # watch time < 40%
        self.unretained = [] 
