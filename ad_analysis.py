import pandas as pd

# 1. Veriyi oku
df = pd.read_csv("ads_data.csv")

# 2. Metrikleri hesapla
df["CTR (%)"] = (df["clicks"] / df["impressions"]) * 100
df["CPC"] = df["cost"] / df["clicks"]
df["Conversion Rate (%)"] = (df["conversions"] / df["clicks"]) * 100
df["ROI (%)"] = ((df["revenue"] - df["cost"]) / df["cost"]) * 100

# 3. Sonucu göster
print(df)

import matplotlib.pyplot as plt

# ROI grafiği
plt.bar(df["campaign"], df["ROI (%)"])
plt.title("Campaign ROI Comparison")
plt.xlabel("Campaign")
plt.ylabel("ROI (%)")
plt.show()
