import math


def ispyth(a, b, c):
    if (a + b == c) and (math.sqrt(a) + math.sqrt(b) + math.sqrt(c) == 1000):
        return True
    else:
        return False
squares = []
for x in range(1,1001):
    squares.append(x**2)


for a in squares:
    for b in squares:
        for c in squares:
            if ispyth(a, b, c) == True:
                print(math.sqrt(a)*math.sqrt(b)*math.sqrt(c))
                break
