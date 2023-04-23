import math

s =  '0 1 1 1 1 1 1 1 0 0 0 1 1 0 0 1 0 0 1 0 0 0 0 0 1 0 1 1 0 1 1 1 0 1 1 0 0 1 0 0 0 1 1 0 0 1 1 1 0 1 1 0 0 0 1 0 1 1 0 1 1 1 1 0 0 0 0 0 1 0 0 0 1 0 0 1 1 1 0 0 0 0 1 1 0 0 1 1 1 0 1 1 0 0 0 0 0 0 0 1 1 0 0 1 1 0 1 1 0 0 1 0 0 1 0 1 1 1 0 0 0 0 1 1 0 1 1 0'
lst  =s.split(' ')
for i in range(len(lst)):
    lst[i] = int(lst[i])
    if lst[i] == 0:
        lst[i] = -1
print(lst) 

summ1 = sum(lst)
summ2 = -(1/math.sqrt(128))* summ1
P = math.erfc(summ2/math.sqrt(2))

print(P)
#0.5958830905651779 > 0.01