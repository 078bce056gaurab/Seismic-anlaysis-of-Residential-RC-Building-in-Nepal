import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'Times New Roman'

df = pd.read_csv('/Users/niraj/Downloads/Projects/Project_Geo_Lab/Building/Combined.csv')

pga = df["PGA (g)"]

columns = {
    "IO Bare": "PoE (IO Bare)",
    "IO Steel": "PoE (IO Steel Angle)",
    "IO Jacketing": "PoE (IO Concrete Jacketing)",
    
    "LS Bare": "PoE (LS Bare)",
    "LS Steel": "PoE (LS Steel Angle)",
    "LS Jacketing": "PoE (LS Concrete Jacketing)",
    
    "CP Bare": "PoE (CP Bare)",
    "CP Steel": "PoE (CP Steel Angle)",
    "CP Jacketing": "PoE (CP Concrete Jacketing)",
}

plt.figure(figsize=(10, 7))

plt.plot(pga, df[columns["IO Bare"]], color="tab:blue", linewidth=1.75, label="Bare")
plt.plot(pga, df[columns["IO Steel"]], color="tab:orange", linewidth=1.75, label="Steel Angle")
plt.plot(pga, df[columns["IO Jacketing"]], color="tab:green", linewidth=1.75, label="Concrete Jacketing")

plt.plot(pga, df[columns["LS Bare"]], color="tab:blue", linewidth=1.75)
plt.plot(pga, df[columns["LS Steel"]], color="tab:orange", linewidth=1.75)
plt.plot(pga, df[columns["LS Jacketing"]], color="tab:green", linewidth=1.75)

plt.plot(pga, df[columns["CP Bare"]], color="tab:blue", linewidth=1.75)
plt.plot(pga, df[columns["CP Steel"]], color="tab:orange", linewidth=1.75)
plt.plot(pga, df[columns["CP Jacketing"]], color="tab:green", linewidth=1.75)

plt.xlabel("PGA (g)", fontsize=15)
plt.ylabel("Probability of Exceedance", fontsize=15)
plt.tick_params(direction='in', right=True, labelsize=15)
plt.axvline(0.35, color='tab:red', linestyle='--', linewidth=1.5) 
plt.title("Fragility Curves", fontsize=15)
plt.xlim(0, 2)
plt.ylim(0, 1)
plt.grid(True, linewidth=0.7, alpha=0.7)
plt.legend(fontsize=15)

plt.tight_layout()
plt.show()