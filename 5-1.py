# -*- coding: utf-8 -*-

import math

for x in range(1000, 10000):
    factor={1};
    for i in range(2,int(math.sqrt (x))+1):
        if x % i == 0:
            factor.add(i)
            factor.add(x//i)
    y = sum(factor)
    factor.clear()
    factor.add(1)
    for j in range(2,int(math.sqrt (y))+1):
        if y % j == 0:
            factor.add(j)
            factor.add(y//j)
    z = sum(factor)
    if z == x:
        print(x,y)
        
    