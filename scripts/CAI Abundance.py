import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/cai_abundance.csv")

plt.figure(figsize=(7,4))
plt.bar(df["Group"], df["AreaPercent"])

plt.ylabel("CAI Area (%)")
plt.xlabel("Carbonaceous Chondrite Group")
plt.title("Distribution of CAIs in Carbonaceous Chondrites")

plt.tight_layout()
plt.savefig("../figures/figure5.png", dpi=300)
plt.show()
