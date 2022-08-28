from cmath import log
import math
import matplotlib.pyplot as plt
import random as random
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

# #Ejercicio 1
# lambda = 7 huracanes / año

#Task 2: Graph of PMF
# values = []
# pmf = []
# for i in range(17):
#     values.append(i)
#     pmf.append(((7**i)*(math.e)**(-7))/(math.factorial(i)))


# plt.plot(values, pmf, marker='o', color='green')
# plt.xlabel('Number of hurricanes')
# plt.ylabel('Probability')
# plt.title('Probability mass function')
# plt.show()

# print("Mass function values: \n")
# for i in range(len(pmf)):
#     print(values[i], pmf[i])

# #Task 3: Graph of CDF

# values = []
# cdf = 0
# cdf_arr = []

# for i in range(17):
#     values.append(i)
#     cdf += ((7**i)*(math.e)**(-7))/(math.factorial(i))
#     cdf = round(cdf, 4)
#     cdf_arr.append(cdf)
# plt.plot(values, cdf_arr, marker='o', color='red')
# plt.xlabel('Number of hurricanes')
# plt.ylabel('Probability')
# plt.title('Cumulative distribution function')
# plt.show()

# print("Cumulative distribution function values: \n")
# for i in range(len(cdf_arr)):
#     print(values[i], cdf_arr[i])

# #Ejercicio 2
# #lambda = 2 buses / 30 minutos

# #Task 2: Graph of PMF
# values = []
# pmf = []
# dict_pmf = {}
# for i in range(101):
#     values.append(i)
#     pmf.append(((2**i)*(math.e)**(-2))/(math.factorial(i)))
#     dict_pmf[i] = pmf[i]

# plt.plot(values, pmf, marker='o', color='green')
# plt.xlabel('Number of buses')
# plt.ylabel('Probability')
# plt.title('Probability mass function')
# plt.show()

# print("Mass function values: \n")
# for i in range(len(pmf)):
#     print(values[i], pmf[i])

# #Ejercicio 3
# #Task 1
# values = []
# icdf = []
# inversecdf = []
# for n in range(1, 11):
#     r = random.random()
#     values.append(n)
#     icdf.append((-1)*((math.log(1-r))/(5)))

# plt.plot(values, icdf, marker='o', color='blue')
# plt.xlabel('Pacientes')
# plt.ylabel('Horas Intermedias')
# plt.title('Inverse CDF')
# plt.show()

# #Task 2
# values = []
# icdf = 0
# cdf_arr = []

# for n in range(1, 11):
#     r = random.random()
#     values.append(n)
#     icdf += (1 - ((math.e)**((-1)*(5*r))))
#     icdf = round(icdf, 4)
#     inversecdf.append(icdf)

# print(inversecdf)

# plt.scatter(values, inversecdf, marker='o', color='blue')
# plt.xlabel('Pacientes')
# plt.ylabel('Probability')
# plt.title('Inverse CDF')
# plt.show()

# #Task 3
# values = []
# icdf = []

# for n in range(1, 501):
#     r = random.random()
#     values.append(n)
#     icdf.append((-1)*((math.log(1-r))/(5)))

# plt.plot(values, icdf, color='blue')
# plt.xlabel('Pacientes')
# plt.ylabel('Horas Intermedias')
# plt.title('Inverse CDF')
# plt.show()

#Ejercicio 4
#Task 2: PMF
values = []
pmf = []
for i in range(101):
    values.append(i)
    pmf.append(((5**i)*(math.e)**(-5))/(math.factorial(i)))


plt.plot(values, pmf, marker='o', color='green')
plt.xlabel('Number of patients')
plt.ylabel('Probability')
plt.title('Probability mass function')
plt.show()

print("Mass function values: \n")
for i in range(len(pmf)):
    print(values[i], pmf[i])

#Graph of CDF

values = []
cdf = 0
cdf_arr = []

for i in range(101):
    values.append(i)
    cdf += ((5**i)*(math.e)**(-5))/(math.factorial(i))
    cdf = round(cdf, 4)
    cdf_arr.append(cdf)
plt.plot(values, cdf_arr, marker='o', color='red')
plt.xlabel('Number of patients')
plt.ylabel('Probability')
plt.title('Cumulative distribution function')
plt.show()

print("Cumulative distribution function values: \n")
for i in range(len(cdf_arr)):
    print(values[i], cdf_arr[i])


#Graph of PMF
values = []
pmf = []
dict_pmf = {}
for i in range(101):
    values.append(i)
    pmf.append(((2**i)*(math.e)**(-2))/(math.factorial(i)))
    dict_pmf[i] = pmf[i]

plt.plot(values, pmf, marker='o', color='green')
plt.xlabel('Number of patients')
plt.ylabel('Probability')
plt.title('Probability mass function')
plt.show()

print("Mass function values: \n")
for i in range(len(pmf)):
    print(values[i], pmf[i])

#Inverse CFD
values = []
icdf = []
inversecdf = []
for n in range(1, 100):
    r = random.random()
    values.append(n)
    icdf.append((-1)*((math.log(1-r))/(5)))

plt.plot(values, icdf, marker='o', color='blue')
plt.xlabel('Pacientes')
plt.ylabel('Horas Intermedias')
plt.title('Inverse CDF')
plt.show()

#Iverse CDF Exponential
values = []
icdf = 0
cdf_arr = []

for n in range(1, 100):
    r = random.random()
    values.append(n)
    icdf += (1 - ((math.e)**((-1)*(5*r))))
    icdf = round(icdf, 4)
    inversecdf.append(icdf)

print(inversecdf)

plt.scatter(values, inversecdf, marker='o', color='blue')
plt.xlabel('Pacientes')
plt.ylabel('Probability')
plt.title('Inverse CDF')
plt.show()


#Ejercicio 5
#Lambda = 2, 1, 0.5
#Task 1: Graph of PMF

# lambdas = [2,1,0.5]
# colors = ['red','blue','green']
# for i in range(3):
#     values = []
#     pmf = []
#     for t in range(15):
#         pmf.append(((lambdas[i])*(math.e)**(-lambdas[i]*t))*(((lambdas[i]*t)**(3-1))/(math.factorial(3-1))))
#         values.append(t)
#     plt.plot(values, pmf, marker='o', color=colors[i])
#     plt.xlabel('Time')
#     plt.ylabel('Probability')
#     plt.title('Probability mass function for lambda' + str(lambdas[i]))

#     plt.show()