import pandas as pd

class DetectionEngine:
    @staticmethod
    def map_mitre(logs):
        """
        Maps actions to official MITRE ATT&CK techniques for professional reporting.
        """
        mappings = {
            'login': 'T1078 (Valid Accounts)',
            'failed_login': 'T1110 (Brute Force)',
            'remote_shell': 'T1059 (Command and Scripting Interpreter)',
            'data_export': 'T1020 (Automated Exfiltration)',
            'file_access': 'T1083 (File and Directory Discovery)',
            'api_call': 'T1565 (Data Manipulation)'
        }
        
        results = []
        for _, row in logs.iterrows():
            # If login failed, use the Brute Force tag specifically
            if row['action'] == 'login' and row['status'] == 'failed':
                results.append(mappings['failed_login'])
            else:
                results.append(mappings.get(row['action'], "T1204 (User Execution)"))
                
        return list(set(results)) # Return unique techniques

    @staticmethod
    def detect_lateral_movement(inc_df):
        """Checks if a single user/session is hopping across different IP addresses."""
        unique_ips = inc_df['ip'].nunique()
        return unique_ips > 1

    @staticmethod
    def detect_patterns(logs):
        """
        The Brain of the SOC: Analyzes the sequence of events to find the 'Story'.
        """
        actions = list(logs['action'])
        statuses = list(logs['status'])
        
        # 1. PRIORITY: Lateral Movement (Most Dangerous)
        if DetectionEngine.detect_lateral_movement(logs):
            return "Potential Lateral Movement"

        # 2. PRIORITY: Account Compromise (Failed Logins -> Success)
        if 'failed' in statuses and 'success' in statuses:
            # Find the first success index
            first_success = statuses.index('success')
            # Check if there were failures BEFORE the success
            failures_before = statuses[:first_success].count('failed')
            
            if failures_before >= 3:
                return "Account Compromise (Brute Force Success)"
            elif failures_before > 0:
                return "Suspicious Login Sequence"

        # 3. PRIORITY: Exfiltration
        if 'data_export' in actions:
            return "Data Exfiltration Attempt"

        # 4. PRIORITY: Remote Execution
        if 'remote_shell' in actions:
            return "Suspicious Remote Access"

        # 5. PRIORITY: Volume Based Anomaly
        if len(logs) > 10:
            return "High-Frequency API/Access Anomaly"

        # Fallback
        return "General Suspicious Activity"