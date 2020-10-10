from aguaclara.core.units import u
import aguaclara.core.physchem as pc
import numpy as np

import pandas as pd
oxygen_solubility = pd.read_csv('research_it/Oxygen Solubility.txt', sep='\t')
oxygen_solubility.columns
oxygen_solubility.index

oxygen_solubility['Temperature (degC)']
oxygen_solubility.iloc[:,0]

oxygen_solubility[['Temperature (degC)', 'Solubility (mg/L)']]
oxygen_solubility.iloc[:, 0:2]

oxygen_solubility.loc[5]
oxygen_solubility.iloc[5]

oxygen_solubility.loc[[0, 1, 2, 3, 4]]
oxygen_solubility.iloc[0:5]

oxygen_solubility.loc[4, 'Solubility (mg/L)']
oxygen_solubility.iloc[4, 1]

oxygen_solubility.loc[0:4, ['Temperature (degC)', 'Solubility (mg/L)']]
oxygen_solubility.iloc[0:5, 0:2]

deficit = oxygen_solubility['Solubility (mg/L)'] - oxygen_solubility['Dissolved Concentration (mg/L)']
oxygen_solubility.loc[deficit <= 0, 'Dissolved Concentration (mg/L)']

#######################################################

import pandas as pd
import scipy.stats as stats

df = pd.read_csv('research_it/Oxygen Solubility.txt', sep='\t')
temperature = df['Temperature (degC)']
solubility = df['Solubility (mg/L)']

linreg = stats.linregress(temperature, solubility)
slope, intercept, r_value = linreg[0:3]

print("Slope:", slope)
print("Intercept:", intercept)
print("R-squared:", r_value ** 2)

# Here's a way to graph the regression line with the data:
import matplotlib.pyplot as plt

plt.xlabel('Temperature (degC)')
plt.ylabel('Solubility of O2 (mg/L)')
plt.plot(temperature, solubility, 'o')
plt.plot(temperature, temperature * slope + intercept)
plt.savefig("/Users/HannahSi/Documents/Atom/aguaclara_tutorial/docs/source/research/Images/Data_Analysis/linear_regression.png")

############################################

import numpy as np
import pandas as pd
import scipy.optimize as opt
import matplotlib.pyplot as plt

def exp_function(x, a, b, c):
    return a * np.exp(-b * x) + c

df = pd.read_csv("https://raw.githubusercontent.com/AguaClara/aguaclara_tutorial/research-docs/data/Oxygen%20Solubility.tsv", sep='\t')
temperature = df['Temperature (degC)']
solubility = df['Solubility (mg/L)']

popt, pcov = opt.curve_fit(exp_function, temperature, solubility)
print("a:", popt[0])
print("b:", popt[1])
print("c:", popt[2])
print('f(x) =', round(popt[0], 4), '* e^(-', round(popt[1], 4), '* x) +', round(popt[2], 4))

plt.xlabel('Temperature (degC)')
plt.ylabel('Solubility of O2 (mg/L)')
plt.plot(temperature, solubility, 'o')
plt.plot(temperature, exp_function(temperature, *popt))
plt.savefig("/Users/HannahSi/Documents/Atom/aguaclara_tutorial/docs/source/research/Images/Data_Analysis/nonlinear_regression.png")
############################################

import pandas as pd
import numpy as np
from aguaclara.core.units import u
df = pd.DataFrame(np.array([['apples', 2, 3], [4, 5, 6], ['bananas', 8, 9]]), columns=['a', 'b', 'c'])
df[pd.to_numeric(df['a'], errors='coerce').notnull()]
s = df['a']
s[pd.to_numeric(s, errors='coerce').isnull()]

############################################
import aguaclara as ac
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy.optimize as opt

path = "https://raw.githubusercontent.com/AguaClara/aguaclara_tutorial/master/data/plantita%208-12-2019.tsv"
# df = pd.read_csv(path, sep="\t")
# time = pd.to_numeric(df.iloc[:,0])
# count = pd.to_numeric(df.iloc[:,5]).size

time = ac.column_of_time(path, 3200, end=5000)
turb = ac.column_of_data(path, 3200, column="Turb_settled ()", end=5000)
# plt.plot(time, turb)

linreg = stats.linregress(time, turb)
slope, intercept, r_value = linreg[0:3]

print("Slope:", slope)
print("Y-intercept:", intercept)
print("R-squared:", r_value ** 2)

def quad_function(x, a, b, c):
  return a * x.m **2 + b * x.m + c

def hyperbolic(x, d, h):
    return d / (x.m - h)

popt, pcov = opt.curve_fit(quad_function, time, turb)
a, b, c = popt
print("a:", a)
print("b:", b)
print("c:", c)

popt, pcov = opt.curve_fit(hyperbolic, time, turb)
d, h = popt
print("d:", d)
print("h:", h)
# print("k:", k)

plt.plot(time, turb)
# plt.plot(time, a * time.m ** 2 + b * time.m + c)
plt.plot(time, d / (time.m - h))
# plt.plot(time, slope * time.m + intercept)

ac.iplot_columns(path, [2,3])
ac.plot_columns(path, ["Turb_settled ()", "Turb_filter ()"])

path = "https://raw.githubusercontent.com/AguaClara/Fluoride-Auto/master/Summer%202019/Data%20and%20Graphs/Molecular%20Ratios.csv"
df = pd.read_csv(path)
df.iloc[0]
df["Influent PACl (atoms/L)"]
df.iloc[:,2]

plt.plot(df["Influent Fluoride (mg/L)"].iloc[11:19], df["Effluent Fluoride (mg/L)"].iloc[11:19], "o")
plt.plot(df["Influent Fluoride (mg/L)"].iloc[4:8], df["Effluent Fluoride (mg/L)"].iloc[4:8], "v")
