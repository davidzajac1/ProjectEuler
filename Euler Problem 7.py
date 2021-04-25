import math
primes = [2, 3, 5, 7, 11, 13]

def isprime(x):
    for y in range(1, int(x/2)+1, 2):
        print(y)
        if x % y == 0:
            pass
        else:
            return True
    return False

badendingnums = [0, 2, 4, 5, 6, 8,]

print(isprime(30))

count = 13
#while len(primes) <= 10000:
    #z = str(int(count))[len(str(int(count)))-1]
    #if float(z) in badendingnums:
    #    pass
    #else:
    #    if isprime(count) == True:
    #        primes.append(count)
    #count = count + 2


#rint(primes[len(primes)-1])
