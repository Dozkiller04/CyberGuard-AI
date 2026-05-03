class ExplanationEngine:
    @staticmethod
    def get_explanations(pattern):
        tech_map = {
            "Account Compromise (Brute Force Success)": "Credential stuffing detected: Failures followed by success.",
            "Suspicious Remote Access": "Post-auth remote management tool execution.",
            "High-Frequency Anomaly": "Automation detected via high event volume.",
            "Potential Lateral Movement": "Internal network traversal detected.",
            "General Suspicious Activity": "Behavior deviates from baseline."
        }
        simple_map = {
            "Account Compromise (Brute Force Success)": "Someone guessed the password correctly after many tries.",
            "Suspicious Remote Access": "The user opened a remote control tool.",
            "High-Frequency Anomaly": "This looks like a bot, not a human.",
            "Potential Lateral Movement": "The user is jumping between computers.",
            "General Suspicious Activity": "Unusual behavior detected."
        }
        return tech_map.get(pattern, "Heuristic match."), simple_map.get(pattern, "Unusual activity.")