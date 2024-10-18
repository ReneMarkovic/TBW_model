import scipy.optimize
import numpy as np

def f_power(x,A,B):
    return A*np.power(x,B)

def f_lin(x,A,B):
    return A*x+B

def f_exp(x,A,B):
    return A*np.exp(B*x)

def fit(f,x,y):
    return scipy.optimize.curve_fit(f,x,y)

def ma(dt,w):
    x=[]
    y=[]
    for i in range(0,len(dt)-w):
        x.append(int(i)+int(w/2))
        y.append(np.mean(dt[i:i+w]))
    return [x,y]