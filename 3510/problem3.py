import pint
import numpy as np
u = pint.UnitRegistry()

Q_stream = 25000*u.m**3/u.day
Q_waste = 2000*u.m**3/u.day
Q = Q_stream + Q_waste
A = 30*u.m**2
velocity = Q/A

k_R = .17/u.day
k_2 = .22/u.day
k_3 = .02/u.day
k_r = k_R + k_3

DO_stream = 10*u.mg/u.L
DO_waste = 2*u.mg/u.L
DO_mix = (DO_stream*Q_stream + DO_waste*Q_waste)/Q
print(DO_mix)
D_0 = 10*u.mg/u.L-DO_mix

L_0 = 105.85*u.mg/u.L

L_0_sample = 6*u.mg/u.L/(1-np.exp(-.25*5))
L_0_A = L_0_sample / np.exp(-k_r*12000*u.m/velocity)
print(L_0_A)

BOD_waste = (L_0_A*Q - 0.5*u.mg/u.L*Q_stream)/Q_waste
print(BOD_waste)

C_organic = BOD_waste*30/32/.85
print(C_organic)

x_c = velocity / (k_2 - k_r) * np.log(k_2/k_r*(1-D_0*(k_2-k_r)/(L_0*k_R)))
print(x_c)

D_c = k_R / k_2 * L_0 * np.exp(-k_r * x_c / velocity)
print(D_c)
print(10*u.mg/u.L-D_c)

x_c = velocity / (k_2 - k_r) * np.log(k_2/k_r)
print(x_c)

D_c = 5*u.mg/u.L

L_0 = D_c * k_2 / k_R * np.exp(k_r * x_c / velocity)
print(L_0)

BOD_waste = (L_0*Q - 0.5*u.mg/u.L*Q_stream)/Q_waste
print(BOD_waste)

C_organic_new = BOD_waste *30/32/.85
print(C_organic_new)

print((C_organic - C_organic_new) / C_organic)
