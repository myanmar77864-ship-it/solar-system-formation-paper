import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/cai_age.csv")

plt.figure(figsize=(8,4))
plt.plot(df["Material"], df["Age_Ga"], marker='o')
plt.ylabel("Age (Ga)")
plt.title("CAI Formation Age and Early Solar System Chronology")
plt.grid(True)

plt.tight_layout()
plt.savefig("../figures/figure4.png", dpi=300)
plt.show()
