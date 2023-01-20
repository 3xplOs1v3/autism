#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 19:25:46 2023

@author: sk
"""


d = {-1,0,1}

def ops(pos):
    return [ [pos[0]+d1,pos[1]+d2] for d1 in d for d2 in d][-8:]  

def listas(pos,mn):
    todos = []
    m,n=len(mn),len(mn[0])
    x,y = pos
    for di in ops([0,0]):
        posn = pos
        lista = []
        while 0<=posn[0]<m and 0<=posn[1]<n:
            lista.append(mn[posn[0]][posn[1]])
            posn = [posn[0]+di[0], posn[1]+di[1]]
        todos.append(lista)
    todos = [ti for ti in todos if len(ti)>1]
    todos.append([mn[pos[0]][pos[1]]])
    return todos


def sublistas(lista):
    return [lista[i:j] for i in range(len(lista)+1) for j in range(len(lista)+1) if len(lista[i:j])>0]


def todo(mn):
    caminos = []
    for i in range(len(mn)):
        for j in range(len(mn[i])):
            print("DESDE LA POSICION ","[",i,j,"]")
            print(listas([i,j],mn))
            for li in listas([i,j],mn):
                if li not in caminos: caminos.append(li)
            
    print("\n\n",caminos, "\n",len(caminos), " formas")
            



"""
0 1 2
3 4 5
6 7 8 
"""
mn = [[0,1],[2,3]]
#mn = [[0,1,2],[3,4,5],[6,7,8]]
#mn = [[0,1,2,4], [4,5,6,7], [8,9,10,11], [12,13,14,15]]

todo(mn)

"""
DESDE LA POSICION  [ 0 0 ]
[[0, 1], [0, 2], [0, 3], [0]]
DESDE LA POSICION  [ 0 1 ]
[[1, 0], [1, 3], [1, 2], [1]]
DESDE LA POSICION  [ 1 0 ]
[[2, 3], [2, 0], [2, 1], [2]]
DESDE LA POSICION  [ 1 1 ]
[[3, 2], [3, 1], [3, 0], [3]]


 [[0, 1], [0, 2], [0, 3], [0], [1, 0], [1, 3], [1, 2], [1], [2, 3], [2, 0], [2, 1], [2], [3, 2], [3, 1], [3, 0], [3]] 
 16  formas

"""
