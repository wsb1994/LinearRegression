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
        #formula to use
        f = lambdify(x,formula, 'numpy')
        #derivative of that formula
        fg = lambdify(x,formula.diff(), 'numpy')
        #update runs on theta[0], theta[1] in a row etc.
        for j in range(len(thetas)):
            Sum = 0
            #for each datapoint begin the sum
            for i in range(len(data)):
                X = data[i][0] 
                y = data[i][1]
                g = f(X)
                h = fg(X)
                exponent = X**j
                Sum = (Sum + g - y) * exponent
            #compute the average * the derivative
            Sum = h * Sum/(2*len(data))
            newThetas[j] = thetas[j] - (alpha * Sum)
        #cycle updates
        for i in range(len(thetas)):
            thetas[i] = newThetas[i]

    def MSE(thetas, data):
        Sum = 0
        for i in range(len(data)):
            Sum = Sum + ((thetas[0] + thetas[1] * data[i][0]**1 + thetas[2]*data[i][0]**2  - data[i][1]))**2
        Sum = Sum/(len(data))
        print(Sum)
        return Sum

    x = Symbol('x')
    thetas = [.4, 0.0001,-0.001]
    alpha = 0.000001
    y1 =  thetas[0] + thetas[1] * x**1 + thetas[2]*x**2 
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



    equation = thetas[0] + thetas[1]*x + thetas[2]*x**2
    xes = []

    def f(t, t1, t2, t3):
        return t1 + t2*t + t3*t**2 
    t = np.arange(-100,100,1)
    ft = f(t, thetas[0], thetas[1], thetas[2])
    filename2 = '2nd order-' + filename 
    plt.plot(t, f(t,thetas[0], thetas[1], thetas[2]), '-r', filename2)
    plt.title(filename2)
   
    plt.ylim(-16,16)
    plt.xlim(-16,16)
    
    plt.savefig(filename2 + ".png")
    plt.close()
    f = open(filename2 + ".txt", 'w')
    for i in range(len(thetas)):
        f.write(" weight: " + str(i) + "  =  " + str(thetas[i]) + "\n")
    f.write("MSE =   " + str(MSE(thetas, myData)))
