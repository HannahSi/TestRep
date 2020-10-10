import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import numpy as np
from aguaclara.core.units import u

line1, = plt.plot([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
line2, = plt.plot([1, 2, 3, 4, 5], [3, 5, 5, 9, 12])
plt.legend((line1, line2), ("line 1", "line 2"))


plt.plot([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
plt.plot([1, 2], [2, 3])
plt.plot([1, 2, 3, 4, 5], [3, 5, 5, 9, 12])
plt.legend(("line 1", "line 2"))

line3, = plt.plot([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
line1 == line3
type(line3)

line1

fig = plt.figure()
plt.plot([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])

plt.figure(1)
plt.plot([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
plt.figure(2)
plt.plot([1, 2, 3, 4, 5], [3, 5, 5, 9, 12])




from matplotlib.testing.decorators import check_figures_equal

@check_figures_equal()
def test_plot(fig_test, fig_ref):
    fig_test.subplots().plot([1, 3, 5])
    fig_ref.subplots().plot([0, 1, 2], [1, 3, 5])

test_plot(plt.figure(), plt.figure())



t = np.arange(0, 10, 0.1)
x = (t ** 3 - t ** 2 + t) * u.m
v = (3*t**2 - 2*t + 1) * u.m/u.s

fig, ax1 = plt.subplots()
line1, = ax1.plot(t, x, "b")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Displacement (m)")

ax2 = ax1.twinx()
line2, = ax2.plot(t, v, "g")
ax2.set_ylabel("Velocity (m/s)")

plt.legend((line1, line2), ("Displacement", "Velocity"))
plt.savefig("/Users/HannahSi/Documents/Atom/aguaclara_tutorial/docs/source/research/Images/Data_Analysis/two_y_axes.png")

##############################################

import aguaclara.research.procoda_parser as pp

path = '/Users/HannahSi/Documents/Atom/aguaclara/tests/research/data/'

# data = get_data_by_state(path=path, dates=['6-19-2013', '6-20-2013'], state=1, column=1)
data = pp.get_data_by_state(path=path, dates='6-19-2013', state=1, column=1, extension='.xls')

for i in data:
    plt.plot(i[:,0]-i[0,0], i[:,1])
plt.show()

##############################################

path = "https://raw.githubusercontent.com/AguaClara/team_resources/master/" + \
        "Data/datalog%206-14-2018.xls"
start = 1000
end = 3000
time = pp.column_of_time(path, start, end).to(u.hr)
influent = pp.column_of_data(path, start, 3, end, "NTU")
effluent = pp.column_of_data(path, start, 4, end, "NTU")
influent - effluent

##############################################

import aguaclara.research.procoda_parser as pp
import matplotlib.pyplot as plt

path = "https://raw.githubusercontent.com/AguaClara/team_resources/master/" + \
        "Data/datalog%206-14-2018.xls"
pp.plot_columns(path, ['Influent Turbidity (NTU)', 'Effluent Turbidity ()'],
                'Day fraction since midnight on 6/14/2018')
# pp.iplot_columns(path, [3, 4], 0)
plt.xlabel("Time (day)")
plt.ylabel("Turbidity (NTU)")
plt.legend(("Influent", "Effluent"))
plt.savefig("/Users/HannahSi/Documents/Atom/aguaclara_tutorial/docs/source/research/Images/Data_Analysis/plot_columns.png")

pp.iplot_columns(path, 5, 0)



time, influent, effluent = pp.get_data_by_time()
