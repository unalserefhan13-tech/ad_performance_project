# Google Ads Performance Dashboard

A professional-grade Google Ads analytics dashboard built with **Python & Streamlit**.  
The project simulates enterprise-level Google Ads performance data and provides actionable insights through KPI analysis and visualizations.

---

## 🚀 Features

- Google Ads–specific CSV validation
- Automated KPI calculations:
  - CTR (%)
  - CPC
  - Conversion Rate (%)
  - ROI (%)
- Campaign-level performance table
- Underperforming campaign detection
- Interactive visualizations
- Executive summary export
- Supports large-scale, multi-brand datasets

---

## 🏢 Dataset Scope

- 100+ real brand names (including defense & commercial sectors)
- Multi-country campaigns
- Time-series data (daily performance)
- Multiple ad groups per campaign
- Synthetic but realistic Google Ads structure

**Defense brands included:**
ASELSAN, ROKETSAN, TUSAŞ, TEI, BAYKAR, HAVELSAN, STM, FNSS, BMC

---

## ⚠️ Ethical Disclaimer

All brands used in this project are real.  
All performance metrics and campaign data are **fully synthetic** and generated for demonstration purposes only.  
No real advertising data is used.

---

## 🧠 Tech Stack

- Python
- Streamlit
- Pandas
- Plotly
- Matplotlib

---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
python fake_google_ads_full_enterprise_dataset.py
streamlit run app.py
