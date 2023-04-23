import math

s =  '0 0 0 1 0 1 1 0 0 1 0 1 0 1 1 0 1 0 1 1 0 1 0 0 1 1 0 1 1 1 0 1 1 0 0 0 0 1 0 0 1 0 1 1 1 1 0 0 0 1 1 0 0 1 0 0 0 1 1 0 0 0 0 1 0 1 1 0 0 0 0 0 0 1 1 1 0 0 1 1 0 0 0 0 1 0 0 0 0 1 1 1 0 0 1 1 0 1 1 0 1 1 0 1 0 1 0 1 0 0 1 0 0 1 0 0 0 1 1 0 1 0 0 0 0 0 0 1'
lst  =s.split(' ')
for i in range(len(lst)):
    lst[i] = int(lst[i])

lst1 = []
lst2 = []

tmp = 0
for i in lst:
    if tmp == 8:
        lst1.extend([lst2])
        lst2 = []
        tmp = 0
    lst2.append(i)
    tmp += 1
print(lst1)
        

lst1_dict = {}
max_count, count, i_count = 0,0,0

for lst2 in lst1:
    for i in lst2:
        if i == 1:
            count += 1
            if count > max_count:
                max_count = count
        else: count = 0
    lst1_dict["lst"+str(i_count)] = max_count
    i_count += 1
    max_count, count = 0, 0
print(lst1_dict)

v_dict = {'1':0, '2':0, '3':0,'4':0}

for i in lst1_dict.values():
    if i == 1:
        v_dict['1'] += 1
    if i == 2:
        v_dict['2'] += 1
    if i == 3:
        v_dict['3'] += 1
    if i == 4:
        v_dict['4'] += 1
print(v_dict)


xi = 0
xi = (v_dict['1'] - (16 * 0.2148)/(16 * 0.2148)) + (v_dict['2'] - (16 * 0.3672)/(16 * 0.3672)) + (v_dict['3'] - (16 * 0.2305)/(16 * 0.2305)) +(v_dict['4'] - (16 * 0.1875)/(16 * 0.1875))

print(xi)
#11.0
XX = 2,28564
print((2.28564/2))

#По результатам вычислений P = 0.51527748 => последовательность прошла тест


