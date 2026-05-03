import pandas as pd
import re
import io
import json
import os

class LogReader:
    @staticmethod
    def fuzzy_find_columns(df):
        """Automatically maps unknown headers to our CyberGuard schema."""
        schema_map = {
            'ip': ['ip', 'source', 'src', 'client', 'addr', 'host', 'remote'],
            'user': ['user', 'account', 'name', 'usr', 'identity', 'uid'],
            'action': ['action', 'event', 'method', 'type', 'cmd', 'operation'],
            'status': ['status', 'res', 'outcome', 'code', 'result', 'err'],
            'timestamp': ['time', 'date', 'ts', '@timestamp', 'datetime']
        }
        
        new_cols = {}
        for internal_name, aliases in schema_map.items():
            for col in df.columns:
                # Convert col to string to avoid errors with numeric headers
                if any(alias in str(col).lower() for alias in aliases):
                    new_cols[col] = internal_name
                    break
        
        df = df.rename(columns=new_cols)
        
        # SELF-HEALING: If columns are STILL missing, create them
        if 'ip' not in df.columns: df['ip'] = "0.0.0.0"
        if 'user' not in df.columns: df['user'] = "system"
        if 'action' not in df.columns: df['action'] = "unknown_activity"
        if 'status' not in df.columns: df['status'] = "info"
        if 'timestamp' not in df.columns: df['timestamp'] = pd.Timestamp.now()
        
        return df

    @staticmethod
    def parse_unstructured(content):
        """Standardizes raw text, syslog, or unknown formats using Regex."""
        ip_regex = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        time_regex = r'(\d{4}-\d{2}-\d{2}.\d{2}:\d{2}:\d{2})'
        
        extracted_data = []
        lines = content.split('\n')
        
        for line in lines:
            if len(line.strip()) < 5: continue
            ip_match = re.search(ip_regex, line)
            time_match = re.search(time_regex, line)
            
            action = "traffic"
            if "login" in line.lower(): action = "login"
            if "shell" in line.lower() or "exec" in line.lower(): action = "remote_shell"
            
            status = "success"
            if any(x in line.lower() for x in ["fail", "deny", "error", "403"]):
                status = "failed"
                
            extracted_data.append({
                'ip': ip_match.group(0) if ip_match else "0.0.0.0",
                'user': "analysed_user",
                'action': action,
                'status': status,
                'timestamp': time_match.group(0) if time_match else pd.Timestamp.now()
            })
        return pd.DataFrame(extracted_data)

    @classmethod
    def load_logs(cls, uploaded_file):
        """Handles both Streamlit Uploads and Local File Paths."""
        try:
            # FIX: Check if we are loading a local path (string) or an upload (object)
            if isinstance(uploaded_file, str):
                filename = os.path.basename(uploaded_file).lower()
                with open(uploaded_file, 'rb') as f:
                    content_bytes = f.read()
            else:
                filename = uploaded_file.name.lower()
                content_bytes = uploaded_file.getvalue()

            # 1. Handle JSON
            if filename.endswith('.json'):
                df = pd.DataFrame(json.loads(content_bytes))
                
            # 2. Handle CSV / TSV
            elif filename.endswith(('.csv', '.tsv')):
                sep = '\t' if filename.endswith('.tsv') else ','
                df = pd.read_csv(io.BytesIO(content_bytes), sep=sep)
                
            # 3. Handle XML
            elif filename.endswith('.xml'):
                df = pd.read_xml(io.BytesIO(content_bytes))
                
            # 4. Handle Everything Else (.log, .txt, .syslog)
            else:
                text_content = content_bytes.decode('utf-8', errors='ignore')
                df = cls.parse_unstructured(text_content)
            
            # Normalize and fix column names
            df = cls.fuzzy_find_columns(df)
            
            # Convert timestamp and handle missing ones
            df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce').fillna(pd.Timestamp.now())
            
            return df
            
        except Exception as e:
            print(f"Universal Parser Error: {e}")
            return None