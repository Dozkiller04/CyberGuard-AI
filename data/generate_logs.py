import pandas as pd
from datetime import datetime, timedelta
import random

def generate_sample_data():
    now = datetime.now()
    logs = [
        # Incident 1: Brute Force Success (Account Compromise)
        [now - timedelta(minutes=60), "192.168.1.50", "admin", "login", "failed"],
        [now - timedelta(minutes=59), "192.168.1.50", "admin", "login", "failed"],
        [now - timedelta(minutes=58), "192.168.1.50", "admin", "login", "failed"],
        [now - timedelta(minutes=57), "192.168.1.50", "admin", "login", "success"],
        [now - timedelta(minutes=55), "192.168.1.50", "admin", "file_access", "success"],
        [now - timedelta(minutes=54), "192.168.1.50", "admin", "data_export", "success"],
        
        # Incident 2: Suspicious Remote Access
        [now - timedelta(minutes=30), "45.33.22.11", "guest", "login", "success"],
        [now - timedelta(minutes=28), "45.33.22.11", "guest", "remote_shell", "success"],
        
        # Incident 3: High Frequency Anomaly
        [now - timedelta(minutes=10), "10.0.0.5", "svc_account", "api_call", "success"],
        [now - timedelta(minutes=10), "10.0.0.5", "svc_account", "api_call", "success"],
        [now - timedelta(minutes=10), "10.0.0.5", "svc_account", "api_call", "success"],
        [now - timedelta(minutes=10), "10.0.0.5", "svc_account", "api_call", "success"],
    ]
    
    df = pd.DataFrame(logs, columns=["timestamp", "ip", "user", "action", "status"])
    df.to_csv("data/logs.csv", index=False)
    print("Sample logs generated in data/logs.csv")

if __name__ == "__main__":
    generate_sample_data()