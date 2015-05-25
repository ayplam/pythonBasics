from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d, Axes3D

import matplotlib.pyplot as plt
import numpy as np


def xyPlot():
    fig1 = plt.figure(1)

    a = np.random.random(5) * 20
    b = np.random.random(5) * 20
    c = np.random.random(5) * 20

    R = np.random.random((5, 10)) * 20
    print R

    # s for square, p for pentagon, -- for dashed line, -. for dash-dot...most of this works similarly to MATLAB

    # plt.plot returns a list, so even if you only have one output, you need to have a comma.
    # Use tuple unpacking with the comma to get the first elemnt of the list.
    lin1, lin2, = plt.plot(a, b, 'ro-', a, c, 'bs-.')
    plt.ylabel('Some random numbers')

    xdata, ydata = lin1.get_data()
    print xdata, ydata

    # Apparently plt.show() pauses the whole thing.

    # Call up another figure and have some subplots
    fig3 = plt.figure(3)
    plt.subplot(2, 2, 1)

    for ind in range(4):
        plt.subplot(2, 2, ind + 1)
        plt.plot(R[0, :], R[ind, :], 'gp--')
    # LOL xkcd plot mode.    
    # plt.xkcd()

    # Change the 3rd subplot
    theta = np.arange(0, 30 * np.pi, 0.02)
    r = np.cos(theta * 7 / 10)

    print "\n Polar plot checking: \n", r

    ax = plt.subplot(2, 2, 3, polar=True)
    ax.set_rmax(2.0)
    ax.plot(theta, r, color='r', linewidth=3)
    ax.grid(True)
    ax.set_title('Random polar plot')

    # setp works just like MATLAB

    plt.figure(1)
    plt.axis([0, 20, 0, 20])

    lin4, = plt.plot(R[1, :], R[2, :], 'cp--')
    # ms for marker size
    plt.setp(lin4, 'ms', 10, 'alpha', 0.4)

    # path = "C:\Users\Adrian Lam\Dropbox\DataIncubator\Python\Tutorials"

    # Find all figure numbers and save!
    # for i in plt.get_fignums():
    #    plt.figure(i)
    #    fname = '\Figure%d.png' % i
    #    fullpath = path+fname
    #    plt.savefig(fullpath,dpi=300,facecolor = 'w')


def drawHistogram():
    mu, sigma = 100, 15
    # normal distribution
    x = mu + sigma * np.random.randn(10000)

    # Histogram of the data
    plt.figure(4)
    n, bins, patches = plt.hist(x, 50, normed=1, facecolor='r', alpha=0.75)
    print "n: \n", n
    print "bins: \n", bins
    print "patches: \n", patches
    print "first patch: \n", patches[0]
    plt.xlabel('Random x label')
    plt.ylabel('Who cares about this label?')
    plt.title('I made a histgram!')

    # Making th estrings raw and using latex (What the "r" is for)
    # The second "\" is there because a "space" is "\ "
    plt.text(50, 0.02, r'$\mu=100,\ \sigma = 15$')
    # Looks like the second "$" stops the "raw" part of things
    # bbox puts a box around the text. Kinda cool. 
    plt.text(140, 0.01, r'$\lambda$ test $\epsilon$', fontsize=15, bbox=dict(facecolor='blue', alpha=0.5))
    plt.grid(True)
    plt.show()


def draw3Dplot():

    fig = plt.figure(facecolor='w')
    ax1 = fig.add_subplot(2, 2, 1, projection='3d')

    # Reduce spacing around subplots
    plt.tight_layout()

    X, Y = np.meshgrid(np.arange(-5, 5, 0.25), np.arange(-5, 5, 0.5))
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)
    surf = ax1.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0.2, alpha=0.5)
    m = cm.ScalarMappable(cmap=cm.jet)
    m.set_array(Z)
    plt.colorbar(m)

    ax1.set_zlim(-1.01, 1.01)



    ax2 = fig.add_subplot(2, 2, 2)
    cs = ax2.contour(X, Y, Z)
    plt.clabel(cs, inline=0.25, fontsize=10)

    # All contours are black now. Dashed lines are negative.
    ax3 = fig.add_subplot(2, 2, 3)
    cs = ax3.contour(X, Y, Z, 6, colors='k')
    plt.clabel(cs, inline=0.25, fontsize=10)

    # Overlay contour with bilinear interpolation on TOP of an image! Woah!
    ax4 = fig.add_subplot(2, 2, 4)
    levels = np.arange(-1, 1, 0.2)
    im = ax4.imshow(Z, interpolation='bilinear', origin='lower', cmap=cm.gray, extent=(-3, 3, -2, 2))
    cs = ax4.contour(Z, levels, origin='lower', linewidths=2, extent=(-3, 3, -2, 2), colormap='hot')

    # Find the zero contour
    zc = abs(cs.cvalues).argmin()
    # Thicken zero contour
    plt.setp(cs.collections[zc], linewidth=6)
    # Label every other level
    plt.clabel(cs, levels[0::2], inline=0.1, fontsize=10)

    # Add a colorbar
    cb = plt.colorbar(cs, orientation='horizontal', shrink=0.8)
    # Set background color of colorbar
    cb.patch.set_facecolor('k')

    # Place the colorbar in a particular location
    l, b, w, h = ax4.get_position().bounds
    ll, bb, ww, hh = cb.ax.get_position().bounds

    print l, b, w, h
    print ll, bb, ww, hh

    ax4.set_position([l - 0.05, b - 0.075, w * 1.25, h * 1.3])
    cb.ax.set_position([ll - 0.05, bb - 0.05, ww * 1.5, hh * 0.8])

    plt.title('Most random contourplot')

    # To see ALL properties    
    # print dir(ax4)

    # Change the figure size
    plt.rcParams['figure.figsize'] = 20, 10

    plt.show()


def closeAll():
    # Close any initially open figures
    for i in plt.get_fignums():
        plt.close(plt.figure(i))


def main():
    print "Time to learn how to plot! \n"

    # Basic x-y plots
    # xyPlot()

    # How to draw a histogram
    # drawHistogram()

    # 3D plots
    draw3Dplot()


if __name__ == "__main__":
    main()
