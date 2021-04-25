def test(x):
    for y in range(11,20):
        if x % y != 0:
            return None
    return x

z = 0
count = 2520
while z < 1:
    if test(count) != None:
        print(str(count) + " is answer!")
        break
    count = count + 2520
