import numpy as np



ell = 0.20      # m
d = 0.03        # m
h = 0.01        # m
r = 0.005       # m
wA = 0.02       # m
wB = 0.02       # m
MG = 2.0        # N*m
mu = 0.2        # Coefficient of friction
theta = np.pi / 6  # 30 degrees in radians

# Unit vectors
ihat = np.array([1.0, 0.0, 0.0])
jhat = np.array([0.0, 1.0, 0.0])
khat = np.array([0.0, 0.0, 1.0])

ul = np.cos(theta) * ihat + np.sin(theta) * jhat
un = -np.sin(theta) * ihat + np.cos(theta) * jhat

# Position vectors
rGC = -(r + h) * un + d * ul
rCA = ell * ihat + wA * jhat
rCB = ell * ihat - wB * jhat

rGA = rGC + rCA
rGB = rGC + rCB

rGD = -r * un
rGE = r * un
rCD = -d * ul + h * un
def cross_z(v1, v2):
    return np.cross(v1, v2)[2]

# ==========================================
# 2. CONSTRUCT MATRIX A AND VECTOR b
# A * x = b
# x = [ND, FD, NE, FE, RGx, RGy, Cx, Cy, FA, FB]^T
# ==========================================
A = np.zeros((10, 10))
b = np.zeros(10)

# Eq 0: Whole system Fx = 0 -> RGx = 0
A[0, 4] = 1.0

# Eq 1: Whole system Fy = 0 -> RGy - FA + FB = 0
A[1, 5] = 1.0
A[1, 8] = -1.0
A[1, 9] = 1.0

# Eq 2: Whole system Mg = 0 -> MG + rGA x (-FA jhat) + rGB x (FB jhat) = 0
A[2, 8] = -cross_z(rGA, jhat)
A[2, 9] = cross_z(rGB, jhat)
b[2] = -MG

# Eq 3: Pipe Fx = 0 -> ND*un_x - FD*ul_x - NE*un_x + FE*ul_x + RGx = 0
A[3, 0] = un[0]
A[3, 1] = -ul[0]
A[3, 2] = -un[0]
A[3, 3] = ul[0]
A[3, 4] = 1.0

# Eq 4: Pipe Fy = 0 -> ND*un_y - FD*ul_y - NE*un_y + FE*ul_y + RGy = 0
A[4, 0] = un[1]
A[4, 1] = -ul[1]
A[4, 2] = -un[1]
A[4, 3] = ul[1]
A[4, 5] = 1.0

# Eq 5: Pipe Mg = 0 -> MG + rGD x (ND*un - FD*ul) + rGE x (-NE*un + FE*ul) = 0
A[5, 0] = cross_z(rGD, un)
A[5, 1] = -cross_z(rGD, ul)
A[5, 2] = -cross_z(rGE, un)
A[5, 3] = cross_z(rGE, ul)
b[5] = -MG

# Eq 6: Top piece Fx = 0 -> -ND*un_x + FD*ul_x + Cx = 0
A[6, 0] = -un[0]
A[6, 1] = ul[0]
A[6, 6] = 1.0

# Eq 7: Top piece Fy = 0 -> -ND*un_y + FD*ul_y + Cy - FA = 0
A[7, 0] = -un[1]
A[7, 1] = ul[1]
A[7, 7] = 1.0
A[7, 8] = -1.0

# Eq 8: Top piece Mc = 0 -> rCD x (-ND*un + FD*ul) + rCA x (-FA*jhat) = 0
A[8, 0] = -cross_z(rCD, un)
A[8, 1] = cross_z(rCD, ul)
A[8, 8] = -cross_z(rCA, jhat)


A[9, 0] = -mu
A[9, 1] = 1.0


x = np.linalg.solve(A, b)

var_names = ["ND", "FD", "NE", "FE", "RGx", "RGy", "Cx", "Cy", "FA", "FB"]

print("=" * 45)
print("  PLIERS PROBLEM SOLUTION (NUMPY MATRIX SOLVE)")
print("=" * 45)
for name, val in zip(var_names, x):
    print(f"{name:5s} = {val:10.4f}")

print("-" * 45)
print(f"Friction ratio at D (FD/ND) = {x[1]/x[0]:.4f}")
print(f"Friction ratio at E (FE/NE) = {x[3]/x[2]:.4f}")
print("=" * 45)