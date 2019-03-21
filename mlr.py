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


print("Running...")

data = {}

file = open('KS_new.csv')
rows = file.read().splitlines()
file.close()
genders = []
years = []
lengths = []

for i in range(0, len(rows)):
    col = rows[i].split(',')
    for j in range(0, len(col)):
        if j == 0:
            genders.append(int(col[j]))
        elif j == 1:
            years.append(int(col[j]))
        else:
            lengths.append(int(col[j]))

data['Gender'] = genders
data['Year'] = years
data['Length'] = lengths

df = DataFrame(data,columns=[i for i in data])

#-------------------------------------------- Plotting --------------------------------------------#

#Plot Gender vs Length
plotScatter(df['Gender'], df['Length'], 'Gender vs Length', 'Gender', 'Length')

#Plot Year vs Length
plotScatter(df['Year'], df['Length'], 'Year vs Length', 'Year', 'Length')


#-------------------------------------------- Multiple Linear Regression --------------------------------------------#
X = df[df.columns.difference(['Length'])]
Y = df['Length']
#
# # with sklearn
regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

#-------------------------------------------- Prediction --------------------------------------------#
# prediction with sklearn
newData = [0, 2030]
print ('Predicted Length: \n', regr.predict([newData]))


#-------------------------------------------- Stats Models --------------------------------------------#
# with statsmodels
X = sm.add_constant(X) # adding a constant

model = sm.OLS(Y, X).fit()
predictions = model.predict(X)

print_model = model.summary()
print(print_model)
