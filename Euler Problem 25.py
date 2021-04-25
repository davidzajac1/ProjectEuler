def digitcount(x):
    return len(str(x))

n = 2
fib = [1, 1]
while digitcount(fib[n-1]) < 1000:
    fib.append(fib[n-1] + fib[n-2])
    n = n + 1

print(n)
