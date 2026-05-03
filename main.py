import os
import subprocess

def run_app():
    print("Starting Mini SOC Assistant...")
    # Check if data exists
    if not os.path.exists("data/logs.csv"):
        print("Data file not found. Generating sample logs...")
        from data.generate_logs import generate_sample_data
        generate_sample_data()
        
    # Run Streamlit
    subprocess.run(["streamlit", "run", "ui/app.py"])

if __name__ == "__main__":
    run_app()