import csv
import os

# Define CSV file path
csv_file = f"C:\Openseespy\Building_Bare_Kabin\Data\\results_bare.csv"

# Check if file exists, if not create it with headers
file_exists = os.path.isfile(csv_file)

# --------------------------------------------------------------
# Ground Motion
# --------------------------------------------------------------

GM_RSN = 5676

pga = 0.2

original_pga_data = {
    5676: 0.36297,
    5259: 0.34798,
    4199: 0.29655,
    3282: 0.32222,
    2510: 0.33066,
    2476: 0.36627,
    334:  0.28209
}

original_pga = original_pga_data[GM_RSN]
factor = (pga * 9810) / original_pga # mm/s2 see the calculation in sheets Final Models Output Data          

direction = 1    # 1, 2 in X and Y Direction respectively

print("=====================================================")
if direction == 1:
    print("Time History Analysis in X Direction...")
elif direction == 2:
    print("Time History Analysis in Y Direction...")
else:
    print("ERROR Direction")

GM_input_file = f"C:\Openseespy\Building_Bare_Kabin\GM\D\RSN_{GM_RSN}.txt"

load_factors = []

# Read and parse the file
with open(GM_input_file, "r") as f:
    lines = f.readlines()

# Extract time step from the line containing "Time Step"
for line in lines:
    if "Time Step" in line:
        dt = float(line.strip().split(":")[1].split()[0])
        break

# Skip lines until you reach the actual data
data_start_index = next(i for i, line in enumerate(lines) if "Time(sec)" in line) + 1

# Read acceleration values
for line in lines[data_start_index:]:
    if line.strip():  # skip empty lines
        parts = line.strip().split()
        if len(parts) >= 2:
            acc = float(parts[1])
            load_factors.append(acc)

tFinal = dt * len(load_factors) # Final time
print(f"RSN: {GM_RSN}, PGA: {pga}, g: {factor}, dt: {dt}, tFinal: {tFinal:.7f}, nPts: {len(load_factors)}")

# --------------------------------------------------------------
# Model
# --------------------------------------------------------------

from Gravity_Analysis import *
print("Gravity Analysis Done.") 

def EigenValues(nModes):
    lambdas = ops.eigen(nModes)  # returns a list of eigenvalues

    omega = []
    frequencies = []
    periods = []

    for lam in lambdas:
        sqrt_lam = lam ** 0.5
        omega.append(sqrt_lam)
        frequencies.append(sqrt_lam / (2 * np.pi))
        periods.append(round(((2 * np.pi) / sqrt_lam),5))
    
    return periods

# --------------------------------------------------------------
# RAYLEIGH damping (D = αM*M + βKcurr*Kcurrent + βKcomm*KlastCommit + βKinit*Kinitial)
# --------------------------------------------------------------
 
xDamp = 0.05  # damping ratio

# damping contribution switches
MpropSwitch = 1.0
KcurrSwitch = 0.0
KcommSwitch = 1.0
KinitSwitch = 0.0

nEigenI = 1  # mode i
nEigenJ = 3  # mode j

# eigenvalue analysis
lambdaN = ops.eigen(nEigenJ)
lambdaI = lambdaN[nEigenI - 1]
lambdaJ = lambdaN[nEigenJ - 1]

# natural frequencies
omegaI = lambdaI ** 0.5
omegaJ = lambdaJ ** 0.5

# Rayleigh damping coefficients
alphaM = MpropSwitch * xDamp * (2 * omegaI * omegaJ) / (omegaI + omegaJ)
betaKcurr = KcurrSwitch * 2.0 * xDamp / (omegaI + omegaJ)
betaKcomm = KcommSwitch * 2.0 * xDamp / (omegaI + omegaJ)
betaKinit = KinitSwitch * 2.0 * xDamp / (omegaI + omegaJ)

# --------------------------------------------------------------
# Analysis by floor
# --------------------------------------------------------------

ops.wipeAnalysis()

ops.rayleigh(alphaM, betaKcurr, betaKinit, betaKcomm)       # apply Rayleigh damping

ops.timeSeries('Path', 200, '-dt', dt, '-values', *load_factors, '-factor', factor)   # tag = 200
ops.pattern('UniformExcitation',  200,   direction,  '-accel', 200) 

ops.constraints('Transformation')
# ops.test('NormDispIncr', 1.0e-6, 50)
ops.test('EnergyIncr', 5.0e-4,  50 )
ops.algorithm('Newton')
ops.numberer('RCM')
ops.system('BandGen')
ops.integrator('Newmark',  0.5,  0.25 )
ops.analysis('Transient')

# Transient Analysis -----------------------------------------------------
# tFinal = nPts * dt
tCurrent = ops.getTime()
ok = 0

control_node = 5     # node where displacement is read (Master Node of top floor)
NBayZ = 4
bay_width_Z = 2150
nodes_for_IDR = [101, 201, 301, 401, 501]

time = []
baseshear = []
control_node_disp = []
drifts_all_floors = [[] for _ in range(NBayZ)]        # One list per floor

while ok == 0 and tCurrent < tFinal: 
    ok = ops.analyze(1, dt)

    if ok != 0:
        print("regular newton failed ... trying ModifiedNewton...")
        ops.test('NormDispIncr', 5.0e-4,  100, 0)
        ops.algorithm('ModifiedNewton')
        ok = ops.analyze( 1, 0.0005)
        if ok == 0:
            # print("ModifiedNewton worked .. back to regular newton")
            ops.test('EnergyIncr', 5.0e-4,  50 )
            ops.algorithm('Newton')
        else:
            # print("ModifiedNewton failed ... trying Broyden...")
            ops.algorithm('Broyden')
            ok = ops.analyze( 1, .0001)
        if ok == 0:
            # print("Broyden worked .. back to regular newton")
            ops.algorithm('Newton')
        else:
            # print("Broyden failed ... trying NewtonLineSearch...")
            ops.algorithm('NewtonLineSearch')
            ok = ops.analyze( 1, .0001)
        if ok == 0:
            # print("NewtonLineSearch worked .. back to regular newton")
            ops.algorithm('Newton')
        else:
            # print("NewtonLineSearch failed ... trying KrylovNewton...")
            ops.algorithm('KrylovNewton')
            ok = ops.analyze( 1, .0001)
        if ok == 0:
            # print("KrylovNewton worked .. back to regular newton")
            ops.algorithm('Newton')
        else:
            print('Analysis Not Successful..')

    tCurrent = ops.getTime()
    time.append(tCurrent)
    ops.reactions()
    basereac = sum(ops.nodeReaction(n, direction) for n in floor_1_nodes)
    baseshear.append(basereac / 1000)
    control_node_disp.append(ops.nodeDisp(control_node, direction))

    for temp_floor in range(NBayZ):
        base_node = nodes_for_IDR[temp_floor]   
        top_node = nodes_for_IDR[temp_floor + 1]    

        base_disp = ops.nodeDisp(base_node, direction)
        top_disp = ops.nodeDisp(top_node, direction)

        drift = abs(top_disp - base_disp) / bay_width_Z
        drifts_all_floors[temp_floor].append(drift)

# Eigenvalue analysis after earthquake -----------------------------------------------------
Final_TimePeriods = EigenValues(3)
print("Final Time Periods: ", [f"{p:.10f}" for p in Final_TimePeriods])

# Maximum Induced Base Shear -----------------------------------------------------
max_base_shear = max(np.abs(baseshear))
print(f"Maximum Induced Base Shear = {max_base_shear:.4f} kN")

max_control_node_disp = max(np.abs(control_node_disp))
print(f"Maximum Top Displacement = {max_control_node_disp:.4f} mm")

MIDRs = [max(drifts) for drifts in drifts_all_floors]

MIDR_1st_floor = MIDRs[0]
MIDR_2nd_floor = MIDRs[1]
MIDR_3rd_floor = MIDRs[2]
MIDR_4th_floor = MIDRs[3]


for i in range(NBayZ):
    print(f'MIDR for Floor {i+1} = {MIDRs[i] * 100:.4f} %')

MIDRall = max(MIDRs)
print(f'MIDR ALL = {MIDRall * 100:.4f} %')

# Open file in append mode
with open(csv_file, 'a', newline='') as f:
    writer = csv.writer(f)
    
    # Write header if file doesn't exist
    if not file_exists:
        writer.writerow(['RSN', 'PGA (g)', 'MIDR 1st Floor (%)', 'MIDR 2nd Floor (%)', 'MIDR 3rd Floor (%)', 'MIDR 4th Floor (%)', 'MIDR ALL (%)'])
    
    # Append the current run's data
    writer.writerow([GM_RSN, pga, f"{MIDR_1st_floor * 100:.5f}", f"{MIDR_2nd_floor * 100:.5f}", f"{MIDR_3rd_floor * 100:.5f}", f"{MIDR_4th_floor * 100:.5f}", f"{MIDRall * 100:.5f}"])

ops.loadConst('-time', 0.0)
ops.remove('recorders') 