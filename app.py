import streamlit as st
import pandas as pd

from utils import (
    normalize_google_ads_columns,
    validate_google_ads_schema,
    convert_cost_micros,
    calculate_metrics,
    campaign_summary,
    detect_weak_campaigns,
    generate_insights,
)

# --------------------------------------------------
# STREAMLIT CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Google Ads Performance Dashboard",
    layout="wide",
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.title("📊 Google Ads Performance Dashboard")
st.caption("Advanced analytics for Google Ads performance CSV exports")

# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------
uploaded_file = st.file_uploader(
    "Upload Google Ads Performance CSV",
    type="csv",
)

if uploaded_file is None:
    st.info("Please upload a Google Ads performance CSV export.")
    st.stop()

# --------------------------------------------------
# LOAD & PROCESS DATA
# --------------------------------------------------
try:
    df = pd.read_csv(uploaded_file)

    df = normalize_google_ads_columns(df)
    validate_google_ads_schema(df)
    df = convert_cost_micros(df)
    df = calculate_metrics(df)

except Exception as e:
    st.error("❌ Invalid Google Ads performance CSV")
    st.code(str(e))
    st.stop()

# --------------------------------------------------
# SUMMARY KPIs
# --------------------------------------------------
summary = campaign_summary(df)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Cost", f"{summary['Total Cost']}")
c2.metric("Total Revenue", f"{summary['Total Revenue']}")
c3.metric("Average ROI (%)", f"{summary['Average ROI (%)']}")
c4.metric("Avg Conversion Rate (%)", f"{summary['Avg Conversion Rate (%)']}")

# --------------------------------------------------
# AUTO INSIGHTS
# --------------------------------------------------
st.subheader("🔍 Automated Insights")
insights = generate_insights(df)

for insight in insights:
    st.info(insight)

# --------------------------------------------------
# WEAK CAMPAIGNS
# --------------------------------------------------
st.subheader("⚠️ Underperforming Campaigns")

weak = detect_weak_campaigns(df)

if weak.empty:
    st.success("No critical underperforming campaigns detected.")
else:
    st.dataframe(weak, use_container_width=True)

# --------------------------------------------------
# FULL DATA TABLE
# --------------------------------------------------
st.subheader("📄 Campaign Performance Data")
st.dataframe(df, use_container_width=True)

# --------------------------------------------------
# VISUALS
# --------------------------------------------------
st.subheader("📈 Performance Visualizations")

if "campaign" in df.columns:
    col1, col2 = st.columns(2)

    with col1:
        st.bar_chart(
            df.groupby("campaign")["ROI (%)"].mean()
        )

    with col2:
        st.bar_chart(
            df.groupby("campaign")["Cost"].sum()
            if "Cost" in df.columns else df.groupby("campaign")["cost"].sum()
        )
