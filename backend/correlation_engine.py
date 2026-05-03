import pandas as pd

class CorrelationEngine:
    def __init__(self, time_window_minutes=30):
        self.time_window = time_window_minutes

    def group_incidents(self, df):
        incidents = []
        # Group by IP and User
        grouped = df.groupby(['ip', 'user'])
        
        for (ip, user), group in grouped:
            group = group.sort_values('timestamp')
            
            current_incident_logs = []
            last_time = None
            
            for _, row in group.iterrows():
                if last_time is None or (row['timestamp'] - last_time).seconds / 60 <= self.time_window:
                    current_incident_logs.append(row)
                else:
                    incidents.append(pd.DataFrame(current_incident_logs))
                    current_incident_logs = [row]
                last_time = row['timestamp']
            
            if current_incident_logs:
                incidents.append(pd.DataFrame(current_incident_logs))
                
        return incidents