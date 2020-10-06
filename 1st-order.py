import numpy as np
from sympy import *
import data
from copy import deepcopy
import matplotlib.pyplot as plt
filenames = ["synthetic-1.csv","synthetic-2.csv","synthetic-3.csv"]
for filename in filenames:
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
            Sum = Sum/(2*len(data))
            newThetas[j] = thetas[j] - (alpha * Sum)
        for i in range(len(thetas)):
            thetas[i] = newThetas[i]

    def MSE(thetas, data):
        Sum = 0
        for i in range(len(data)):
            Sum = Sum + ((thetas[0] + thetas[1]*data[i][0]) - data[i][1])**2
        Sum = Sum/len(data)
        print(Sum)
        return Sum

    x = Symbol('x')
    thetas = [.5, 0.00001]
    alpha = 0.0001
    y1 =  thetas[0] * x**0 + thetas[1] * x**1
    yprime = thetas[1]
    #y2 = thetas[2]*x**2 + thetas[1]*x**1 + thetas[0]*x**0
    #y3 = x**3 + x**2 + x**0
    #y4 = x**4 + x**3 + x**2 + x**0
    #y5 = x**7 + x**6 + x**5 + x**4 + x**3 + x**2 + x**1 + x**0

    myData = data.data(filename)
    myData.cast_to_float()

    myData = myData.data
    hypothesis = [0]*len(myData)

    #######################################################################################################
    for i in range(5000):
        updateTheta(thetas, myData, y1, hypothesis, alpha)

    for i in thetas:
        print(i)
    #######################################################################################################

    xes = []
    yes = []
    for i in range(len(myData)):
    	xes.append(myData[i][0])
    	yes.append(myData[i][1])
    	
    plt.plot(xes,yes, 'ro')



    equation = thetas[0] + thetas[1]*x 
    xes = []

    def f(t, t1, t2):
        return t1 + t2*t 
    t = np.arange(-100,100,1)
    ft = f(t, thetas[0], thetas[1])
    filename2 = '1st order-' + filename 
    plt.plot(t, f(t,thetas[0], thetas[1]), '-r', filename2)
    plt.title(filename2)
   
    plt.ylim(-16,16)
    plt.xlim(-16,16)
    
    plt.savefig(filename2 + ".png")
    plt.close()
    f = open(filename2 + ".txt", 'w')
    for i in range(len(thetas)):
        f.write(" weight: " + str(i) + "  =  " + str(thetas[i]) + "\n")
    f.write("MSE =   " + str(MSE(thetas, myData)))
