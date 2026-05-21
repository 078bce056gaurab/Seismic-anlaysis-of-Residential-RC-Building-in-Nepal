import numpy as np

def compute_PSA(accel, dt, T1, damping=0.05):
    omega_n = 2 * np.pi / T1  # Natural frequency (rad/s)
    m = 1.0  # Mass (normalized to 1 for PSA calculation)

    # Newmark parameters (average acceleration method)
    beta = 0.25
    gamma = 0.5

    # Initialize displacement, velocity, and acceleration
    u = np.zeros(len(accel))
    v = np.zeros(len(accel))
    a = np.zeros(len(accel))
    a[0] = -accel[0] - 2 * damping * omega_n * v[0] - omega_n**2 * u[0]

    for i in range(1, len(accel)):
        # Predictors
        u_pred = u[i-1] + dt * v[i-1] + (0.5 - beta) * dt**2 * a[i-1]
        v_pred = v[i-1] + (1 - gamma) * dt * a[i-1]

        # Solve for acceleration
        a[i] = (-accel[i] - 2 * damping * omega_n * v_pred - omega_n**2 * u_pred) / (
            1 + 2 * damping * omega_n * gamma * dt + omega_n**2 * beta * dt**2
        )

        # Correctors
        u[i] = u_pred + beta * dt**2 * a[i]
        v[i] = v_pred + gamma * dt * a[i]

    # Absolute acceleration = structural + ground acceleration
    abs_accel = np.abs(a + accel)
    PSA = np.max(abs_accel)
    return PSA

GM_input_file = '"C:\Openseespy\Groups\GM\D\RSN_334.txt"'     
T1 = 0.422  

load_factors = []

with open(GM_input_file, "r") as f:
        lines = f.readlines()

for line in lines:
        if "Time Step" in line:
            dt = float(line.strip().split(":")[1].split()[0])
            break

data_start_index = next(i for i, line in enumerate(lines) if "Time(sec)" in line) + 1

# Read acceleration values
for line in lines[data_start_index:]:
    if line.strip():  # skip empty lines
        parts = line.strip().split()
        if len(parts) >= 2:
            acc = float(parts[1])
            load_factors.append(acc)

tFinal = dt * len(load_factors)
print(f"RSN: , dt: {dt}, tFinal: {tFinal:.7f}, nPts: {len(load_factors)}")

scale_factors = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0] 
raw_accel_array = np.array(load_factors)

print(f"{'Scale Factor':<15} | {'Sa(T1) [g]':<15}")
print("-" * 35)

for scale in scale_factors:
    # Scale the ground motion
    scaled_accel = raw_accel_array * scale
    
    # Calculate Sa for this specific scale
    sa_value = compute_PSA(scaled_accel, dt, T1)
    
    print(f"{scale:<15.2f} | {sa_value:<15.6f}")