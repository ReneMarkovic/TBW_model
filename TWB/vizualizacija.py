import matplotlib.pyplot as plt
from TWB import analiza #f_lin,f_power,fit,ma
import numpy as np

def Fig_1(plazovi,S,Sth,START,save):
    freq={}
    for v in plazovi[START::]:
        if v not in freq:
            freq[v]=0
        freq[v]+=1
    

    x=[v for v in freq]
    y=[freq[v] for v in freq]

    fig=plt.figure(figsize=(18,6))
    ax=fig.add_subplot(131)
    ax.text(-0.05,1.05,"A)",transform=ax.transAxes,fontsize=16,fontweight="bold",va="top")
    
    ax.plot(plazovi)
    ax.set_xlim(0,len(plazovi))
    ax.set_ylim(0,max(plazovi))
    ax.set_xlabel("Zaporeden plaz")
    ax.set_ylabel("Velikost plaza") 
    


    ax=fig.add_subplot(132)
    ax.text(-0.05,1.05,"B)",transform=ax.transAxes,fontsize=16,fontweight="bold",va="top")
    ax.scatter(x,y)
    ax.set_ylabel("Pogostost")
    ax.set_xlabel("Velikost plaza")
    ax.set_xscale("log")
    ax.set_yscale("log")


    ax=fig.add_subplot(133)
    ax.text(-0.05,1.05,"C)",transform=ax.transAxes,fontsize=16,fontweight="bold",va="top")
    ax.imshow(S,cmap="jet",vmin=0,vmax=Sth)
    plt.tight_layout()
    if save:
        plt.savefig("FIF_1.jpg",dpi=150)
    plt.show()
    
def Fig_2(dt,plazovi,START,save):
    plt.figure(figsize=(12,6))
    plt.subplot(122)
    plt.plot(dt,label="Podatki")
    for ww in range(5,36,5):
        x,y=analiza.ma(dt,ww)
        plt.plot(x,y,label="Zglajeno %d"%ww)
    plt.legend()
    
    plt.subplot(121)
    
    x1=np.array([i for i in range(0,START)])
    y1=plazovi[0:START]
    print(len(x1),len(y1))
    
    x2=np.array([i for i in range(START,len(plazovi))])
    y2=plazovi[START::]
    print(len(x2),len(y2))
    
    plt.plot(x1,y1,color="red")
    plt.plot(x2,y2,color="green")
    plt.xlim(0,len(plazovi))
    plt.ylim(0,max(plazovi))
    plt.xlabel("Zaporeden plaz")
    plt.ylabel("Velikost plaza")
    
    plt.tight_layout()
    if save:
        plt.savefig("FIF_2.jpg",dpi=150)

    plt.show()
    
def Fig_3(plazovi,START,save):
    freq={}
    for v in plazovi[START::]:
        if v not in freq:
            freq[v]=0
        freq[v]+=1
        

    x=[v for v in freq]
    y=[freq[v] for v in freq]

    popt, pcov = analiza.fit(analiza.f_power,x,y)
    A, B = popt
    perr = pcov[0,1]/np.sqrt(pcov[0,0]*pcov[1,1])#np.sqrt(np.diag(pcov))
    print(pcov[0,1],pcov[0,0],perr)
    
    fig=plt.figure(figsize=(15,5))
    ax=fig.add_subplot(122)
    ax.scatter(x,y)
    ax.set_xscale('log')
    ax.set_yscale('log')

    yy=analiza.f_power(sorted(x),A,B)
    p1,=ax.plot(sorted(x),yy,color='r')
    ax.legend([p1], [r'${D_f} = %1.2f$'%(B)+" "+r'$(r = %.2f)$'%(perr)], loc=1)


    ax=fig.add_subplot(121)
        
    x=np.array([np.log(v) for v in freq])
    y=np.array([np.log(freq[v]) for v in freq])

    popt, pcov = analiza.fit(analiza.f_lin,x,y)
    A, B = popt
    perr = pcov[0,1]/np.sqrt(pcov[0,0]*pcov[1,1])#np.sqrt(np.diag(pcov))
    print(pcov[0,1],pcov[0,0],perr)

    ax.scatter(x,y)
    x=np.array(sorted(x))
    print(A,B)
    yy=analiza.f_lin(x,A,B)
    p1,=ax.plot(sorted(x),yy,color='r')
    ax.legend([p1], [r'${D_f} = %1.2f$'%(A)+" "+r'$(r = %.2f)$'%(perr)], loc=1)
    
    
    
    '''ax=fig.add_subplot(133)

    x=np.array(sorted([v for v in freq]))
    y=np.array([freq[v] for v in x])
    #y=np.log(y)

    popt, pcov = analiza.fit(analiza.f_exp,x,y)
    A, B = popt
    perr = pcov[0,1]/np.sqrt(pcov[0,0]*pcov[1,1])#np.sqrt(np.diag(pcov))
    print(pcov[0,1],pcov[0,0],perr)

    ax.scatter(x,y)
    ax.set_xlim(0,max(x))
    x=np.array(sorted(x))
    print(A,B)
    
    #yy=analiza.f_exp(x,A,B)
    
    p1,=ax.plot(sorted(x),yy,color='r')
    ax.set_xscale("log")
    ax.legend([p1], [r'${D_f} = %1.2f$'%(A)+" "+r'$(r = %.2f)$'%(perr)], loc=1)
    
    
    ymin=sorted(list(set(y)))[1]
    ax.set_xlim(min(x),max(x))
    ax.set_ylim(ymin,max(y))
    
    print(min(x),max(x))
    print(ymin,max(y))'''
    plt.tight_layout()
    if save:
        plt.savefig("FIF_3.jpg",dpi=150)
    plt.show()
