import disnames
from getdata import rows

# print(getdata.analysis)
# [print(i + ":", str(j)) for i, j in getdata.analysis.items()]
# test = disnames.consclusters(["Katie", "Jamie", "Ben", "Joe", "Alphonse"])
# [print(i + ":", str(j)) for i, j in test.items()]


nameclusters = disnames.consclusters([i.name for i in rows])
names = [i.name for i in rows]
years = [i.year for i in rows]
genders = [i.gender for i in rows]
states = [i.state for i in rows]
occurrences = [i.number for i in rows]

[print(i + ":", str(j)) for i, j in nameclusters.items()]
print(names)
print(years)
print(genders)
print(states)
print(occurrences)
