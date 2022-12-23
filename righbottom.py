#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 22:29:28 2022

@author: sk
"""

import numpy as np

M,N = 3,3
#0 abajo 1 derecha
def ceruno(n):
    d = [0,1]
    if n == 0: return [[di] for di in d]
    return [e+[di] for e in ceruno(n-1) for di in d ]

 
n = M*N
def caminos():
    caminos = []
    for i in range(max(M,N),n+1):
        [caminos.append(ti) for ti in ceruno(i)]
    return caminos
        
        
def termina(camino):
    x,y = 0,0
    for i in range(len(camino)):
        ci = camino[i]
        if ci==0:
            x+=1
        if ci==1:
            y+=1
        if x == M-1 and y == N-1:
            return camino[:i+1]
    return False
    
def limpia(l):
    res = []
    for li in l:
        if li not in res:
            res.append(li)
    return res
            
def caminosValidos():
    validos = []
    cams = caminos()
    for c in cams:
        posible = termina(c)
        if posible: 
            validos.append(posible)
    return limpia(validos)


def valorK(camino):
    giros = 0
    for i in range(len(camino)-1):
        if camino[i]!=camino[i+1]:
            giros+=1
    return giros

def dale(ka):
    res = []
    todos = caminosValidos()
    for ti in todos:
        if valorK(ti)==ka:
            #print("ti: ", ti, "tiene k=",ka)
            res.append(ti)
    return res

def pintaTraza(camino):
    pasos = [(0,0)]
    x,y = 0,0
    for i in range(len(camino)):
        ci = camino[i]
        if ci==0:
            x+=1
        if ci==1:
            y+=1
        pasos.append((x,y))
        if x == M-1 and y == N-1:
            break
    print(pasos)
    
    
def ejecuta(k):
    #k = 1
    for di in dale(k):
        pintaTraza(di)

