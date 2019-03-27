from pandas import DataFrame
import matplotlib.pyplot as plt

from sklearn import linear_model
import statsmodels.api as sm

def plotScatter(x, y, title, xlabel, ylabel):
    plt.scatter(x, y, color='red')
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.grid(True)
    plt.show()

#-------------------------------------------- Data --------------------------------------------#

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

gendersDict = {'F': 0, 'M': 1}

file = open('MO.txt')
rows = file.read().splitlines()
file.close()

for i in range(0, len(rows)):
    col = rows[i].split(',')
    for j in range(1, 4):
        if j == 1:
            genders.append(gendersDict[col[j]])
        elif j == 2:
            years.append(int(col[j]))
        elif j == 3:
            lengths.append(len(col[j]))

data['Gender'] = genders
data['Year'] = years
data['Length'] = lengths

df2 = DataFrame(data,columns=[i for i in data])


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

for i in range(0, len(genders)):
    gender = genders[i]
    year = years[i]
    testData = [gender, year]
    print('Predicted Length (gender: ',gender, ", year: ", year, "): ", regr.predict([testData]))

#-------------------------------------------- Stats Models --------------------------------------------#
# with statsmodels
X = sm.add_constant(X) # adding a constant

model = sm.OLS(Y, X).fit()
predictions = model.predict(X)

print_model = model.summary()
print(print_model)
