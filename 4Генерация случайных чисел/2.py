from random import *
output = open('float_data.txt', 'w')
for i in range(int(16)):
    print(100*random(), file=output)
output.close()