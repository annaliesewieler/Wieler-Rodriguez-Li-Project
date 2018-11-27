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

def ddSim2(y, t0, b, a, e, s, d, alpha, w):
    H= y[0]
    P = y[1]
    dHdt = b*H*(1-alpha*H) - w*(H/(d+H))*P
    dPdt = e*w*(H/(d+H))*P - s*P
    return [dHdt, dPdt]
