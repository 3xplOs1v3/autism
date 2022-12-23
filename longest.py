#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 21:06:19 2022

@author: sk
"""

N = 7

def ceruno(n):
    d = [0,1]
    if n == 0: return [[di] for di in d]
    return [e+[di] for e in ceruno(n-1) for di in d ]


def mensajePermu(m,p):
    res = ''
    for i in range(len(m)):
        if p[i]==1: res+=str(m[i])
    return res
            

def permMen(m):
    res = []
    perms = ceruno(len(m))
    to = [mensajePermu(m,pi) for pi in perms]
    return list(set(to))


def dale(m1,m2):
    inter = []
    t1, t2 = permMen(m1),permMen(m2)
    for ti in t1:
        if ti in t2:
            inter.append(ti)
    return sorted(inter, key=lambda x: len(x), reverse=True)
    
dale("ABCBDABABC","BDCABABCD")