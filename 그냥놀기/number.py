f = open(file='text.txt', mode='w',encoding='utf-8')
for i in range(0000,10000):
    f.write("010"+'{0:04d}'.format(i)+"2523"+"\n")