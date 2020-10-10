import aguaclara as ac
# from aguaclara.core.units import u
import pandas as pd

path = "/Users/HannahSi/Documents/Atom/aguaclara/tests/research/data/"
data1 = pd.read_csv(path + "datalog_6-19-2013.xls", delimiter='\t')
data2 = pd.read_csv(path + "datalog_6-20-2013.xls", delimiter='\t')
state1 = pd.read_csv(path + "statelog_6-19-2013.xls", delimiter='\t')
state2 = pd.read_csv(path + "statelog_6-20-2013.xls", delimiter='\t')

# # read_state(dates, state, column, units='', path='', extension='.tsv')

# day 1

start_times1 = state1[state1[" State ID"] == 1].iloc[:,0]
bools = list(state1[" State ID"] == 1)
bools.insert(0, False)
end_times1 = state1[bools[0:-1]].iloc[:,0]

start_indexes1 = []
for t in start_times1:
    start_indexes1.append((data1.iloc[:,0] > t).idxmax())

end_indexes1 = []
for t in end_times1:
    end_indexes1.append((data1.iloc[:,0] > t).idxmax())

num_entries = []
for i in range(len(start_indexes1)):
    s = start_indexes1[i]
    e = end_indexes1[i]-1
    num_entries.append(e - s + 1)
    print(str(s) + ":" + str(e))

print("Entries in day 1:", num_entries)

# day 2

start_times2 = state2[state2[" State ID"] == 1].iloc[:,0]
bools = list(state2[" State ID"] == 1)
bools.insert(0, False)
end_times2 = state2[bools[0:-1]].iloc[:,0]

start_indexes2 = []
for t in start_times2:
    start_indexes2.append((data2.iloc[:,0] > t).idxmax())

end_indexes2 = []
for t in end_times2:
    end_indexes2.append((data2.iloc[:,0] > t).idxmax())

num_entries = []
for i in range(len(start_indexes2)):
    s = start_indexes2[i]
    e = end_indexes2[i]-1
    num_entries.append(e - s + 1)
    print(str(s) + ":" + str(e))

print("Entries in day 2:", num_entries)
print()
