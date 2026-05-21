import openseespy.opensees as ops
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
rcParams['font.family'] = 'Times New Roman'

ops.wipe()  
from Materials_Retrofit_Steel_Jacketing import * 

# ------------------------------------------------------------
# Testing Materials
# ------------------------------------------------------------

# Steel02 material test clear model using ops.wipe() in case of malfunction

ops.testUniaxialMaterial(steel_tag)

# Define strain history
strain_values_steel = np.concatenate([
    np.linspace(0, 0.01, 100),                   
    np.linspace(0.01, -0.001, 200), 
    np.linspace(-0.001, 0.02, 200),  
    np.linspace(0.02, -0.001, 200),                    
    np.linspace(-0.001, 0.03, 300),                   
    np.linspace(0.03, -0.001, 300),                   
    np.linspace(-0.001, 0.04, 400),                  
    np.linspace(0.04, -0.001, 400),
    np.linspace(-0.001, 0.06, 400)
])

stress_steel = []
strain_steel = []

# Obtain stress values for each strain value
for eps in strain_values_steel:
    ops.setStrain(eps)
    stress = ops.getStress()
    strain = ops.getStrain()
    stress_steel.append(stress)
    strain_steel.append(strain)

# Plotting
plt.figure()
plt.plot(strain_steel, stress_steel)
plt.title('Steel02')
plt.xlabel('Strain')    
plt.ylabel('Stress (MPa)')
plt.tick_params(direction='in', top=True, right=True)
plt.axhline(0, color='black', linewidth=0.8)  # horizontal axis
plt.axvline(0, color='black', linewidth=0.8)  # vertical axis
plt.grid(True, linewidth = 0.7, alpha=0.8)
plt.xlim(-0.01, 0.06)
plt.tight_layout()
plt.show()