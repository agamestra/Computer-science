__author__ = 'Evgeny'
from math import *
marks = list(map(int, input().split()))
summa = 0
i = 0
while True:
    if marks[i] == 2:
        if marks[i+1] == 2:
            i += 1
        else:
            marks.pop(i)
    else:
        i += 1
    if i > len(marks)-2:
        break
print(floor(sum(marks)/len(marks)))