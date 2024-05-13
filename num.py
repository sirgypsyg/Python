import numpy as np

t = np.array([1,2,3])
print(type(t))
print("")

t1 = np.zeros((10,5)) #tablcia wypelniona zerami(majac 2 wartosci to 2 wymiar)
t2 = np.ones(10)      #tablcia wypelniona jedynkami
print(t1)
print("")
print(t2)
print("")

l = np.linspace(0,1,6)    #tworzenie przedziałow (poczatek,koniec,na ile elementow)
print(l)
l2 = np.arange(0,1.2,0.2) #tworzenie przedziałow (poczatek,koniec,na ile elementow)
print(l2)
print("")

lp = [1,2,3,4]
lp*=3                       #utworzenie 3 razy [1,2,3,4]
print(lp)
print("")

x = np.arange(1,5,1)        #przedział 1,2,3,4
print(x)
x *=3                       #pomnożenie każdego elementu *3
print(x)
print("")

x = np.array([i for i in range(11)])  #tablica od 0 do 10
print(x)
print(np.sin(x))                    #obliczanie sinusa z radianu w kazdym elemencie
print(np.sin(np.pi/2))
print("")

print(x<5)                  #warunek logiczny tworzy tablice true i false sprawdzajac kazdy element z wyrazeniem
print("")

x = np.array([0,1,2,3,4,5,6,7,8,9])
print(np.logical_and(x>2,x<5))  #logiczny and dla kazdego elementu
print(np.logical_or(x<2,x>5))   #logiczny or dla kazdego elementu
print("")

print(x[x>3])
print(x[np.sin(x)>0.5])



import matplotlib.pyplot as plt
x = [i for i in range(1,11)]
y = list(map(lambda i:i**2,x))
plt.plot(x,y,marker = "D")
plt.show()
plt.scatter(x,y,marker = "D")
plt.show()



import math
x = [i/100 for i in range (0,628)]
y = list(map(lambda i:math.sin(i),x))
plt.scatter(x,y)
plt.show()
print("")
x = np.linspace(-1,1,20)
plt.scatter(x,x**2)
plt.scatter(x,x**3)
plt.legend("123")
plt.show()