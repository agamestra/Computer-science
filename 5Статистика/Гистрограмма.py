import matplotlib.pyplot as plt
from random import random

data=[]
input = open('/home/student/PycharmProjects/untitled/4Генерация случайных чисел/float_data.txt', 'r')
for i in range(int(1e6)):
    data.append(float(input.readline()))
plt.hist(data, bins=20)
plt.show()