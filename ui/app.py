import streamlit as st
import pandas as pd
import sys
import os
from datetime import datetime
from backend.explanation_engine import ExplanationEngine
from backend.feedback_engine import FeedbackEngine

# --- ROBUST PATH FIX ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

try:
    from backend.log_reader import LogReader
    from backend.correlation_engine import CorrelationEngine
    from backend.detection_engine import DetectionEngine
    from backend.risk_engine import RiskEngine
    from backend.investigation_engine import InvestigationEngine
except ImportError as e:
    st.error(f"❌ Backend Import Error: {e}")

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="CyberGuard AI | SOC Assistant", layout="wide", page_icon="🛡️"
)

# --- CUSTOM CSS FOR UI ---
st.markdown(
    """
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1e2130; padding: 15px; border-radius: 10px; border: 1px solid #3e4255; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🛡️ CyberGuard AI - Advanced SOC Assistant")
st.markdown("---")

# --- SIDEBAR & DATA LOADING ---
st.sidebar.header("📥 Ingestion Layer")
uploaded_file = st.sidebar.file_uploader("Upload Raw Logs (CSV)", type="csv")

if uploaded_file is None:
    if os.path.exists("data/logs.csv"):
        df = LogReader.load_logs("data/logs.csv")
        st.sidebar.success("✅ Loaded: data/logs.csv")
    else:
        st.sidebar.warning("⚠️ No logs found. Please run data/generate_logs.py")
        df = None
else:
    df = LogReader.load_logs(uploaded_file)

if df is not None:
    # --- 1. CORE LOGIC (Process everything first) ---
    ce = CorrelationEngine()
    incidents = ce.group_incidents(df)

    # Pre-calculate overall stats for the dashboard
    high_risk_count = 0
    med_risk_count = 0
    low_risk_count = 0
    risk_data = []

    processed_incidents = []
    for inc_df in incidents:
        pattern = DetectionEngine.detect_patterns(inc_df)
        risk_lvl, risk_score, confidence = RiskEngine.calculate_risk(inc_df, pattern)

        # Track stats
        if risk_lvl == "HIGH":
            high_risk_count += 1
        elif risk_lvl == "MEDIUM":
            med_risk_count += 1
        else:
            low_risk_count += 1

        risk_data.append({"Pattern": pattern, "Risk": risk_lvl, "Score": risk_score})
        processed_incidents.append(
            {
                "df": inc_df,
                "pattern": pattern,
                "risk_lvl": risk_lvl,
                "score": risk_score,
                "conf": confidence,
            }
        )

    # --- 2. EXECUTIVE DASHBOARD ---
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    m_col1.metric("Total Events", len(df))
    m_col2.metric("Correlated Incidents", len(incidents))
    m_col3.metric(
        "High Risk Alerts", high_risk_count, delta="CRITICAL", delta_color="inverse"
    )

    # Calculate Dwell Time (Simple Average)
    dwell_times = [
        (i["df"]["timestamp"].max() - i["df"]["timestamp"].min()).seconds / 60
        for i in processed_incidents
    ]
    avg_dwell = sum(dwell_times) / len(dwell_times) if dwell_times else 0
    m_col4.metric("Avg Dwell Time", f"{avg_dwell:.1f} mins")

    # --- 3. RISK VISUALIZATION ---
    st.markdown("### 📊 Threat Landscape")
    chart_col1, chart_col2 = st.columns([2, 1])

    with chart_col1:
        risk_df = pd.DataFrame(risk_data)
        if not risk_df.empty:
            st.bar_chart(risk_df["Risk"].value_counts(), color="#ff4b4b")

    with chart_col2:
        st.write("**Quick Analysis**")
        st.info(
            f"The most common pattern detected is: **{risk_df['Pattern'].mode()[0] if not risk_df.empty else 'N/A'}**"
        )

    st.markdown("---")

# --- 4. INCIDENT INVESTIGATION FEED ---
    st.header("🔍 Incident Investigation Feed")

    # Create Tabs
    tab_all, tab_high = st.tabs(["All Incidents", "🔥 High Priority Only"])

    # UPGRADED FUNCTION: Integrated Intelligence Engine & Feedback Loop
    def display_incident(item, idx, tab_id):
        # 1. ANALYST FEEDBACK LOGIC
        inc_id = f"INC-{idx}" # Unique ID for this incident
        
        # Recalculate Risk and Confidence based on Analyst Feedback (Adaptive Scoring)
        # This calls the updated RiskEngine which checks the FeedbackEngine
        risk_lvl, risk_score, confidence = RiskEngine.calculate_risk(item['df'], item['pattern'], inc_id)
        
        # 2. EXPLANATION ENGINE (Technical + Simple Language)
        tech_explanation, simple_explanation = ExplanationEngine.get_explanations(item['pattern'])

        # Dynamic Color Coding based on ADAPTIVE score
        header_color = "🔴" if risk_lvl == "HIGH" else "🟠" if risk_lvl == "MEDIUM" else "🟢"

        with st.expander(
            f"{header_color} INCIDENT #{idx+1}: {item['pattern']} (Risk: {risk_lvl} - {risk_score}%)"
        ):
            col1, col2 = st.columns([1, 2])

            with col1:
                st.markdown("#### 📝 Identity & Risk")
                st.write(f"**Source IP:** `{item['df'].iloc[0]['ip']}`")
                st.write(f"**User:** `{item['df'].iloc[0]['user']}`")
                
                # Visual Risk Gauge
                st.progress(risk_score / 100, text=f"Risk Score: {risk_score}%")
                st.write(f"**AI Confidence:** {confidence}%")

                st.markdown("#### 🏷️ MITRE ATT&CK")
                mitre_tags = DetectionEngine.map_mitre(item["df"])
                for tag in set(mitre_tags):
                    st.code(tag, language=None)
                
                # --- NEW: ANALYST FEEDBACK SYSTEM ---
                st.markdown("---")
                st.markdown("#### 🧠 Analyst Intelligence")
                current_status = FeedbackEngine.get_feedback(inc_id)
                st.write(f"Current Status: **{current_status}**")
                
                btn_col1, btn_col2 = st.columns(2)
                if btn_col1.button("🔥 True Attack", key=f"bt_att_{tab_id}_{idx}", use_container_width=True):
                    FeedbackEngine.save_feedback(inc_id, "Attack")
                    st.rerun() # Refresh UI to show new risk score
                    
                if btn_col2.button("✅ False Positive", key=f"bt_fp_{tab_id}_{idx}", use_container_width=True):
                    FeedbackEngine.save_feedback(inc_id, "False Positive")
                    st.rerun() # Refresh UI to show new risk score

            with col2:
                # --- NEW: EXPLANATION ENGINE OUTPUT ---
                st.markdown("#### 🤖 AI Investigation Reasoning")
                
                with st.container(border=True):
                    st.markdown("**Technical Analysis:**")
                    st.write(tech_explanation)
                    
                    st.markdown("**Simple Language Mode:**")
                    st.info(f"💡 {simple_explanation}")

                st.markdown("#### ⏳ Activity Timeline")
                st.dataframe(
                    item["df"][["timestamp", "action", "status"]],
                    use_container_width=True,
                )

                st.markdown("#### 🛠️ Response Playbook")
                recs = InvestigationEngine.get_recommendations(risk_lvl)
                for r in recs:
                    st.checkbox(r, key=f"{tab_id}_check_{idx}_{r}")

                # --- 5. REPORT EXPORTER (Updated with new intelligence) ---
                report_text = f"""SOC INCIDENT REPORT
===========================
Incident ID: {inc_id}
Feedback Status: {current_status}
Pattern: {item['pattern']}
Risk Level: {risk_lvl} ({risk_score}%)
Confidence: {confidence}%

TECHNICAL EXPLANATION:
{tech_explanation}

SIMPLE SUMMARY:
{simple_explanation}

RECOMMENDED STEPS:
{chr(10).join(['- ' + r for r in recs])}
"""
                st.download_button(
                    label="📄 Download Full Intelligence Report",
                    data=report_text,
                    file_name=f"Intelligence_Report_{inc_id}.txt",
                    mime="text/plain",
                    key=f"{tab_id}_dl_{idx}",
                )

    # --- RENDER TABS ---
    with tab_all:
        for i, item in enumerate(processed_incidents):
            display_incident(item, i, "all")

    with tab_high:
        # High Priority logic: Now filters based on the ADAPTIVE risk score
        high_priority_count = 0
        for i, item in enumerate(processed_incidents):
            # Recalculate to see if it's still HIGH after feedback
            r_lvl, _, _ = RiskEngine.calculate_risk(item['df'], item['pattern'], f"INC-{i}")
            if r_lvl == "HIGH":
                display_incident(item, i, "high")
                high_priority_count += 1
        
        if high_priority_count == 0:
            st.success("✅ No High-Risk incidents found!")

else:
    st.info("👋 Welcome! Please upload a log file or ensure data/logs.csv is generated to begin.")    