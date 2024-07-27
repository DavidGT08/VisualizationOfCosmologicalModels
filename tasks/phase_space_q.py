from pylab import *
import numpy as np

#grid
xvalues , yvalues = np.meshgrid(np.arange(0.001,1,0.01), np.arange(0.001,1,0.01))

# constants
gamma_de = 0
xi_zero = 0.028
beta = 0.2

z = beta * xvalues * yvalues/(xvalues+yvalues)

# diferential equations
xprime = 3*(xvalues - 1) * xvalues* gamma_de - 3*xi_zero*xvalues*yvalues**0.5 - xvalues*(4*xvalues + yvalues - 4) - z 

yprime = 3* gamma_de* xvalues * yvalues - yvalues*(4*xvalues+yvalues-1) - 3*xi_zero*(yvalues-1)*yvalues**0.5  + z

# deceleration parameter
q = 1-(2-1.5*gamma_de)*xvalues-0.5*yvalues-1.5*xi_zero*yvalues**0.5
qprime = 2*xprime-3/2*gamma_de*xprime - 0.5*yprime - 3/4*xi_zero*(yvalues**-0.5)*yprime



# effective EoS
w = 1/3*(1-(4-3*gamma_de)*xvalues-yvalues-3*xi_zero*yvalues**0.5)

# jerk parameter
j = q*(2*q+1)-qprime

def plot_phase_space_q(xvalues, yvalues, xprime, yprime,q):
    stream = streamplot(xvalues, yvalues, xprime, yprime, color=q, cmap='viridis')

    #plt.colorbar(label="Like/Dislike Ratio", orientation="horizontal")
    cbar = plt.colorbar(stream.lines, orientation='horizontal')
    cbar.set_label('Deceleration Parameter (q)')

    show()

plot_phase_space_q(xvalues, yvalues, xprime, yprime,q)

def plot_phase_space_w(xvalues, yvalues, xprime, yprime, w):
    stream = streamplot(xvalues, yvalues, xprime, yprime, color=w, cmap='viridis')

    #plt.colorbar(label="Like/Dislike Ratio", orientation="horizontal")
    cbar = plt.colorbar(stream.lines, orientation='horizontal')
    cbar.set_label('Efective EoS (w)')

    show()

# plot_phase_space_w(xvalues, yvalues, xprime, yprime,w)

def plot_phase_space_j(xvalues, yvalues, xprime, yprime,j):
    stream = streamplot(xvalues, yvalues, xprime, yprime, color=j, cmap='viridis')

    #plt.colorbar(label="Like/Dislike Ratio", orientation="horizontal")
    cbar = plt.colorbar(stream.lines, orientation='horizontal')
    cbar.set_label('Jerk (j)')

    show()

# plot_phase_space_j(xvalues, yvalues, xprime, yprime,j)
