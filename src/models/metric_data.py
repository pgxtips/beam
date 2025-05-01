class MetricData:
    def __init__(self):
        self.content_completion_percentages: dict[str, float] = {}
        self.content_revisited: set[str] = set()

    def record_watch_percentage(self, cid: str, percent: float):
        self.content_completion_percentages[cid] = max(self.content_completion_percentages.get(cid, 0), percent)

    def record_replay(self, cid: str):
        self.content_revisited.add(cid)

    def to_dict(self):
        return {
            "watch_percentages": self.content_completion_percentages,
            "replayed_videos": list(self.content_revisited),
        }
