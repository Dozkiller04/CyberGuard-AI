class FeedbackEngine:
    _storage = {}

    @classmethod
    def save_feedback(cls, incident_id, status):
        cls._storage[incident_id] = status

    @classmethod
    def get_feedback(cls, incident_id):
        return cls._storage.get(incident_id, "Pending")

    @classmethod
    def adjust_by_feedback(cls, incident_id, base_score, base_conf):
        status = cls.get_feedback(incident_id)
        if status == "Attack":
            return min(base_score + 15, 100), min(base_conf + 10, 100)
        elif status == "False Positive":
            return base_score * 0.1, base_conf * 0.4
        return base_score, base_conf