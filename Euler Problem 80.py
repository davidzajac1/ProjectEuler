import math
irr = []
for x in range(1, 100):
    if len(str(math.sqrt(x))) > 14:
        irr.append(format(math.sqrt(x),'.100f'))


print(irr)

print(math.sqrt(10))
