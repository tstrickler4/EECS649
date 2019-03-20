from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
import statsmodels.api as sm

def plotScatter(x, y, title, xlabel, ylabel):
    plt.scatter(x, y, color='red')
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.grid(True)
    plt.show()

#-------------------------------------------- Reading Data --------------------------------------------#

print("Running...")

data = {}

file = open('../KS_new.csv')
rows = file.read().splitlines()
file.close()
genders = []
years = []
lengths = []

for i in range(0, len(rows)):
    col = rows[i].split(',')
    for j in range(0, len(col)):
        if j == 0:
            genders.append(col[j])
        elif j == 1:
            years.append(col[j])
        else:
            lengths.append(col[j])

data['Gender'] = genders
data['Year'] = years
data['Length'] = lengths

df = DataFrame(data,columns=[i for i in data])

#-------------------------------------------- Plotting --------------------------------------------#

#Plot Gender vs Length
plotScatter(df['Gender'], df['Length'], 'Scatter Plot', 'Gender', 'Length')

#Plot Year vs Length
plotScatter(df['Year'], df['Length'], 'Scatter Plot', 'Year', 'Length')

#-------------------------------------------- Multiple Linear Regression --------------------------------------------#
X = df[df.columns.difference(['Length'])] # here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
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
print ('Predicted Name Length Example (gender = 0, year = 2030): \n', regr.predict([newData]))
