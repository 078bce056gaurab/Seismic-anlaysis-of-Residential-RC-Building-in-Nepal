import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

# ==============================
# USER INPUTS
# ==============================
input_csv = r"C:\Users\Acer\Downloads\DIANA Files\house_VI_data.csv"       # your input file
output_csv = "fragility_output.csv"    # exported fragility data
im_column = "PGA"                   # intensity measure

# ==============================
# 1. READ DATA
# ==============================
df = pd.read_csv(input_csv)

# ==============================
# 2. FUNCTION TO EXTRACT FIRST EXCEEDANCE IM
# ==============================
def get_first_exceedance(df, limit_state):
    """
    Returns array of IM values where limit_state is first exceeded
    """
    exceedance_ims = []

    for rsn, group in df.groupby("RSN"):
        exceeded = group[group[limit_state] == 1]
        if not exceeded.empty:
            exceedance_ims.append(exceeded.iloc[0][im_column])

    return np.array(exceedance_ims)

# Extract exceedance IMs
io_ims = get_first_exceedance(df, "IO")
ls_ims = get_first_exceedance(df, "LS")
cp_ims = get_first_exceedance(df, "CP")

# ==============================
# 3. FIT LOGNORMAL PARAMETERS
# ==============================
def fit_lognormal(im_values):
    log_im = np.log(im_values)
    mu = np.exp(np.mean(log_im))       # median
    beta = np.std(log_im, ddof=1)      # dispersion
    return mu, beta

mu_io, beta_io = fit_lognormal(io_ims)
mu_ls, beta_ls = fit_lognormal(ls_ims)
mu_cp, beta_cp = fit_lognormal(cp_ims)

print("Lognormal Parameters:")
print(f"IO: μ = {mu_io:.3f}, β = {beta_io:.3f}")
print(f"LS: μ = {mu_ls:.3f}, β = {beta_ls:.3f}")
print(f"CP: μ = {mu_cp:.3f}, β = {beta_cp:.3f}")

# ==============================
# 4. GENERATE FRAGILITY CURVES
# ==============================
# im_min = df[im_column].replace(0, np.nan).min()
# im_max = df[im_column].max()


im_min = 0
im_max = 0.8
im_range = np.linspace(im_min, im_max, 500)

def fragility_function(im, mu, beta):
    return norm.cdf((np.log(im) - np.log(mu)) / beta)

poe_io = fragility_function(im_range, mu_io, beta_io)
poe_ls = fragility_function(im_range, mu_ls, beta_ls)
poe_cp = fragility_function(im_range, mu_cp, beta_cp)

# ==============================
# 5. EXPORT FRAGILITY DATA
# ==============================
fragility_df = pd.DataFrame({
    "Sa(T1)": im_range,
    "PoE(IO)": poe_io,
    "PoE(LS)": poe_ls,
    "PoE(CP)": poe_cp
})


fragility_df.to_csv(output_csv, index=False)

print(f"\nFragility data exported to: {output_csv}")

# ==============================
# 6. PLOT FRAGILITY CURVES
# ==============================
# plt.figure(figsize=(8, 6))

plt.figure()

plt.plot(im_range, poe_io, label="IO", linewidth=2)
plt.plot(im_range, poe_ls, label="LS", linewidth=2)
plt.plot(im_range, poe_cp, label="CP", linewidth=2)

plt.xlabel("Sa(T1) (g)")
plt.ylabel("Probability of Exceedance")
plt.title("Fragility Curves")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.ylim(0, 1)

plt.tight_layout()
plt.show()