import numpy as np

def fourPtCenteredDiff(x,y):
    """This function takes the four point center difference by looking at the
    four points closest to the differentiated point and keeps the higher order
    terms from the Taylor expansion to define a more accurate derivative."""
    dydx = np.zeros(y.shape, float)
    dydx[0] = (y[1] - y[0])/(x[1] - x[0])
    dydx[1] = (y[2] - y[1])/(x[2] - x[1])
    dydx[-2] = (y[-2] - y[-3])/(x[-2] - x[-3])
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    dydx[2:-2] = (y[0:-4] - 8 * y[1:-3] + 8 * y[3:-1] - y[4:])/(12.0 * (x[1] - x[0]))
    return dydx

def twoPtForwardDiff(x,y):
    """This function will take the forward differentiation of the point x of 
    the function y. It looks at the points ahead of it to determine a relatively
    accurate depiction of the derivative of the function y."""
    dydx1 = np.zeros(y.shape,float)
    dydx1[0:-1] = np.diff(y)/np.diff(x)
    dydx1[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    return dydx1

def twoPtCenteredDiff(x,y):
    """This function looks at the points surrounding the points of interest
    and then finds the derivative at that point by calculating the average 
    slope around that particular x-value."""
    dydx2 = np.zeros(y.shape,float)
    dydx2[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2])
    dydx2[0] = (y[1]-y[0])/(x[1]-x[0])
    dydx2[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    return dydx2