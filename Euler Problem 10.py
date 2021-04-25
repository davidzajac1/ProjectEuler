import math

list = []
nums = [2 , 4, 5, 6, 8, 0]
for x in range(1, 2000000):
    if int(str(x)[len(str(x))-1]) in nums:
        pass
    else:
        list.append(x)

for x in list:
    if math.sqrt(x).is_integer() == True:
        list.remove(x)

for x in list:
    z = x/3
    if z.is_integer() == True:
        list.remove(x)
        print(x)


print(len(list))
