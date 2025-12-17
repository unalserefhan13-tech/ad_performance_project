import pandas as pd
import random

random.seed(42)

BRANDS = [
    # 🇹🇷 Turkey (Defense & Tech)
    "ASELSAN_Search",
    "ROKETSAN_Search",
    "TUSAS_Search",
    "TEI_Search",
    "BAYKAR_Search",
    "HAVELSAN_Search",
    "STM_Defence_Search",
    "BMC_Defence_Search",
    "FNSS_Defence_Search",
    "TURKSAT_Search",

    # 🇹🇷 Turkey (Commercial)
    "Turkish_Airlines_Search",
    "Pegasus_Airlines_Search",
    "Beko_Search",
    "Arcelik_Search",
    "Vestel_Search",
    "LC_Waikiki_Search",
    "Koton_Search",
    "Migros_Search",
    "A101_Search",
    "BIM_Search",

    # 🌍 Global Tech
    "Apple_Search",
    "Google_Search",
    "Microsoft_Search",
    "Amazon_Search",
    "Meta_Search",
    "Netflix_Search",
    "Spotify_Search",
    "Samsung_Search",
    "Intel_Search",
    "Nvidia_Search",

    # 🌍 Global Consumer
    "Nike_Search",
    "Adidas_Search",
    "Puma_Search",
    "CocaCola_Display",
    "Pepsi_Display",
    "McDonalds_Display",
    "BurgerKing_Display",
    "Starbucks_Display",
    "Unilever_Display",
    "Nestle_Display",

    # 🌍 Automotive
    "Tesla_Search",
    "BMW_Search",
    "Mercedes_Search",
    "Audi_Search",
    "Volkswagen_Search",
    "Toyota_Search",
    "Ford_Search",
    "Hyundai_Search",
    "Renault_Search",
    "Honda_Search",

    # 🌍 Finance & Services
    "Visa_Search",
    "Mastercard_Search",
    "PayPal_Search",
    "Stripe_Search",
    "GoldmanSachs_Search",
    "JPMorgan_Search",
    "HSBC_Search",
    "ING_Search",
    "BNPParibas_Search",
    "Revolut_Search",

    # 🌍 Travel & Platforms
    "Uber_Search",
    "Airbnb_Search",
    "Booking_Search",
    "Expedia_Search",
    "Trivago_Search",
    "Skyscanner_Search",
    "TripAdvisor_Search",
    "Bolt_Search",
    "Lyft_Search",
    "BlaBlaCar_Search",
]

rows = []

for campaign in BRANDS:
    for _ in range(12):  # her marka için 12 satır
        impressions = random.randint(3_000, 120_000)
        clicks = random.randint(100, int(impressions * 0.15))
        cost = round(random.uniform(80, 2000), 2)
        conversions = random.randint(0, int(clicks * 0.4))
        revenue = round(conversions * random.uniform(30, 220), 2)

        rows.append({
            "Campaign": campaign,
            "Impressions": impressions,
            "Clicks": clicks,
            "Cost": cost,
            "Conversions": conversions,
            "Conv. value": revenue,
        })

df = pd.DataFrame(rows)

df.to_csv("fake_google_ads_100_real_brands.csv", index=False)

print("✅ fake_google_ads_100_real_brands.csv created")
