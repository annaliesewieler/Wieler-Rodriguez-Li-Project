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
from plotnine import *

def ddSim1(y, t0, b, a, e, s):
    H = y[0]
    P = y[1]
    dHdt = b*H - a*P*H
    dPdt = e*a*P*H - s*P
    return [dHdt, dPdt]

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
ggplot(simDF,aes(x="t",y="Prey"))+ylab("")+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

# changing b

times = np.linspace(0, 50, 501)
y0 = [25, 5]
params = (1.5, 0.02, 0.1, 0.2)
sim=spint.odeint(func=ddSim1,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Prey"))+ylab("")+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

times = np.linspace(0, 50, 501)
y0 = [25, 5]
params = (0.5/3, 0.02, 0.1, 0.2)
sim=spint.odeint(func=ddSim1,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Prey"))+ylab("")+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

# changing a

times = np.linspace(0, 50, 501)
y0 = [25, 5]
params = (0.5, 0.04, 0.1, 0.2)
sim=spint.odeint(func=ddSim1,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Prey"))+ylab("")+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

times = np.linspace(0, 50, 501)
y0 = [25, 5]
params = (0.5, 0.01, 0.1, 0.2)
sim=spint.odeint(func=ddSim1,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Prey"))+ylab("")+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

# changing e
times = np.linspace(0, 50, 501)
y0 = [25, 5]
params = (0.5, 0.02, 0.3, 0.2)
sim=spint.odeint(func=ddSim1,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Prey"))+ylab("")+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

times = np.linspace(0, 50, 501)
y0 = [25, 5]
params = (0.5, 0.02, 0.05, 0.2)
sim=spint.odeint(func=ddSim1,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Prey"))+ylab("")+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

# change s
times = np.linspace(0, 50, 501)
y0 = [25, 5]
params = (0.5, 0.02, 0.1, 0.6)
sim=spint.odeint(func=ddSim1,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Prey"))+ylab("")+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

times = np.linspace(0, 50, 501)
y0 = [25, 5]
params = (0.5, 0.02, 0.1, 0.1)
sim=spint.odeint(func=ddSim1,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
simDF.Predator.max()
ggplot(simDF,aes(x="t",y="Prey"))+ylab("")+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

###################################################################

# Second Model

# baseline situation

times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.8, 0.07, 0.2, 5, 400, 0.001)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Prey"))+ylab("")+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

# change b
times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (2.4, 0.07, 0.2, 5, 400, 0.001)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Prey"))+ylab("")+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.2, 0.07, 0.2, 5, 400, 0.001)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Prey"))+ylab("")+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

# change e
times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.8, 0.21, 0.2, 5, 400, 0.001)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Prey"))+ylab("")+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.8, 0.035, 0.2, 5, 400, 0.001)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Prey"))+ylab("")+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

# change s
times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.8, 0.07, 0.6, 5, 400, 0.001)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Prey"))+ylab("")+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.8, 0.07, 0.05, 5, 400, 0.001)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Prey"))+ylab("")+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

# change w
times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.8, 0.07, 0.2, 15, 400, 0.001)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Prey"))+ylab("")+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.8, 0.07, 0.2, 2.5, 400, 0.001)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Prey"))+ylab("")+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

# change d
times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.8, 0.07, 0.2, 5, 1200, 0.001)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Prey"))+ylab("")+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.8, 0.07, 0.2, 5, 100, 0.001)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Prey"))+ylab("")+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

# change alpha
times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.8, 0.07, 0.2, 5, 400, 0.003)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Prey"))+ylab("")+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

times = np.linspace(0, 50, 501)
y0 = [500, 120]
params = (0.8, 0.07, 0.2, 5, 400, 0.00025)
sim=spint.odeint(func=ddSim2,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"Prey":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Prey"))+ylab("")+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()
