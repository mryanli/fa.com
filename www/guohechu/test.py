#!/usr/bin/python
# -*- coding:UTF-8 -*-
from functools import reduce

a = [1,2,3,4]
b = [1,2,3,4]

fun = lambda x,y:x[0]

print(reduce((lambda x,y:x[0]*x[1] + y[0]*y[1]),zip(a,b)))