from getdata import rows
import disnames
import dictionaries

from pandas import DataFrame
import matplotlib.pyplot as plt

from sklearn import linear_model
import statsmodels.api as sm

gendersDict = dictionaries.genders
statesDict = dictionaries.states

def plotScatter(x, y, title, xlabel, ylabel):
    plt.scatter(x, y, color='red')
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.grid(True)
    plt.show()

#-------------------------------------------- Data --------------------------------------------#

#NOTE: Treating 'occurrences' as the dependent variable and everything else as independent variables

data = {}

nameclusters = disnames.consclusters([i.name for i in rows])

names = [i.name for i in rows]
for i in range(0, len(names)):
    names[i] = i;

data['Name'] = names

years = [i.year for i in rows]
data['Year'] = years

genders = [i.gender for i in rows]
for i in (range(0, len(genders))):
    genders[i] = gendersDict[genders[i]]
data['Gender'] = genders

states = [i.state for i in rows]
# for i in (range(0, len(states))):
#     states[i] = statesDict[states[i]]

statecategories = []
for i in (range(0, len(statesDict))):
        statecategories.append([])

for state in states:
    for j in range(0, len(statesDict)):
        if j == statesDict[state]:
            statecategories[j].append(1);
        else:
            statecategories[j].append(0);

i = 0
for state in statesDict:
    data[state] = statecategories[i]
    i = i + 1

occurrences = [i.number for i in rows]
data['Occurrence'] = occurrences

df = DataFrame(data,columns=[i for i in data])


#-------------------------------------------- Printing (for debugging purposes) --------------------------------------------#
# [print(i + ":", str(j)) for i, j in nameclusters.items()]
# print(data)

#-------------------------------------------- Plotting --------------------------------------------#

#Plot Name vs Occurrence
plotScatter(df['Name'], df['Occurrence'], 'Scatter Plot', 'Name', 'Occurrence')

#Plot Year vs Occurrence
plotScatter(df['Year'], df['Occurrence'], 'Scatter Plot', 'Year', 'Occurrence')

#Plot Gender vs Occurrence
plotScatter(df['Gender'], df['Occurrence'], 'Scatter Plot', 'Gender', 'Occurrence')

#Plot Each State vs Occurrence
#i = 0
# for state in statesDict:
#     plotScatter(statecategories[i], occurrences, 'Scatter Plot', state, 'Occurrence')
#     i = i + 1


#-------------------------------------------- Multiple Linear Regression --------------------------------------------#
X = df[df.columns.difference(['Occurrence'])] # here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
Y = df['Occurrence']
#
# # with sklearn
regr = linear_model.Perceptron()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

#-------------------------------------------- Prediction --------------------------------------------#
# prediction with sklearn
newData = [101, 2030, 0]
for i in range(0, len(statesDict)):
    if i == 32:
        newData.append(i)
    else:
        newData.append(0)
print ('Predicted Occurrence: \n', regr.predict([newData]))


#-------------------------------------------- Stats Models --------------------------------------------#
# with statsmodels
X = sm.add_constant(X) # adding a constant

model = sm.OLS(Y, X).fit()
predictions = model.predict(X)

print_model = model.summary()
print(print_model)
