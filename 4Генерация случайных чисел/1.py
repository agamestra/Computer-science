from random import *
output = open('int_data.txt', 'w')
for i in range(int(1e6)):
    print(randint(0, 100), file=output)
output.close()