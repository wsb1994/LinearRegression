import numpy as np
from sympy import *
import data
from copy import deepcopy
import matplotlib.pyplot as plt

def updateTheta( thetas, data, formula, hypothesis, alpha):
    x = Symbol('x')
    newThetas = deepcopy(thetas)
    Sum = 0
    f = lambdify(x,formula, 'numpy')

    for j in range(len(thetas)):
        Sum = 0
        for i in range(len(data)):
            x = data[i][0] 
            y = data[i][1]
            g = f(x)
            Sum = (Sum + g - y) * x**j
        Sum = Sum/len(data)
        newThetas[j] = thetas[j] - (alpha * Sum)
    for i in range(len(thetas)):
        thetas[i] = newThetas[i]

def MSE(thetas, data):
    Sum = 0
    for i in range(len(data)):
        Sum = Sum + ((thetas[0] + thetas[1]*data[i][0]) - data[i][1])**2
    Sum = Sum/len(data)
    print(Sum)

x = Symbol('x')
thetas = [10, 10]
alpha = 0.0001
y1 =  thetas[0] * x**0 + thetas[1] * x**1
yprime = thetas[1]
#y2 = thetas[2]*x**2 + thetas[1]*x**1 + thetas[0]*x**0
#y3 = x**3 + x**2 + x**0
#y4 = x**4 + x**3 + x**2 + x**0
#y5 = x**7 + x**6 + x**5 + x**4 + x**3 + x**2 + x**1 + x**0

myData = data.data("synthetic-1.csv")
myData.cast_to_float()

myData = myData.data
hypothesis = [0]*len(myData)

#######################################################################################################
for i in range(1000000):
    updateTheta(thetas, myData, y1, hypothesis, alpha)

for i in thetas:
    print(i)
#######################################################################################################

plt.plot(myData, 'ro')
xes = []
yes = []
for i in range(len(myData)):
    f = lambdify(x,y1, 'numpy')
    xes.append(myData[i][0])
    yes.append(f(myData[i][0]))


Xrange = np.linspace(-5,100,100)
equation = thetas[0] + thetas[1]*Xrange**1

plt.plot(Xrange, equation, '-r', label='y=2x+1')
plt.savefig('plot.png')

MSE(thetas, myData)