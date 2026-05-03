import pandas as pd

class LogReader:
    @staticmethod
    def load_logs(filepath):
        try:
            df = pd.read_csv(filepath)
            if 'timestamp' in df.columns:
                df['timestamp'] = pd.to_datetime(df['timestamp'])
                return df.sort_values(by='timestamp')
            return df
        except Exception as e:
            print(f"Error loading logs: {e}")
            return pd.DataFrame()