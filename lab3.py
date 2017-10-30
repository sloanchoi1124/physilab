from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

def fitfunc(p, x):
    return p[0] * (x ** p[1])
def errfunc(p, x, y):
    return y - fitfunc(p, x)

xdata=np.array([0.0059, 0.0144, 0.0029596, 0.000998, 0.0010814, 0.005, 0.0073, 0.011068])
xdata_adapted=np.array([0.0059, 0.0144, 0.0029596, 0.000998, 0.00010814, 0.005, 0.0073, 0.011068])
ydata=np.array([44.345, 25.425, 57.18, 92.268, 105.66, 44.63, 38.695, 34.551])

N = 5000
xprime = xdata * N

plt.plot(xdata, ydata, 'o', label='raw data')
plt.plot(xdata_adapted, ydata, 'x', markersize=10, label='revised data')
plt.xlabel("mu (kg/m)")
plt.ylabel("C (m/s)")
plt.legend(loc='upper right')
plt.show()

qout,success = optimize.leastsq(errfunc, [3.13, -0.5],
                               args=(xprime, ydata),maxfev=3000)

#print (optimize.leastsq(errfunc, [3.13, -0.5], args=(xprime, ydata), maxfev=3000, full_output=True))
out = qout[:]
out[0] = qout[0] * (N**qout[1])
out[1] = qout[1]
print ("%g*x^%g"%(out[0],out[1]))
print (qout)
print (success)
