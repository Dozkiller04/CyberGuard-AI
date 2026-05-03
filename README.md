# 🛡️ CyberGuard AI: Mini SOC Assistant
**AI-Assisted Threat Investigation, Correlation & Intelligence System**

![Cybersecurity](https://img.shields.io/badge/Domain-Cybersecurity-red)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Intelligence](https://img.shields.io/badge/Logic-Heuristic_AI-purple)

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
### 🌟 Advanced Features
- **🚀 Universal Log Parser:** Seamlessly ingest **CSV, JSON, XML, Syslog, and Plain Text (.log/.txt)**. The system uses fuzzy logic to "self-heal" and map any log format to a security schema.
  
- **🧠 Adaptive Intelligence Loop:** Features a "Human-in-the-Loop" system. Marking incidents as "True Attack" or "False Positive" dynamically retrains the risk engine during the session.
  
- **🔍 Explainable AI (XAI):** Translates complex technical sequences into **Simple Language Mode** for management and **Technical Analysis** for senior analysts.
  
- **📡 Threat Intel Integration:** Built-in IP Reputation engine that checks sources against a global (simulated) blacklist of C2 servers and malicious actors.
  
- **📈 Executive Dashboard:** High-level KPIs including Correlated Incident counts, High-Risk distribution, and Attacker Dwell Time.

---
## 🏗️ Modular Architecture
The system is built on 8 specialized intelligence engines:
1. **Log Reader:** Universal parser for all file extensions.
2. **Correlation Engine:** Temporal and entity-based event clustering.
3. **Detection Engine:** Identifies Brute Force, Lateral Movement, and Exfiltration.
4. **Risk Engine:** Adaptive 0-100 scoring based on patterns + Threat Intel + Feedback.
5. **Threat Intel:** Reputation-based IP analysis.
6. **Explanation Engine:** Multi-mode narrative generator.
7. **Feedback Engine:** Session-based memory for analyst decisions.
8. **Investigation Engine:** Automated response playbook generation.

---

## 🛠️ Tech Stack
- **Backend:** Python 3.12 (Modular Architecture)
- **Processing:** Pandas & Regex (High-performance data manipulation)
- **Frontend:** Streamlit (Reactive Dashboard)
- **Logic:** Heuristic State-Machines & Rule-based Intelligence

---

## 📂 Project Structure
```text
mini_SOC_V.12/
├── backend/                        # 🧠 The Intelligence Layer
│   ├── log_reader.py               # Universal Parser (CSV, JSON, XML, TXT)
│   ├── correlation_engine.py       # Event clustering & Session logic
│   ├── detection_engine.py         # Attack chain pattern recognition
│   ├── risk_engine.py              # Adaptive & Intel-driven scoring
│   ├── threat_intel.py             # IP Reputation & Blacklist engine
│   ├── explanation_engine.py       # Technical & Simple Language XAI
│   ├── feedback_engine.py          # Memory layer for analyst decisions
│   └── investigation_engine.py     # Response playbook generator
├── data/                           # 📊 Data Layer
│   ├── generate_logs.py            # Simulated threat dataset generator
│   └── logs.csv                    # Default active log database
├── ui/                             # 🖥️ Presentation Layer
│   └── app.py                      # Advanced Streamlit SOC Dashboard
├── requirements.txt                # Project dependencies
├── .gitignore                      # Ensures a clean repository
└── main.py                         # Application entry point
```

## 🚀 Getting Started

### 1. Installation
**Clone the repository and navigate to the project folder:**
```bash
git clone https://github.com/Dozkiller04/CyberGuard-AI.git
```
**cd CyberGuard-AI**

**Install the required Python dependencies:**
```Bash
pip install -r requirements.txt
```
### 2. Prepare Data
**Generate the simulated log dataset (includes Brute Force, Lateral Movement, and Anomaly scenarios):**
```Bash
python data/generate_logs.py
```
### 3. Launch Dashboard
**Start the SOC Assistant interface:**
```bash
python -m streamlit run ui/app.py
```
### 4. Supported Formats

**Simply drag and drop any of the following:**
**Web Logs:** JSON, XML, CSV
**Server Logs:** .txt, .log, .syslog
**Network Logs:** Exported Netflow/Zeek CSVs

---

### 🖥️ Dashboard Usage

**Executive View:** Monitor real-time KPIs, including High-Risk alerts and Average Dwell Time.

**Triage Feed**: Filter incidents by priority to focus on critical threats.

**Investigate:** Expand any incident to view the Attack Timeline and AI Analysis.

**Feedback Loop:** Use the "True Attack" or "False Positive" buttons to refine the system's scoring.

**Reporting:** Generate and download a professional "Intelligence Report" for documentation.

---

## 📊 Project Gallery

### 1. Executive Dashboard
*Overview of security metrics and real-time threat landscape.*

<img width="1836" height="861" alt="image" src="https://github.com/user-attachments/assets/e3bcf262-d6aa-4880-a002-3482940ecd1e" />


### 2. Intelligent Attack Chain
*A multi-stage incident correlated from raw logs and mapped to MITRE ATT&CK.*

<img width="1845" height="848" alt="image" src="https://github.com/user-attachments/assets/637a6292-ecda-4694-a7de-e2678a0d2509" />


### 3. Adaptive Feedback & XAI
*The analyst feedback loop and Explainable AI summaries.*

<img width="1534" height="778" alt="image" src="https://github.com/user-attachments/assets/c3242980-3308-4fb5-8fbb-9d891cb9702f" />


### 📊 Recommended 
**Executive Dashboard**: Overview of metrics and threat landscape.
**Incident Deep-Dive:** View of the timeline and MITRE mapping.
**Adaptive Feedback:** Showing how risk scores change after analyst input.

### 🔮 Future Scope
**Live Ingestion:** Integration with live Syslog/Windows Event Forwarding.
**Database Backend:** Transitioning from CSV to SQLite/PostgreSQL for persistent feedback storage.
**Advanced AI:** Integrating local LLMs (Ollama/Llama 3) for deeper contextual narrative reporting.

### 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.


