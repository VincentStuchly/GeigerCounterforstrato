from matplotlib import pyplot as plt

dev_x = [0,1000,5000,10000,15000,20000,25000,50000]


dev_y = [1225,1112,736,414,195,89,40,1]

plt.plot(dev_x, dev_y, label ='all devs')



plt.xlabel("ages")
plt.ylabel("salray")
plt.title("salary by age")


plt.show()
