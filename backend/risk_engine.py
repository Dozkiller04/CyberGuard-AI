from backend.feedback_engine import FeedbackEngine

# Safety Import for ThreatIntel
try:
    from backend.threat_intel import ThreatIntel
except ImportError:
    # Fallback if the file is missing or broken
    class ThreatIntel:
        @classmethod
        def check_ip(cls, ip): return False, "Intel Service Unavailable"

class RiskEngine:
    @staticmethod
    def calculate_risk(incident_logs, pattern, incident_id=None):
        score = 0
        confidence = 85
        
        # 1. Threat Intel Check
        source_ip = incident_logs.iloc[0]['ip']
        is_blacklisted, intel_reason = ThreatIntel.check_ip(source_ip)
        
        # 2. Base weights
        pattern_weights = {
            "Potential Lateral Movement": 90,
            "Account Compromise (Brute Force Success)": 80,
            "Suspicious Remote Access": 75,
            "High-Frequency Anomaly": 45,
            "General Suspicious Activity": 20
        }
        
        score = pattern_weights.get(pattern, 15)

        # 3. Apply Intel Boost
        if is_blacklisted:
            score = 100
            confidence = 100

        # 4. Feedback Adjustment
        if incident_id is not None:
            score, confidence = FeedbackEngine.adjust_by_feedback(incident_id, score, confidence)
        
        # Determine Level
        if score >= 75:
            return "HIGH", int(score), int(confidence)
        elif score >= 40:
            return "MEDIUM", int(score), int(confidence)
        else:
            return "LOW", int(score), int(confidence)