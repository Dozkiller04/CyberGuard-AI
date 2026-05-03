from backend.feedback_engine import FeedbackEngine

class RiskEngine:
    @staticmethod
    def calculate_risk(incident_logs, pattern, incident_id=None):
        """
        Calculates risk score based on pattern and adjusts it 
        based on Analyst Feedback.
        """
        score = 0
        
        # Base weights for different attack patterns
        pattern_weights = {
            "Potential Lateral Movement": 90,
            "Account Compromise (Brute Force Success)": 80,
            "Suspicious Remote Access": 75,
            "High-Frequency Anomaly": 45,
            "General Suspicious Activity": 20
        }
        
        # 1. Get base score from pattern
        score = pattern_weights.get(pattern, 15)
        confidence = 85 # Initial confidence level
        
        # 2. ADAPTIVE LOGIC: Check if Analyst has provided feedback
        # This is where the 3rd argument (incident_id) is used
        if incident_id is not None:
            score, confidence = FeedbackEngine.adjust_by_feedback(incident_id, score, confidence)
        
        # 3. Categorize Risk
        if score >= 75:
            return "HIGH", int(score), int(confidence)
        elif score >= 40:
            return "MEDIUM", int(score), int(confidence)
        else:
            return "LOW", int(score), int(confidence)