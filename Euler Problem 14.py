def collatz(x):
    n = x
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n /2
            count = count + 1
        else:
            n = 3*n + 1
            count = count + 1
    return count


max = 0
for x in range(1,1000000):
    if collatz(x) > max:
        max = collatz(x)
        print(x)
        print(collatz(x))
