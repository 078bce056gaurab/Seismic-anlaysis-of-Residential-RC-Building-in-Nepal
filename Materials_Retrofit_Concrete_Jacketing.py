import openseespy.opensees as ops
import numpy as np

gamma_conc = 2.5e-5       # N/mm^3 (for γ = 25 kN/m^3)
gamma_masonry = 2.0e-5    # N/mm^3 (for γ = 20 kN/m^3)
g = 9.81e3                # mm/s^2

unconfined_concrete_tag = 1     # unconfined concrete for existing cover
confined_concrete_tag = 2       # confined concrete for existing core
steel_tag = 3                   # existing reinforcement

# nominal concrete compressive strength
fc = -20.               # CONCRETE Compressive Strength (+Tension, -Compression)
Ec = 5000 * (-fc)**0.5  # Concrete Elastic Modulus (the term in sqr root in Mpa)
Kfc = 1.20			    # ratio of confined to unconfined concrete strength
Kres = 0.1			    # ratio of residual/ultimate to maximum stress
lambda_u = 0.1          # ratio between unloading slope at $eps2 and initial slope $Ec

# unconfined concrete (U) : compressive stress-strain properties
fc1U = fc               # (todeschini parabolic model), maximum compressive stress
eps1U = -0.002          # strain at maximum compressive stress
fc2U = Kres * fc1U      # ultimate compressive stress
eps2U = -0.02           # strain at ultimate compressive stress

# confined concrete (C) : compressive stress-strain properties
fc1C = Kfc * fc1U           # (mander model), maximum compressive stress
eps1C  = max(eps1U * (1 + 5 * (Kfc - 1)), -0.006)    # strain at maximum compressive stress
fc2C = Kres * fc1C          # ultimate compressive stress
eps2C = 10 * eps1C          # strain at ultimate compressive stress

# tensile stress-strain properties
ftC = -0.1 * fc1C  # tensile strength +tension
ftU = -0.1 * fc1U  # tensile strength +tension
Ets = ftU / 0.002   # tension softening stiffness

# STEEL parameters for Steel02
Fy_steel = 415.     # Yield stress (MPa)
E0_steel = 2.0e5    # Initial modulus (MPa)
Bs = 0.01           # strain-hardening ratio
params_steel = [20,0.925,0.15]             # control the transition from elastic to plastic branches

# uniaxialMaterial('Concrete02', matTag, fpc, epsc0, fpcu, epsU, lambda, ft, Ets)
ops.uniaxialMaterial("Concrete02", unconfined_concrete_tag, fc1U, eps1U, fc2U, eps2U, lambda_u, ftU, Ets)   # unconfined concrete for existing cover
ops.uniaxialMaterial("Concrete02", confined_concrete_tag, fc1C, eps1C, fc2C, eps2C, lambda_u, ftC, Ets)     # confined concrete for existing core
ops.uniaxialMaterial("Steel02", steel_tag, Fy_steel, E0_steel, Bs, *params_steel)                           # reinforcement for the existing

# ------------------------------------------------------------------------------------
# Materials for Retrofit Concrete Jacketing
# ------------------------------------------------------------------------------------

unconfined_concrete_tag_retrofit = 4     # unconfined concrete for retrofit cover
confined_concrete_tag_retrofit = 5       # confined concrete for retrofit core
steel_tag_retrofit = 6                   # reinforcement for the retrofit 

# nominal concrete compressive strength
fc_retrofit = -25.                        # CONCRETE Compressive Strength (+Tension, -Compression)
Ec_retrofit = 5000 * (-fc_retrofit)**0.5  # Concrete Elastic Modulus (the term in sqr root in Mpa)
Kfc_retrofit = 1.20			              # ratio of confined to unconfined concrete strength
Kres_retrofit = 0.1			              # ratio of residual/ultimate to maximum stress
lambda_u_retrofit = 0.1                   # ratio between unloading slope at $eps2 and initial slope $Ec

# unconfined concrete (U) : compressive stress-strain properties
fc1U_retrofit = fc_retrofit               # (todeschini parabolic model), maximum compressive stress
eps1U_retrofit = -0.002                   # strain at maximum compressive stress
fc2U_retrofit = Kres_retrofit * fc1U_retrofit      # ultimate compressive stress
eps2U_retrofit = -0.02                    # strain at ultimate compressive stress

# confined concrete (C) : compressive stress-strain properties
fc1C_retrofit = Kfc_retrofit * fc1U_retrofit           # (mander model), maximum compressive stress
eps1C_retrofit  = max(eps1U_retrofit * (1 + 5 * (Kfc_retrofit - 1)), -0.006)    # strain at maximum compressive stress
fc2C_retrofit = Kres_retrofit * fc1C_retrofit          # ultimate compressive stress
eps2C_retrofit = 10 * eps1C_retrofit                   # strain at ultimate compressive stress

# tensile stress-strain properties
ftC_retrofit = -0.1 * fc1C_retrofit  # tensile strength +tension
ftU_retrofit = -0.1 * fc1U_retrofit  # tensile strength +tension
Ets_retrofit = ftU_retrofit / 0.002   # tension softening stiffness

# uniaxialMaterial('Concrete02', matTag, fpc, epsc0, fpcu, epsU, lambda, ft, Ets)
ops.uniaxialMaterial("Concrete02", unconfined_concrete_tag_retrofit, fc1U_retrofit, eps1U_retrofit, fc2U_retrofit, eps2U_retrofit, lambda_u_retrofit, ftU_retrofit, Ets_retrofit) # unconfined concrete for retrofit cover
ops.uniaxialMaterial("Concrete02", confined_concrete_tag_retrofit, fc1C_retrofit, eps1C_retrofit, fc2C_retrofit, eps2C_retrofit, lambda_u_retrofit, ftC_retrofit, Ets_retrofit) # confined concrete for retrofit core
ops.uniaxialMaterial("Steel02", steel_tag_retrofit, 500., E0_steel, Bs, *params_steel) # reinforcement for the retrofit 