###Plotting and Linear Regression for Small Data Sets

Note: this is not finished. It will be updated with tutorial style explanations and code for graphing from spreadsheet data.

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd

# Replace coordinates here with your data. Make as many coordinates as necessary.
data_points = np.array([[1,3],
                       [2,5],
                       [3,7],
                       [4,8],
                       [5,11],
                       [6,14]])

x_points = data_points[:,0]
y_points = data_points[:,1] # You can perform operations on your data here such as np.log10(data_points[:,1])

linreg = stats.linregress(x_points, y_points)
slope, intercept, r_value = linreg[0:3]

start = 0 # Change as desired
end = x_points[-1] # last element plus one; change as desired
plt.plot(x_points, y_points, 'ko')
plt.plot(np.arange(start,end+1, ), np.arange(start,end+1)*slope + intercept, 'k-')
print()
plt.xlabel('X Label')
plt.ylabel('Y label')
plt.title('Title')
plt.minorticks_on()
plt.grid(which = 'major')
plt.grid(which = 'minor')
plt.show()

print("Slope:", slope)
print("Intercept:", intercept)
print("R-squared:", r_value ** 2)
```
