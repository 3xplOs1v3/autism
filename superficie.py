#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 01:33:34 2023

@author: sk
"""
import numpy as np
from matplotlib import pyplot as plt


def vecinos(punto):
    x,y = punto
    a = [-1,1,0]
    vecinos = [[x+i1,y+i2] for i1 in a for i2 in a]
    return [vi for vi in vecinos if vi!=punto]

def alturaVecinos(punto,M):
    vecindad = vecinos(punto)
    alturas = []
    for vi in vecindad:
        #print("toy en ", punto)
        if 0<=vi[0]<len(M) and 0<=vi[1]<len(M) and not M[vi[0]][vi[1]]!=M[vi[0]][vi[1]]:
            #print(" vecino: ",vi)
            alturas.append(M[vi[0]][vi[1]])
        #try: 
        #    if M[vi[0]][vi[1]]!=np.nan:
        #        cuantos+=1
        #        alturas.append(M[vi[0]][vi[1]])
        #except: None
    if len(alturas)==0: return 0
    return sum(alturas)/len(alturas)
        

def dameM(n):
    a = np.empty((n,n))
    a[:] = np.nan
    a[0,:] = 1
    a[len(a)-1,:] = 1
    a[:,0] = 1
    a[:,len(a)-1] = 1
    return a



#a = dameM(4)

"""

a = np.array([[ 3,  2,  1,  0],
              [ 3, np.nan, np.nan,  0],
              [ 3, np.nan, np.nan,  0],
              [ 3,  2,  1,  0]])


"""
def escalona(n):
    esc = [n-i-1 for i in range(n)]
    a = np.empty((n,n))
    a[:] = np.nan
    a[0,:] = esc
    a[len(a)-1,:] = esc
    a[:,0] = n-1
    a[:,len(a)-1] = 0
    return a

def escalona2(n):
    esc = [(n-i) for i in range(1,n+1)]
    a = np.empty((2*n,2*n))
    a[:] = np.nan
    a[0,:] = esc+esc[::-1]
    a[len(a)-1,:] = esc+esc[::-1]
    a[:,0] = esc+esc[::-1]
    a[:,len(a)-1] = esc+esc[::-1]
    return a


def escalona4(n):
    esc = [(n-i) for i in range(1,n+1)]
    a = np.empty((4*n,4*n))
    a[:] = np.nan
    aki = esc+esc[::-1]+esc+esc[::-1]
    a[0,:] = aki
    a[len(a)-1,:] = aki
    a[:,0] = aki
    a[:,len(a)-1] = aki
    for i in range(4*n):
        a[i][i] = aki[i]
    for i in range(4*n):
        a[i][-i-1] = aki[i]
    return a
from matplotlib import cm
def itera(M):  
    #ant = M[:]
    X,Y,Z = [], [], []

    for veces in range(len(M)):
        print("iteracion: ",veces)
        print(M)
        #plt.imshow(M, interpolation='nearest')
        #plt.show()
        X,Y,Z = [], [], []
        for i in range(len(M)):
            for j in range(len(M[i])):
                if i == 0 or i == len(M)-1 or j == 0 or j == len(M)-1:
                    None #print(M[i][j])
                else: M[i][j] = round(alturaVecinos([i,j],M),3)
                X.append(i)
                Y.append(j)
                Z.append(M[i][j])
    ax = plt.axes(projection='3d')
    #ax.scatter(X, Y, Z, c=Z, cmap='viridis', linewidth=0.5)
    ax.plot_trisurf(X, Y, Z, cmap='viridis', edgecolor='none')
    #ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

    




    return M


def iteraAle(M):  
    #ant = M[:]
    for veces in range(50*len(M)):
        print("iteracion: ",veces)
        print(M)
        plt.imshow(M, interpolation='nearest')
        plt.show()
        

        elige = [i for i in range(len(M))]
        for _ in range(len(M**2)):
            i, j = np.random.choice(elige),np.random.choice(elige)
            if i == 0 or i == len(M)-1 or j == 0 or j == len(M)-1:
                None #print(M[i][j])
            else: M[i][j] = round(alturaVecinos([i,j],M),3)


    return M
            
itera(escalona4(10))   
       
#iteraAle(escalona4(8))   
   