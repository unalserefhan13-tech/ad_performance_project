import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
START_DATE = datetime(2024, 1, 1)
DAYS = 30

COUNTRIES = ["Turkey", "USA", "Germany", "UK", "France"]

DEFENSE_BRANDS = [
    "ASELSAN", "ROKETSAN", "TUSAS", "TEI", "BAYKAR",
    "HAVELSAN", "STM_Defence", "FNSS", "BMC_Defence"
]

COMMERCIAL_BRANDS = [
    "Apple", "Google", "Amazon", "Microsoft", "Samsung",
    "Nike", "Adidas", "Tesla", "BMW", "Netflix",
    "Spotify", "Uber", "Airbnb", "Booking", "CocaCola",
    "Pepsi", "McDonalds", "Starbucks", "Visa", "Mastercard",
    "Turkish_Airlines", "Pegasus", "Beko", "Vestel", "LC_Waikiki",
    "Migros", "BIM", "A101", "Ford", "Toyota",
    "Honda", "Renault", "Hyundai", "Intel", "Nvidia",
    "Meta", "PayPal", "Stripe", "HSBC", "ING",
    "BNPParibas", "GoldmanSachs", "JPMorgan", "Revolut",
    "Skyscanner", "TripAdvisor", "Bolt", "Lyft", "BlaBlaCar"
]

ALL_BRANDS = DEFENSE_BRANDS + COMMERCIAL_BRANDS

AD_GROUPS = ["Brand", "Generic", "Competitor", "Remarketing"]

# --------------------------------------------------
# DATA GENERATION
# --------------------------------------------------
rows = []

for brand in ALL_BRANDS:
    sector = "Defense" if brand in DEFENSE_BRANDS else "Commercial"

    for ad_group in AD_GROUPS:
        for day in range(DAYS):
            date = START_DATE + timedelta(days=day)
            country = random.choice(COUNTRIES)

            impressions = random.randint(2_000, 150_000)
            clicks = random.randint(80, int(impressions * 0.15))
            cost = round(random.uniform(50, 2500), 2)
            conversions = random.randint(0, int(clicks * 0.4))
            revenue = round(conversions * random.uniform(25, 250), 2)

            rows.append({
                "Date": date.strftime("%Y-%m-%d"),
                "Campaign": f"{brand}_Search",
                "Ad Group": ad_group,
                "Sector": sector,
                "Country": country,
                "Impressions": impressions,
                "Clicks": clicks,
                "Cost": cost,
                "Conversions": conversions,
                "Conv. value": revenue,
            })

df = pd.DataFrame(rows)

# --------------------------------------------------
# EXPORTS
# --------------------------------------------------
df.to_csv("fake_google_ads_full_dataset.csv", index=False)

# Executive summary
summary = df.groupby(["Sector"]).agg(
    Total_Cost=("Cost", "sum"),
    Total_Revenue=("Conv. value", "sum"),
    Avg_CTR=("Clicks", "mean"),
).reset_index()

summary.to_csv("executive_summary.csv", index=False)

print("✅ fake_google_ads_full_dataset.csv created")
print("✅ executive_summary.csv created")
