import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'Times New Roman'

# List of files
files = [
    r"C:\Openseespy\Building_Bare_Kabin\Data\pushover_results_retrofit_X.csv",
    r"C:\Openseespy\Building_Bare_Kabin\Data\pushover_results_Bare_X.csv"
]

fig, ax = plt.subplots(figsize=(8, 6))

for file in files:
    df = pd.read_csv(file)
    label = os.path.basename(file).replace(".csv", "").replace(" Pushover", "")
    label = label.replace("750kL ", "")
    line, = ax.plot(df["Drift (%)"], df["Base Shear (kN)"], label=label, linewidth=1.8)
    line_color = line.get_color()

    # ── find maximum base shear ────────────────────────────────────────────
    idx       = df["Base Shear (kN)"].idxmax()
    max_bs    = df.loc[idx, "Base Shear (kN)"]
    max_drift = df.loc[idx, "Drift (%)"]

    # dot at the peak
    ax.plot(max_drift, max_bs, 'o', markersize=6, color='black', zorder=5)

    # ── vertical solid line from peak down to x-axis ───────────────────────
    ax.plot([max_drift, max_drift], [0, max_bs],
            color=line_color, linestyle='-', linewidth=1.0, alpha=0.85, zorder=3)

    # ── horizontal solid line from peak left to y-axis ─────────────────────
    ax.plot([0, max_drift], [max_bs, max_bs],
            color=line_color, linestyle='-', linewidth=1.0, alpha=0.85, zorder=3)

    # ── Vmax label written ALONG the horizontal line ───────────────────────
    ax.text(max_drift * 0.35, max_bs,
            f"  $V_{{max}}$ = {max_bs:.0f} kN  ",
            ha='center', va='bottom',           # sits just above the line
            fontsize=9, color=line_color, fontweight='bold',
            rotation=0,                         # horizontal — along the line
            bbox=dict(boxstyle='square,pad=0.15', fc='white', ec='none', alpha=0.95),
            zorder=6)

    # ── Drift label written ALONG the vertical line ────────────────────────
    ax.text(max_drift, max_bs * 0.35,
            f"  Drift = {max_drift:.2f}%  ",
            ha='center', va='center',           # centred on the line
            fontsize=9, color=line_color, fontweight='bold',
            rotation=90,                        # vertical — along the line
            bbox=dict(boxstyle='square,pad=0.15', fc='white', ec='none', alpha=0.95),
            zorder=6)

# Performance level vertical lines
performance_levels = [(1.0, "IO"), (2.15, "LS"), (3.5, "CP")]
for drift, label in performance_levels:
    ax.axvline(x=drift, color='brown', linestyle='--', linewidth=1.0)
    ax.text(drift - 0.05, 480, label, ha='right', va='top', fontsize=9, color='black')

ax.set_xlabel("Drift (%)")
ax.set_ylabel("Base Shear (kN)")
ax.set_title("Pushover Curves ")
ax.legend(loc='lower right')
ax.set_xlim(0, 4.2)
ax.set_ylim(0, 2500)
ax.grid(True, axis='y', linewidth=0.7, alpha=0.5)
plt.subplots_adjust(left=0.18, bottom=0.15)
plt.savefig(r"C:\Openseespy\Building_Bare_Kabin\Plots\Pushover Comparison Curves.pdf",
            format='pdf', dpi=300, bbox_inches='tight')

plt.tight_layout()
plt.show()