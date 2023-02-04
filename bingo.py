#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 18:42:04 2023

@author: sk
"""

import random
import matplotlib.pyplot as plt

numsCarton = 15
numeros = 100
personas = 10


info = False

def simula(N):
    cuantos = []
    for _ in range(N):
        saco = [i for i in range(1,numeros+1)]
        cartones = [random.sample(saco,k=numsCarton) for _ in range(personas)]
        i = 0
        bingo = False
        while not bingo:
            i+=1
            num = random.choice(saco)
            if info: print("salio el: ", num, "len de saco: ",len(saco))
            for carton in cartones:
                if num in carton:
                    if info: print(">>>>> salio el ", num, " lo tengo")
                    carton.remove(num)
                if len(carton)==0:
                    if info: print("FIN: ",i)
                    cuantos.append(i)
                    bingo = True
                    break
            saco.remove(num)
    return cuantos

    
N = 1000
k = simula(N)    
plt.hist(k,bins=len(set(k)))



"""
# analitica
import math
def prob(tiradas):
    total = math.comb(100,15)
    p = math.comb(tiradas,15)
    print(p/total)
    return p/total
    
    
probs = [prob(i) for i in range(1,101)]
plt.hist(probs)


puntual = []
for i in range(1,len(probs)):
    puntual.append(probs[i]-probs[i-1])

"""
