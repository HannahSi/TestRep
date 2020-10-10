```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 8, 10]
y1 = [5, 3, 0, -1.2, 3.33, 8]
y2 = [4.5, 3.5, 1, 0, 3, 7.4]

trial1, = plt.plot(x, y, "ro")
trial2, = plt.plot(x, y2, "bs")
plt.xlabel("Time (min)")
plt.ylabel("Displacement (m)")
plt.legend((trial1, trial2), ("Trial 1", "Trial2"))

# plt.savefig("research_it/Example Images/example3.png")
```

```python
import numpy as np
import pandas as pd
import aguaclara.research.procoda_parser as pp
import matplotlib.pyplot as plt

data_raw = pd.read_csv("https://raw.githubusercontent.com/AguaClara/Dissolved-Gas/master/Data/TestingTemperatureDifference_Trial01_20190319.xls", delimiter="\t")
data = pp.remove_notes(data_raw)
time = pd.to_numeric(data["Day fraction since midnight on "])
temp_in = data["Temperature In (C)"]
temp_out = data["Temperature Out (C)"]
temp_in/temp_out
plt.plot(time-time.iloc[0], temp_in)
plt.show()

x = [1, 2, 3, 4, 8, 10]
np.divide(x, 2)
np.array(x)/2

x = [1, 2, 3, 4, 8, 10]
x_array = np.array(x)

y = [5, 3, 0, -1.2, 3.33, 8]
y_array = np.array(y)

average = (x_array + y_array) / 2
np.round(np.log10(average), 3)

```

```python
print(data[‘PumpOutput()’])


import scipy.stats as stats
import pandas as pd
import aguaclara.research.procoda_parser as pp

data_raw = pd.read_csv("C:/users/elena/OneDrive/Desktop/2/DISSOLVEDGASDATA.csv", index_col=0)
data = pp.remove_notes(data_raw)
Time = data.iloc[:,0]
TemperatureIn= data["Temperature In (C)"]

linreg = stats.linregress(Time, TemperatureIn)
slope, intercept, r_value = linreg[0:3]

print("Slope:", slope)
print("Intercept:", intercept)
print("R-squared:", r_value ** 2)

```
