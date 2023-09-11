# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 21:40:08 2023

@author: 820763897
"""

import math


def slopeDegRadius(xx,yy,xc,yc):
    # returns angle in degrees (0 to 360) and radius (xc,yc to optical center)
    dx=xx-xc; dy=yy-yc; 
    r=math.sqrt(dx*dx + dy*dy)
    if dx==0:
        dx=0.001
    s=dy/dx
    ss=int(math.degrees(math.atan(s)))
    if dx<0:
        ss+=180
    elif dx>0 and dy<0:
        ss+=360
    #ss=ss%180
    return(ss,r)

for angle in range(0,360,10):
    y=100*math.sin(math.radians(angle))
    x=100*math.cos(math.radians(angle))
    if x==0:
        x=0.001
    slope=y/x
    atan=int(math.degrees(math.atan(slope)))
    ss,r=slopeDegRadius(x,y,0,0)
    print('angle',angle,'x',int(x),'y',int(y),'slope',round(slope,2),'atan deg',atan,ss)
    
