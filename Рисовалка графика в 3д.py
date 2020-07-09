import pylab
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.ticker as ticker

import numpy
from mpmath import*

def makeData ():
    n = numpy.arange(0, 5, 0.1)
    x = numpy.arange(0, 10, 0.1)
    ngrid, xgrid = numpy.meshgrid(n, x)
    f =numpy.frompyfunc(besselj,2,1)
    zgrid = f(ngrid, xgrid)
    return ngrid, xgrid, numpy.single(zgrid)

n, x, z = makeData()
fig = pylab.figure()
axes = Axes3D(fig)
axes.plot_surface(n,x, z , cmap = cm.jet)
axes.set_xlabel('N')
axes.set_ylabel('X')
axes.set_zlabel('Значение функци')
pylab.show()
