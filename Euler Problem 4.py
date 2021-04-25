def pal(x):
    if len(str(x)) % 2 == 0:
        half1 = []
        half2 = []
        for z in range (0, int(len(str(x))/2)):

            half1.append(str(x)[z])
        for z in range(int(len(str(x))/2), int(len(str(x)))):
            half2.append(str(x)[z])
        half2b = []
        for z in range(0, len(half2)):
            half2b.append(half2[len(half2)-z-1])
        if half1 == half2b:
            return(x)
pals = []

for x in range((999*999), (100*100), -1):
    if pal(x) != None:
        pals.append(pal(x))

for x in pals:
    for y in range(999, 100, -1):
        z = x/y
        if (z.is_integer() == True) and (z > 99) and (z < 1000):
            print(x)
            break
