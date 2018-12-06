# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 13:04:13 2018

@author: Rachel R
"""

# Coding differential equations for group project

import pandas as pd
import numpy as np
import scipy 
import scipy.integrate as spint
import matplotlib.pyplot as plt

# Lotka-Volterra Simulation Function
def ddSim1(y, t0, b, a, e, s):
    H = y[0]
    P = y[1]
    dHdt = b*H - a*P*H
    dPdt = e*a*P*H - s*P
    return [dHdt, dPdt]

# Rosenzweig- MacArthur Model
def ddSim2(y, t0, b, e, s, w, d, alpha):
    H= y[0]
    P = y[1]
    dHdt = b*H*(1-alpha*H) - w*(H/(d+H))*P
    dPdt = e*w*(H/(d+H))*P - s*P
    return [dHdt, dPdt]

# baseline situation

times = np.linspace(0, 50, 501)
y0 = [25, 5]
params = (0.5, 0.02, 0.1, 0.2)
sim=spint.odeint(func=ddSim1,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
simDF.Predator.max()
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

# changing b

times = np.linspace(0, 50, 501)
y0 = [25, 5]
params = (1.5, 0.02, 0.1, 0.2)
sim=spint.odeint(func=ddSim1,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

times = np.linspace(0, 50, 501)
y0 = [25, 5]
params = (0.5/3, 0.02, 0.1, 0.2)
sim=spint.odeint(func=ddSim1,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

# changing a

times = np.linspace(0, 50, 501)
y0 = [25, 5]
params = (0.5, 0.04, 0.1, 0.2)
sim=spint.odeint(func=ddSim1,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

times = np.linspace(0, 50, 501)
y0 = [25, 5]
params = (0.5, 0.01, 0.1, 0.2)
sim=spint.odeint(func=ddSim1,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

# changing e
times = np.linspace(0, 50, 501)
y0 = [25, 5]
params = (0.5, 0.02, 0.3, 0.2)
sim=spint.odeint(func=ddSim1,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

times = np.linspace(0, 50, 501)
y0 = [25, 5]
params = (0.5, 0.02, 0.05, 0.2)
sim=spint.odeint(func=ddSim1,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

# change s
times = np.linspace(0, 50, 501)
y0 = [25, 5]
params = (0.5, 0.02, 0.1, 0.6)
sim=spint.odeint(func=ddSim1,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

times = np.linspace(0, 50, 501)
y0 = [25, 5]
params = (0.5, 0.02, 0.1, 0.1)
sim=spint.odeint(func=ddSim1,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
simDF.Predator.max()
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

###################################################################

# Second Model

# baseline situation

times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.8, 0.07, 0.2, 5, 400, 0.001)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

# change b
times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (2.4, 0.07, 0.2, 5, 400, 0.001)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.2, 0.07, 0.2, 5, 400, 0.001)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

# change e
times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.8, 0.21, 0.2, 5, 400, 0.001)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.8, 0.035, 0.2, 5, 400, 0.001)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

# change s
times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.8, 0.07, 0.6, 5, 400, 0.001)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.8, 0.07, 0.05, 5, 400, 0.001)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

# change w
times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.8, 0.07, 0.2, 15, 400, 0.001)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.8, 0.07, 0.2, 2.5, 400, 0.001)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

# change d
times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.8, 0.07, 0.2, 5, 1200, 0.001)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.8, 0.07, 0.2, 5, 100, 0.001)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

# change alpha
times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.8, 0.07, 0.2, 5, 400, 0.003)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.8, 0.07, 0.2, 5, 400, 0.00025)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()


###################################################################

# Paradox of Enrichment

# K=2000
times = np.linspace(0, 100, 1001)
y0 = [500, 120]
params = (0.8, 0.07, 0.2, 5, 400, 0.00050)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

# K=1333
times = np.linspace(0, 100, 1001)
y0 = [500, 120]
params = (0.8, 0.07, 0.2, 5, 400, 0.00075)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
print simDF.Predator.iloc[-1]
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()

# K=1000
times = np.linspace(0, 100, 1001)
y0 = [500, 120]
params = (0.8, 0.07, 0.2, 5, 400, 0.00100)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()
simDF.Predator.iloc[-1]

# K=800
times = np.linspace(0, 100, 1001)
y0 = [500, 120]
params = (0.8, 0.07, 0.2, 5, 400, 0.00125)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
plt.plot(simDF["t"],simDF["Prey"])
plt.plot(simDF["t"],simDF["Predator"])
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(['Prey', 'Predator'], loc='upper right')
plt.show()
simDF.Predator.iloc[-1]

