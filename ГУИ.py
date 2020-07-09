from mpmath import besselj
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
import matplotlib.ticker as ticker
from matplotlib import cm


#finction besselj
f =np.frompyfunc(besselj,2,1)
#генерируем 3д график 
def makeData ():
    n = np.arange(0, 5, 0.5)
    x = np.arange(0, 10, 0.5)
    ngrid, xgrid = np.meshgrid(n, x)
    zgrid = f(ngrid, xgrid)
    return ngrid, xgrid, np.single(zgrid)
n3d, x3d, z3d = makeData()

fig = plt.figure(figsize=(12,6))
gs = fig.add_gridspec(1, 2)
ax1 = fig.add_subplot(gs[0, 1],projection='3d')
ax = fig.add_subplot(gs[0, 0])
surf = ax1.plot_surface(n3d, x3d, z3d,cmap = cm.jet)

ax1.invert_xaxis()
ax1.set_xlabel('v')
ax1.set_ylabel('X')
ax1.set_zlabel('Jv')

ax.set_xlabel('X')
ax.set_ylabel('Jv')

#двигаем по y
box = ax.get_position()
box.y0 = box.y0+0.1
box.y1 = box.y1+0.1
ax.set_position(box)
box = ax1.get_position()
box.y0 = box.y0+0.1
box.y1 = box.y1+0.1
ax1.set_position(box)

#X
x = np.arange(0, 20.0, 0.1)
#x limits
ax.set_xlim(min(x), max(x))


#Начальный текст 
initial_text = "0.1"

#первоначальный график 
y = f(0.1,x)
graph1, = plt.plot(x,y)



#  Сетка
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.grid(which='major',
        color = 'k')
ax.minorticks_on()
ax.grid(which='minor',
        color = 'gray',
        linestyle = ':')
#

def submit(text):
    v = float(text)
    ydata = np.single(f(v,x))
    graph1.set_ydata(ydata)
    plt.autoscale()
    ax.set_ylim(min(ydata)-0.1, max(ydata)+0.1)
    ax.set_xlim(min(x), max(x))
    plt.draw()

axbox = plt.axes([0.1, 0.05, 0.8, 0.075])
text_box = TextBox(axbox, 'par v', initial=initial_text)
text_box.on_submit(submit)

plt.show()
