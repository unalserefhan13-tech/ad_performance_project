import pandas as pd

# --------------------------------------------------
# COLUMN NORMALIZATION
# --------------------------------------------------
def normalize_google_ads_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.lower()
    )

    mapping = {
        "campaign": "campaign",
        "campaign name": "campaign",

        "impressions": "impressions",

        "clicks": "clicks",
        "clicks (all)": "clicks",

        "cost": "cost",
        "cost (usd)": "cost",
        "cost (eur)": "cost",
        "cost micros": "cost_micros",

        "conversions": "conversions",
        "all conv.": "conversions",
        "all conversions": "conversions",

        "conv. value": "revenue",
        "conversion value": "revenue",
        "all conv. value": "revenue",
        "revenue": "revenue",
    }

    df.rename(columns=mapping, inplace=True)
    return df


# --------------------------------------------------
# SCHEMA VALIDATION
# --------------------------------------------------
def validate_google_ads_schema(df: pd.DataFrame):
    required = {
        "impressions",
        "clicks",
        "conversions",
        "revenue",
    }

    if not ("cost" in df.columns or "cost_micros" in df.columns):
        raise ValueError("Missing cost or cost micros column")

    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


# --------------------------------------------------
# COST MICROS
# --------------------------------------------------
def convert_cost_micros(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "cost" not in df.columns and "cost_micros" in df.columns:
        df["cost"] = df["cost_micros"] / 1_000_000

    return df


# --------------------------------------------------
# KPI CALCULATIONS
# --------------------------------------------------
def calculate_metrics(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["CTR (%)"] = (df["clicks"] / df["impressions"]) * 100
    df["CPC"] = df["cost"] / df["clicks"]
    df["Conversion Rate (%)"] = (df["conversions"] / df["clicks"]) * 100
    df["ROI (%)"] = ((df["revenue"] - df["cost"]) / df["cost"]) * 100

    return df


# --------------------------------------------------
# SUMMARY
# --------------------------------------------------
def campaign_summary(df: pd.DataFrame) -> dict:
    return {
        "Total Cost": round(df["cost"].sum(), 2),
        "Total Revenue": round(df["revenue"].sum(), 2),
        "Average ROI (%)": round(df["ROI (%)"].mean(), 2),
        "Avg Conversion Rate (%)": round(df["Conversion Rate (%)"].mean(), 2),
    }


# --------------------------------------------------
# WEAK CAMPAIGN DETECTION
# --------------------------------------------------
def detect_weak_campaigns(df: pd.DataFrame) -> pd.DataFrame:
    if "campaign" not in df.columns:
        return pd.DataFrame()

    grouped = df.groupby("campaign").agg({
        "ROI (%)": "mean",
        "cost": "sum",
        "Conversion Rate (%)": "mean",
    }).reset_index()

    weak = grouped[
        (grouped["ROI (%)"] < 0) |
        (grouped["Conversion Rate (%)"] < 1)
    ]

    return weak.sort_values("ROI (%)")


# --------------------------------------------------
# AUTO INSIGHTS
# --------------------------------------------------
def generate_insights(df: pd.DataFrame) -> list:
    insights = []

    avg_roi = df["ROI (%)"].mean()
    avg_ctr = df["CTR (%)"].mean()

    if avg_roi < 0:
        insights.append(
            "Overall ROI is negative. Budget optimization is strongly recommended."
        )

    high_cost_low_roi = df[
        (df["cost"] > df["cost"].mean()) &
        (df["ROI (%)"] < 0)
    ]

    if not high_cost_low_roi.empty:
        insights.append(
            "Some campaigns have high spend but negative ROI. Consider pausing or optimizing them."
        )

    if avg_ctr < 1:
        insights.append(
            "Average CTR is low. Ad creatives or targeting may need improvement."
        )

    if not insights:
        insights.append(
            "Campaign performance looks healthy. No critical issues detected."
        )

    return insights
