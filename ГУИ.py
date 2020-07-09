from mpmath import besselj
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
import matplotlib.ticker as ticker
from matplotlib import cm


#finction besselj
f =np.frompyfunc(besselj,2,1)
#значения x
x = np.arange(0, 20.0, 0.1)
#окно
fig = plt.figure(figsize=(12,6))
#сетка
gs = fig.add_gridspec(1, 2)


graph1 = None
ax = None
defualt_value=0.1

#генерируем значения для 3д графика 
def makeData ():
    n = np.arange(0, 5, 0.5)
    x = np.arange(0, 10, 0.5)
    ngrid, xgrid = np.meshgrid(n, x)
    zgrid = f(ngrid, xgrid)
    return ngrid, xgrid, np.single(zgrid)

def redraw2d(v):
    ydata = np.single(f(v,x))
    graph1.set_ydata(ydata)
    ax.set_ylim(min(ydata)-0.1, max(ydata)+0.1)
    ax.set_xlim(min(x), max(x))
    plt.draw()

def draw3d():
    n3d, x3d, z3d = makeData()
    ax1 = fig.add_subplot(gs[0, 1],projection='3d')
    surf = ax1.plot_surface(n3d, x3d, z3d,cmap = cm.jet)
    ax1.invert_xaxis()
    ax1.set_xlabel('v')
    ax1.set_ylabel('X')
    ax1.set_zlabel('Jv')
    box = ax1.get_position()
    box.y0 = box.y0+0.1
    box.y1 = box.y1+0.1
    ax1.set_position(box)

def draw2d():
    ax = fig.add_subplot(gs[0, 0])
    y = f(defualt_value,x)
    graph1, = plt.plot(x,y)
    ax.set_xlabel('X')
    ax.set_ylabel('Jv')
    #двигаем по y
    box = ax.get_position()
    box.y0 = box.y0+0.1
    box.y1 = box.y1+0.1
    ax.set_position(box)
    #масштабируем
    ax.set_xlim(min(x), max(x))
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
    return graph1,ax

def submit(text):
    redraw2d(float(text))


graph1,ax = draw2d()
draw3d()

axbox = plt.axes([0.15, 0.05, 0.1, 0.075])
text_box = TextBox(axbox, 'par v', initial=str(defualt_value))
text_box.on_submit(submit)



plt.show()
