import math

s =  '0 0 0 1 0 1 1 0 0 1 0 1 0 1 1 0 1 0 1 1 0 1 0 0 1 1 0 1 1 1 0 1 1 0 0 0 0 1 0 0 1 0 1 1 1 1 0 0 0 1 1 0 0 1 0 0 0 1 1 0 0 0 0 1 0 1 1 0 0 0 0 0 0 1 1 1 0 0 1 1 0 0 0 0 1 0 0 0 0 1 1 1 0 0 1 1 0 1 1 0 1 1 0 1 0 1 0 1 0 0 1 0 0 1 0 0 0 1 1 0 1 0 0 0 0 0 0 1'
lst  =s.split(' ')
count0 = 0
count1 = 0
for i in range(len(lst)):
    lst[i] = int(lst[i])
    if lst[i] == 1:
        count1 += 1
    else:
        count0 += 1

pi = count1/128
print(pi)
#0.4765625

#проверка условия 
print((abs(pi-0.5)) < 2/math.sqrt(128))
#True

count = 0
for i in range(len(lst)-1):
    if lst[i] != lst[i+1]: 
        count += 1
print(count)


P = math.erfc((67-2*128*pi*(1-pi))/(2*math.sqrt(2*128)*pi*(1-pi)))
print(P)
#0.47255340621435993 > 0.01 => последовательность случайна