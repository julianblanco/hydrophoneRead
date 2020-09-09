import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

my_data = np.genfromtxt('test3.csv', delimiter=',')
start =18000
end = 20000

numSamples= end -start
fig = plt.figure()
ax = plt.axes()
x = np.linspace(0, numSamples*100,numSamples)

plt.xlabel('time (100microseconds)')
plt.ylabel('noise amplitude')

ax.plot(x, my_data[start:end,0],'r');
ax.plot(x, my_data[start:end,1],'b');
plt.axis([0, numSamples, 0, np.amax(my_data[start:end,1])])
plt.show()