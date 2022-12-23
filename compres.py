#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 19:13:36 2022

@author: sk
"""
import random
  
random.seed(123)
  
sampleList = [1,2,3,4]
#pesos = (1/2, 1/4, 1/8, 1/8)
pesos = (1/4, 1/4, 1/4, 1/4)
  
randomList = random.choices(sampleList, weights=pesos, k=1500)
  
print(randomList)

d = {1:'0', 2:'10', 3:'110', 4:'111'}
d = {1:'0', 2:'10', 3:'110', 4:'1110': 5'1111'}

#de = {'0':1, '10':2, '110':3, '111':4}

def invD(d):
    res = {}
    for di in d:
        res[d[di]] = di
    return res

#d = {1:'00', 2:'01', 3:'11',4:'10'}
#de = {'00':1, '01':2, '11':3,'10':4}

def toStrin(l):
    res = ''
    for li in l:
        res+=str(li)
    return res


def code(lista,d):
    #print("mensaje: ", str(lista))
    res = ''
    for ri in randomList:
        res+=d[ri]
    #print("codificado: ", res)
    return res

print("mensaje: ",toStrin(randomList),len(toStrin(randomList)))

men = code(randomList,d)
men = str(men)

print("codificado: ",men, len(men))

def decode(mensaje,de):
    i = 0
    res = ''
    cursor = 0
    while i<=len(men)+1:
        if men[cursor:i] in de:
            res+=str(de[men[cursor:i]])
            cursor = i
        i+=1
        
        
    #print("aki:: "+res)
    #print(res)
    return res

print("decodificado: ", decode(men,de))


def creaCodi(simbolos):
    
        
