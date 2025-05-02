class MetricData:
    def __init__(self):
        self.content_completion_percentages: dict[str, float] = {}
        self.content_revisited: set[str] = set()

    def to_dict(self):
        return {
            "watch_percentages": self.content_completion_percentages,
            "replayed_videos": list(self.content_revisited),
        }
