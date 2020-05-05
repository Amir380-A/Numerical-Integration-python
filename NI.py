
from __future__ import division
import math


def Numerical_Integration(start, end, number, function):
  sum = 0
  inc = (end - start ) / number
  choice=input("press t for trapezoid or s for simpson")
  if (choice =="s"):
    for i in range(number + 1):
        x = start + (i * inc)
        summ = function(x)
        if (i != 0) and (i != number):
          summ *= 2
        sum += summ

    return sum * ((end - start) / (2 * number))
  
  
  
  else:
       for i in range(number + 1):
           x = start + (i * inc)
           summ = function(x)
           if (i != 0) and (i != number):
              summ *= (2 + (2 * (i % 2)))
           sum += summ
  return ((end - start) / (3 * number)) * sum
  
  
  
  

print(trapezoid(1, 2, 10, lambda x: 1 / x))
