from aguaclara.research.procoda_parser import *
import matplotlib.pyplot as plt

path = '/Users/HannahSi/Documents/Atom/aguaclara/tests/research/data/'

# data = get_data_by_state(path=path, dates=['6-19-2013', '6-20-2013'], state=1, column=1)
data = get_data_by_state(path=path, dates='6-19-2013', state=1, column=1)

for i in data:
    plt.plot(i[:,0]-i[0,0], i[:,1])
plt.show()
