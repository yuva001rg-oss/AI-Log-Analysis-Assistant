import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Log Analysis Assistant",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI Log Analysis Assistant")
st.write("Analyze synthetic security logs and detect suspicious activity.")

try:
    df = pd.read_csv("synthetic_logs.csv")
except FileNotFoundError:
    st.error("Please run generate_logs.py first.")
    st.stop()

# Detect suspicious activity
failed = df[df["event_type"] == "Failed Login"]
counts = failed["ip_address"].value_counts()

def detect_threat(row):
    if (
        row["event_type"] == "Failed Login"
        and counts.get(row["ip_address"], 0) >= 5
    ):
        return "High"
    elif row["event_type"] == "Failed Login":
        return "Medium"
    elif row["event_type"] == "Permission Denied":
        return "Medium"
    elif row["status"] == "ERROR":
        return "Low"
    return "Normal"

df["threat_level"] = df.apply(detect_threat, axis=1)

# Dashboard metrics
c1, c2, c3 = st.columns(3)
c1.metric("Total Logs", len(df))
c2.metric("High Risk Events", (df["threat_level"] == "High").sum())
c3.metric("Medium Risk Events", (df["threat_level"] == "Medium").sum())

st.subheader("Threat Summary")
st.bar_chart(df["threat_level"].value_counts())

st.subheader("Security Logs")
levels = st.multiselect(
    "Filter by threat level",
    ["High", "Medium", "Low", "Normal"],
    default=["High", "Medium", "Low", "Normal"]
)

filtered = df[df["threat_level"].isin(levels)]
st.dataframe(filtered, use_container_width=True)

st.subheader("Security Analysis")
if not filtered.empty:
    high_logs = filtered[filtered["threat_level"] == "High"]

    if not high_logs.empty:
        st.warning(
            "Repeated failed logins detected. "
            "Investigate the source IP and authentication records."
        )
    else:
        st.info("No high-risk events in the selected results.")

st.download_button(
    "Download analyzed logs",
    df.to_csv(index=False).encode("utf-8"),
    file_name="analyzed_logs.csv",
    mime="text/csv"
)