import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

mu = 2.340
sigma = .377
average = 11.053
stdev = 3.778

#model = np.random.lognormal(mean= mu, sigma=sigma,size = (13,2000))
model = np.random.normal(average, stdev,size = (15,2000))

test = model.sum(axis=0)
plt.hist(test,density=True)



plt.xlabel('Number of Total Enrolled Students')
plt.ylabel('Probability')
plt.title('Histogram Estimated Total Enrollment')
plt.text(180, .025, r'$ Class\ \mu=11.053,\ \sigma=3.77$')
plt.text(180,.02, 'Total ' + r'$\mu$=' + str(test.mean().round(2)) + ', ' + r'$\sigma$=' + str(test.std().round(2)))
#plt.axis([40, 160, 0, 0.03])
plt.grid(True)
#plt.show()
plt.savefig('Hist.png')





bob = 1