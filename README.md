# 🛡️ CyberGuard AI: Mini SOC Assistant
**AI-Assisted Threat Investigation, Correlation & Intelligence System**

![Cybersecurity](https://img.shields.io/badge/Domain-Cybersecurity-red)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 Project Overview
CyberGuard AI is an intelligent Security Operations Center (SOC) assistant designed to combat **Alert Fatigue**. Instead of overwhelming analysts with thousands of isolated logs, the system uses a custom **Heuristic Correlation Engine** to transform raw data into structured, multi-stage **Attack Chains**.

This platform provides **Explainable AI (XAI)** insights, translating complex security events into both technical analysis and simple, non-technical language. It also features an **Adaptive Learning Loop** that refines risk scores based on real-time analyst feedback.

---

## 🧠 Core Intelligence Features

### 1. Heuristic Correlation & Investigation
- **Attack Chain Reconstruction:** Groups isolated events (Logins, File Access, API calls) into unified incidents based on IP, User, and temporal windows.
- **Dwell Time Analysis:** Automatically calculates the time between the attacker's initial entry and the final detected action.

### 2. Explainable AI (XAI) Engine
- **Technical Mode:** Deep-dive analysis of event sequences for senior analysts.
- **Simple Language Mode:** Human-readable summaries (e.g., *"Someone successfully guessed a password after multiple attempts"*) for rapid triage.

### 3. Adaptive Risk Scoring (Human-in-the-Loop)
- **Analyst Feedback Loop:** Analysts can mark incidents as "True Attack" or "False Positive."
- **Dynamic Confidence:** The system automatically adjusts risk scores and dashboard priority based on analyst decisions.

### 4. Industry Standard Mapping
- **MITRE ATT&CK Integration:** Automatically maps detected behaviors to official techniques (e.g., T1110 - Brute Force, T1021 - Lateral Movement).

---

## 🛠️ Tech Stack
- **Backend:** Python 3.12 (Modular Engine Architecture)
- **Processing:** Pandas (High-speed log correlation)
- **Frontend:** Streamlit (Reactive SOC Dashboard)
- **Logic:** Heuristic State-Machines & Rule-based Intelligence

---

## 📂 Project Structure
```text
mini_SOC_V.12/
├── backend/                # Intelligence & Logic Engines
│   ├── log_reader.py       # Data parsing
│   ├── detection_engine.py  # Pattern recognition
│   ├── risk_engine.py       # Adaptive risk scoring
│   ├── feedback_engine.py   # Analyst feedback memory
│   ├── explanation_engine.py# Technical & Simple reasoning
│   └── ...                 
├── data/                   # Data Layer
│   ├── generate_logs.py    # Simulated threat generator
│   └── logs.csv            # Active log database
├── ui/                     # Presentation Layer
│   └── app.py              # Streamlit Dashboard
└── requirements.txt        # Dependencies

## 🚀 Getting Started

### 1. Installation
Clone the repository and navigate to the project folder:
```bash
git clone https://github.com/Dozkiller04/CyberGuard-AI.git
cd CyberGuard-AI

Install the required Python dependencies:
code
Bash
2. Prepare Data
Generate the simulated log dataset (includes Brute Force, Lateral Movement, and Anomaly scenarios):
code
Bash
python data/generate_logs.py
3. Launch Dashboard
Start the SOC Assistant interface:
code
Bash
python -m streamlit run ui/app.py
🖥️ Dashboard Usage
Executive View: Monitor real-time KPIs, including High-Risk alerts and Average Dwell Time.
Triage Feed: Filter incidents by priority to focus on critical threats.
Investigate: Expand any incident to view the Attack Timeline and AI Analysis.
Feedback Loop: Use the "True Attack" or "False Positive" buttons to refine the system's scoring.
Reporting: Generate and download a professional "Intelligence Report" for documentation.
📊 Recommended Screenshots (To be added)
Executive Dashboard: Overview of metrics and threat landscape.
Incident Deep-Dive: View of the timeline and MITRE mapping.
Adaptive Feedback: Showing how risk scores change after analyst input.
🔮 Future Scope
Live Ingestion: Integration with live Syslog/Windows Event Forwarding.
Database Backend: Transitioning from CSV to SQLite/PostgreSQL for persistent feedback storage.
Advanced AI: Integrating local LLMs (Ollama/Llama 3) for deeper contextual narrative reporting.
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
