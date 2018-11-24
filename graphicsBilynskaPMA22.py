import matplotlib.pyplot as plt
import numpy as np
f=open(r"text1population.txt","r")
population=f.readlines()
for i in range(8):
    population[i]=int(population[i])
f.close()
print("Population=", population)
m=open(r"text2percent.txt","r")
percent=m.readlines()
for i in range(8):
    percent[i]=float(percent[i])
m.close()
print("Percent=", percent)
plt.xlabel('Population, mln')
plt.ylabel('Percent, %')
plt.title("Simple Plot")

k=open(r"text3years.txt","r")
years=k.readlines()
for i in range(8):
    years[i]=int(years[i])
k.close()
print("Years", years)

w=open(r"text4salary.txt","r")
salary=w.readlines()
for i in range(8):
    salary[i]=int(salary[i])
w.close()
print("Salary", salary)

plt.plot(population, percent)#населення Землі відповідно до відсотку використання газу на заправках
plt.show()
plt.xlabel('Population, mln')
plt.ylabel('Years')
plt.title("Planet Population+Years")
plt.scatter(population, years)#населення відповідно до років
plt.show()
#size=2*np.random.randn(8)
#colors=np.random.rand(8)
#plt.scatter(years,salary, s=size, c=colors)
e1=0.1*np.abs(np.random.randn(len(years)))
plt.xlabel('Years, mln')
plt.ylabel('Salary, UA hrn')
plt.title("Years+Salary")
plt.errorbar(years,salary,yerr=e1,fmt='.-')
plt.show()

plt.xlabel('Salary')
plt.title("Salary Histogram")
plt.hist(salary,7)#гістограма по зарплатах
plt.show()