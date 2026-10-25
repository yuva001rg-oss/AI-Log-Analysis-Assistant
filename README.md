# AI Log Analysis Assistant

## Project Overview
A Python-based cybersecurity project that analyzes synthetic security logs and identifies potentially suspicious activities using rule-based threat detection.

## Features
- Analyze security logs from CSV files.
- Detect repeated failed login attempts.
- Classify events as High, Medium, Low, or Normal.
- Display security statistics and threat charts.
- Filter logs by threat level.
- Download analyzed logs as CSV.

## Technologies Used
- Python
- Streamlit
- Pandas

## Project Structure
- app.py — Streamlit dashboard and threat analysis.
- generate_logs.py — Generates synthetic security logs.
- synthetic_logs.csv — Sample security log data.
- requirements.txt — Required Python packages.

## Installation and Usage

1. Clone the repository:
   `git clone https://github.com/yuva001rg-oss/AI-Log-Analysis-Assistant.git`

2. Open the project folder:
   `cd AI-Log-Analysis-Assistant`

3. Install dependencies:
   `pip install -r requirements.txt`

4. Generate sample logs:
   `python generate_logs.py`

5. Run the application:
   `streamlit run app.py`

## Threat Classification
- High: Repeated failed login attempts from the same IP address.
- Medium: Failed login or permission-denied events.
- Low: Events with an error status.
- Normal: Other routine events.

## Future Enhancements
- Machine-learning-based anomaly detection.
- Real-time log monitoring.
- Additional log formats and alert notifications.

## Disclaimer
This educational project uses synthetic logs and rule-based detection. It does not currently use a trained AI model and is not intended for production-grade security monitoring.

## Author
Yuva — Cyber Security Student
