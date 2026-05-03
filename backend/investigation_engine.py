class InvestigationEngine:
    @staticmethod
    def generate_explanation(pattern, risk_level):
        explanations = {
            "Account Compromise (Brute Force Success)": "An external entity attempted multiple passwords and eventually gained access.",
            "Suspicious Remote Access": "A remote shell or unauthorized access tool was executed post-login.",
            "High-Frequency Anomaly": "The account is performing actions at a rate impossible for a human user.",
        }
        return explanations.get(pattern, "General suspicious activity detected from this source.")

    @staticmethod
    def get_recommendations(risk_level):
        if risk_level == "HIGH":
            return ["Isolate Host", "Reset User Password", "Revoke Active Sessions", "Enable MFA"]
        if risk_level == "MEDIUM":
            return ["Review Audit Logs", "Contact User for Verification", "Monitor IP activity"]
        return ["No immediate action required", "Continue monitoring"]