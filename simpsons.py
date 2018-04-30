import numpy as np
from matplotlib import pyplot as plt



def simpsons(fun,x0,x1,n):
    #first, let's check we got a valid input for n.
    if not(type(n)==int):  
        print 'number of points must be an integer'
        return None
    if n&1==0:
        print 'number of points must be odd in simpsons'
        return None
    x=np.linspace(x0,x1,n)
    dx=x[1]-x[0]
    y=fun(x)  #this calls the function we passed in at the x points
    even_sum=y[2:-1:2].sum() #make sure we don't pick up last point
    odd_sum=y[1::2].sum()
    tot=y[0]+y[-1]+4*odd_sum+2*even_sum
    return dx*tot/3


def simple_int(fun,x0,x1,n):
    x=np.linspace(x0,x1,n)
    dx=x[1]-x[0]
    y=fun(x)
    return dx*y.sum()


n=[11,31,101,301,1001]

nvec=np.asarray(n)
errvec=np.zeros(len(n))
errvec_simple=np.zeros(len(n))
for i in range(len(n)):
    err=simpsons(np.cos,0,np.pi/2,n[i])-1
    print 'Simpsons error on ',n[i],' points is ',err
    errvec[i]=np.abs(err)
    errvec_simple[i]=simple_int(np.cos,0,np.pi/2,n[i])-1

plt.ion()
plt.clf();
plt.plot(nvec,errvec)
ax=plt.gca()
ax.loglog() #here's another way to specify log axes

pp=np.polyfit(np.log(nvec),np.log(errvec),1)
print 'Error goes like number of point to the power ',pp[0]
pred=np.polyval(pp,np.log(nvec))
plt.plot(nvec,np.exp(pred))

plt.plot(nvec,errvec_simple)
pp_simple=np.polyfit(np.log(nvec),np.log(errvec_simple),1)
print 'Error for simple integrator goes like number of point to the power ',pp_simple[0]

plt.legend(['Simpsons Error','Power Law Fit','Simple Integrator Error'])
