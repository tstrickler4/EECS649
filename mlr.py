import disnames
from getdata import rows

# print(getdata.analysis)
# [print(i + ":", str(j)) for i, j in getdata.analysis.items()]
# test = disnames.consclusters(["Katie", "Jamie", "Ben", "Joe", "Alphonse"])
# [print(i + ":", str(j)) for i, j in test.items()]

states = [i.state for i in rows];
data = disnames.consclusters([i.name for i in rows]);
arr = [i.name for i in rows];
arr2 = [i.year for i in rows];

print(data)
[print(i + ":", str(j)) for i, j in data.items()]

print(arr)
print(arr2)
