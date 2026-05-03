class ThreatIntel:
    """
    Threat Intelligence Engine:
    Simulates a database of known malicious IPs.
    """
    # Blacklist of malicious IPs
    BLACKLIST = [
        "45.33.22.11", 
        "185.220.101.1", 
        "103.15.28.2",
        "192.168.1.50" # This matches sample data
    ]

    @classmethod
    def check_ip(cls, ip):
        """Checks if an IP exists in the blacklist."""
        if ip in cls.BLACKLIST:
            return True, "IP identified in Global Blacklist (Known C2/Malicious)"
        return False, "IP not found in Threat Intel database"