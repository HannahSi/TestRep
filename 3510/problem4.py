from numpy import *
import matplotlib.pyplot as plt
import pint
u = pint.UnitRegistry()

DO_waste = 1*u.mg/u.L
Q_waste = .06*u.m**3/u.s
DO_stream = 6*u.mg/u.L
Q_stream = .55*u.m**3/u.s
DO_mix = (DO_waste * Q_waste + DO_stream * Q_stream) / (Q_waste + Q_stream)
D_0 = 10.07*u.mg/u.L - DO_mix

L_waste = 80*u.mg/u.L
L_stream = 10*u.mg/u.L
L_0 = (L_waste * Q_waste + L_stream * Q_stream) / (Q_waste + Q_stream)

t = arange(0, 26, .4)*u.day

k_1 = .15/u.day
v = 0.2*u.m/u.s
plt.plot(t, 10.07*u.mg/u.L-deficit(D_0, k1(k_1, 15), k2(v, 15), L_0, t))
plt.title("Treatment Plant A at Green River")
plt.xlabel("Time (days)")
plt.ylabel("Dissolved Oxygen Level (mg/L)")
x = x_c(v, k1(k_1, 15), k2(v, 15), D_0, L_0).to(u.m)
print("Time traveled:", (x/v).to(u.day))
print("Maximum deficit:", deficitX(D_0, k1(k_1, 15), k2(v, 15), L_0, x, v))
plt.savefig("A Green")

k_1 = .15/u.day
v = 0.3*u.m/u.s
plt.plot(t, 10.07*u.mg/u.L-deficit(D_0, k1(k_1, 15), k2(v, 15), L_0, t))
plt.title("Treatment Plant A at White River")
plt.xlabel("Time (days)")
plt.ylabel("Dissolved Oxygen Level (mg/L)")
x = x_c(v, k1(k_1, 15), k2(v, 15), D_0, L_0).to(u.m)
print("Time traveled:", (x/v).to(u.day))
print("Maximum deficit:", deficitX(D_0, k1(k_1, 15), k2(v, 15), L_0, x, v))
plt.savefig("A White")


k_1 = .11/u.day
v = 0.2*u.m/u.s
plt.plot(t, 10.07*u.mg/u.L-deficit(D_0, k1(k_1, 15), k2(v, 15), L_0, t))
plt.title("Treatment Plant B at Green River")
plt.xlabel("Time (days)")
plt.ylabel("Dissolved Oxygen Level (mg/L)")
x = x_c(v, k1(k_1, 15), k2(v, 15), D_0, L_0).to(u.m)
print("Time traveled:", (x/v).to(u.day))
print("Maximum deficit:", deficitX(D_0, k1(k_1, 15), k2(v, 15), L_0, x, v))
plt.savefig("B Green")


k_1 = .11/u.day
v = 0.3*u.m/u.s
plt.plot(t, 10.07*u.mg/u.L-deficit(D_0, k1(k_1, 15), k2(v, 15), L_0, t))
plt.title("Treatment Plant B at White River")
plt.xlabel("Time (days)")
plt.ylabel("Dissolved Oxygen Level (mg/L)")
x = x_c(v, k1(k_1, 15), k2(v, 15), D_0, L_0).to(u.m)
print("Time traveled:", (x/v).to(u.day))
print("Maximum deficit:", deficitX(D_0, k1(k_1, 15), k2(v, 15), L_0, x, v))
plt.savefig("B White")


def deficit(D_0, k_1, k_2, L_0, t):
    k_r = k_1
    return D_0*exp(-k_2*t)+k_1*L_0/(k_2-k_r)*(exp(-k_r*t)-exp(-k_2*t))

def deficitX(D_0, k_1, k_2, L_0, x, v):
    k_r = k_1
    return D_0*exp(-k_2*x/v)+k_1*L_0/(k_2-k_r)*(exp(-k_r*x/v)-exp(-k_2*x/v))

def k1(k20, T):
    return k20*1.056**(T-20)

def k2(v, T):
    return OConDob(v)*1.024**(T-20)

def OConDob(v):
    D = 7.5*10**-6 * u.m**2/u.hr
    return 24*u.hr/u.day * (D*v)**(1/2) / (3.5*u.m)**(3/2)

def x_c(v, k_1, k_2, D_0, L_0):
    return v / (k_2 - k_1) * np.log(k_2/k_1*(1-D_0*(k_2-k_1)/(L_0*k_1)))
