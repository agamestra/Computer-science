from random import *
output = open('float_data.txt', 'w')
for i in range(int(1e6)):
    print('%.2f' % (100*random()), file=output)
output.close()