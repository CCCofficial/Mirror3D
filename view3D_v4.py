# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 16:32:37 2023

@author: 820763897
"""
import numpy as np
import matplotlib.pyplot as plt

trackFile=r'C:\Users\820763897\Documents\AAA_WORK\MirrorCam\Code\3D_Track_Bubble_1.csv'
MAX_OBJ=20; MAX_COL_OBJ=14
FRAME,ID,XC,YC,ZC,XR,YR,RADIUS_C,RADIUS_R,SLOPE_C,SLOPE_R,SLOPE_MUTUAL,PAIRED,SAVE=range(MAX_COL_OBJ) #XC,YC,ZC=real object XR,YR=reflection

fileDir=r'C:\Users\820763897\Documents\AAA_WORK\MirrorCam\Code\Plot\\'

def plotXYZ(selectID,xList,yList,zList,label,frame):
    size=10;
    totalPoints=len(xList)
    maxPoints=500
    minPoints=100
    sections=int(totalPoints/maxPoints)
    for s in range(sections):
        a=s*maxPoints; b=a+maxPoints
        t=range(a,b)
        print(totalPoints,sections,s,a,b)
        if (b-a)>minPoints:
            print('details',t,a,b)
            ax = plt.axes(projection='3d')
            p=ax.scatter(xList[a:b],yList[a:b],zList[a:b],c=t,cmap=plt.cm.get_cmap("Reds"),s=size)
            plt.colorbar(p)
            fileName='ID '+str(selectID)+ ' Range '+ str(a) +'_'+ str(b)
            plt.title(fileName)
            plt.savefig(fileDir+fileName+'.png')
            plt.show()  
    # # plot remainder
    # a=b
    # b=len(xList)-a
    # print('a',a,'b',b,'b-a',b-a)
    # if (b-a)>minPoints:
    #     ax = plt.axes(projection='3d')
    #     t=range(a,b)
    #     #p=ax.scatter(xList[b:],yList[b:],zList[b:],c=t,cmap=plt.cm.get_cmap("inferno"),s=size)
    #     p=ax.scatter(xList[a:b],yList[a:b],zList[a:b],c=t,cmap=plt.cm.get_cmap("inferno"),s=size)
    #     plt.title('ID '+str(selectID)+ ' Range '+ str(a) +' '+ str(b))
    #     #p=ax.scatter(xList[b:],yList[b:],zList[b:],cmap=plt.cm.get_cmap("inferno"),s=size)
    #     plt.colorbar(p)
    #     plt.show()  
            
    return      

def plotXYZ2(selectID,xList,yList,zList,label,frame):
    size=10;
    totalPoints=len(xList)
    t=range(totalPoints)
    print(totalPoints,t)
    ax = plt.axes(projection='3d')
    p=ax.scatter(xList,yList,zList,c=t,cmap=plt.cm.get_cmap("inferno"),s=size)
    plt.colorbar(p)
    plt.show()  
    return    

data=np.loadtxt(trackFile,delimiter=',',skiprows=1,dtype='int')
maxID=max(data[:,ID])

for selectID in range(maxID):
    xList=[]; yList=[]; zList=[]; label=[]; frame=[] # for xyz plotting
    for i in range(len(data)):
        if data[i,ID]==selectID:
            xList.append(data[i,XC])
            yList.append(data[i,YC])
            zList.append(data[i,ZC])
            label.append(data[i,ID])
            frame.append(data[i,FRAME])
    print('plot',selectID,'points',len(xList))
    plotXYZ(selectID,xList,yList,zList,label,frame)

    