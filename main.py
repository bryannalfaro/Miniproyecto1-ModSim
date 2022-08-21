import math
import matplotlib.pyplot as plt
#Miniproyecto 1
#Modelacion y simulacion

#Autores:
#Bryann Alfaro
#Diego Arredondo

'''
Referencias:
https://pythonguides.com/python-find-max-value-in-a-dictionary/
https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
'''

#Ejercicio 1
#lambda = 7 huracanes / año

#Task 2: Graph of PMF
values = []
pmf = []
for i in range(17):
    values.append(i)
    pmf.append(((7**i)*(math.e)**(-7))/(math.factorial(i)))


plt.plot(values, pmf, marker='o', color='green')
plt.xlabel('Number of hurricanes')
plt.ylabel('Probability')
plt.title('Probability mass function')
plt.show()

#Task 3: Graph of CDF

values = []
cdf = 0
cdf_arr = []

for i in range(17):
    values.append(i)
    cdf += ((7**i)*(math.e)**(-7))/(math.factorial(i))
    cdf = round(cdf, 4)
    cdf_arr.append(cdf)
plt.plot(values, cdf_arr, marker='o', color='red')
plt.xlabel('Number of hurricanes')
plt.ylabel('Probability')
plt.title('Cumulative distribution function')
plt.show()

#Ejercicio 2
#lambda = 2 buses / 30 minutos

#Task 2: Graph of PMF
values = []
pmf = []
dict_pmf = {}
for i in range(101):
    values.append(i)
    pmf.append(((2**i)*(math.e)**(-2))/(math.factorial(i)))
    dict_pmf[i] = pmf[i]

print("Maximo: ",max(dict_pmf, key=dict_pmf.get), "Value:",dict_pmf[max(dict_pmf, key=dict_pmf.get)])
plt.plot(values, pmf, marker='o', color='green')
plt.xlabel('Number of buses')
plt.ylabel('Probability')
plt.title('Probability mass function')
plt.show()


#Ejercicio 5
#Lambda = 2, 1, 0.5
#Task 1: Graph of PMF

lambdas = [2,1,0.5]
colors = ['red','blue','green']
for i in range(3):
    values = []
    pmf = []
    for t in range(15):
        pmf.append(((lambdas[i])*(math.e)**(-lambdas[i]*t))*(((lambdas[i]*t)**(3-1))/(math.factorial(3-1))))
        values.append(t)
    plt.plot(values, pmf, marker='o', color=colors[i])
    plt.xlabel('Time')
    plt.ylabel('Probability')
    plt.title('Probability mass function for lambda' + str(lambdas[i]))

    plt.show()