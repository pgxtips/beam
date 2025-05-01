class Metrics:
    def __init__(self):
        self.content_completion_percentages: dict[str, float] = {}
        self.content_started: set[str] = set()
        self.content_completed: set[str] = set()
        self.content_revisited: set[str] = set()

    def record_start(self, cid: str):
        self.content_started.add(cid)

    def record_completion(self, cid: str):
        self.content_completed.add(cid)
        self.content_completion_percentages[cid] = 1.0

    def record_watch_percentage(self, cid: str, percent: float):
        self.content_completion_percentages[cid] = max(self.content_completion_percentages.get(cid, 0), percent)

    def record_replay(self, cid: str):
        self.content_revisited.add(cid)

    def to_dict(self):
        return {
            "watch_percentages": self.content_completion_percentages,
            "video_started": list(self.content_started),
            "video_completed": list(self.content_completed),
            "replayed_videos": list(self.content_revisited),
        }
