import disnames
import dictionaries
from getdata import rows
from pandas import DataFrame
import matplotlib.pyplot as plt

#-------------------------------------------- Data --------------------------------------------#

nameclusters = disnames.consclusters([i.name for i in rows])
names = [i.name for i in rows]
years = [i.year for i in rows]
genders = [i.gender for i in rows]
for i in (range(0, len(genders))):
    genders[i] = dictionaries.genders[genders[i]]
states = [i.state for i in rows]
# for i in (range(0, len(states))):
#     states[i] = dictionaries.states[states[i]]
occurrences = [i.number for i in rows]

[print(i + ":", str(j)) for i, j in nameclusters.items()]
# print(names)
print(years)
# print(genders)
print(states)
print(occurrences)

# for i in range(1,len(years)):
#     print(type(years[i]))
#
# for i in range(1,len(occurrences)):
#     print(type(occurrences[i]))

plt.scatter(states, occurrences, color='red')
plt.title('Scatter Plot', fontsize=14)
plt.xlabel('States', fontsize=14)
plt.ylabel('Occurrences', fontsize=14)
plt.grid(True)
plt.show()
