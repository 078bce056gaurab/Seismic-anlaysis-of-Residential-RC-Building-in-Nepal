import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

plt.rcParams['font.family'] = 'Times New Roman'

# Load the dataset
df = pd.read_csv('/Users/niraj/Downloads/Projects/Project_Geo_Lab/Building/IDA Data.csv')

# Unique RSNs (taken from the column with the most data to ensure we catch all)
unique_rsns = df['RSN Concrete Jacketing'].unique()

# Define specific colors and styles for the three scenarios
configs = {
    'Bare': {'rsn': 'RSN Bare', 'pga': 'PGA (g) Bare', 'midr': 'MIDR (%) Bare', 'color': 'tab:blue', 'ls': '-'},
    'Steel Angle': {'rsn': 'RSN Steel Angle', 'pga': 'PGA (g) Steel Angle', 'midr': 'MIDR (%) Steel Angle', 'color': 'tab:orange', 'ls': '-'},
    'Concrete Jacketing': {'rsn': 'RSN Concrete Jacketing', 'pga': 'PGA (g) Concrete Jacketing', 'midr': 'MIDR (%) Concrete Jacketing', 'color': 'tab:green', 'ls': '-'}
}

configs = {
    'Bare': {'rsn': 'RSN Bare', 'pga': 'PGA (g) Bare', 'midr': 'MIDR (%) Bare', 'color': 'tab:blue', 'label': 'Bare'},
    'Steel Angle': {'rsn': 'RSN Steel Angle', 'pga': 'PGA (g) Steel Angle', 'midr': 'MIDR (%) Steel Angle', 'color': 'tab:orange', 'label': 'Steel Angle Retrofit'},
    'Concrete Jacketing': {'rsn': 'RSN Concrete Jacketing', 'pga': 'PGA (g) Concrete Jacketing', 'midr': 'MIDR (%) Concrete Jacketing', 'color': 'tab:green', 'label': 'Concrete Jacket Retrofit'}
}

fig, ax = plt.subplots(figsize=(10, 7))

# 1. Plot individual RSN curves
for name, config in configs.items():
    first = True # Helper to avoid duplicate legend entries
    for rsn in unique_rsns:
        # Filter each case by its own RSN column to handle misaligned rows
        data = df[df[config['rsn']] == rsn][[config['pga'], config['midr']]].dropna().sort_values(by=config['pga'])
        
        if not data.empty:
            ax.plot(data[config['pga']], data[config['midr']], 
                    color=config['color'], alpha=0.8, linewidth=1.2, 
                    label=config['label'] if first else "")
            first = False

# 2. Add Horizontal limit lines and labels (IO, LS, CP)
y_limits = {1: 'IO', 2: 'LS', 4: 'CP'}
for y, text in y_limits.items():
    ax.axhline(y, color='brown', linestyle='--', linewidth=1.2)
    # Place text at the right edge (x=0.99 in axes coords) and at the line height (y)
    ax.text(0.99, y + 0.05, text, transform=ax.get_yaxis_transform(), 
            color='black', fontsize=14, ha='right', va='bottom')

# 3. Add Vertical line (Design PGA or other reference)
ax.axvline(0.35, color='tab:red', linestyle='--', linewidth=1.2)

# Formatting the plot
ax.set_xlabel('PGA (g)', fontsize=17)
ax.set_ylabel('MIDR (%)', fontsize=17)
ax.tick_params(direction='in', top=True, right=True, labelsize=15)
ax.set_title('Incremental Dynamic Analysis (IDA)', fontsize=18)
ax.legend(loc='lower right', fontsize=12)
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)
ax.grid(False)

plt.tight_layout()
plt.show()