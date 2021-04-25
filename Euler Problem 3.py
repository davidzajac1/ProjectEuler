factors = []

for x in range(int((600851475142/2)), 1, -2):
    print(x)
    if 600851475143 % x == 0:
        factors.append(x)
