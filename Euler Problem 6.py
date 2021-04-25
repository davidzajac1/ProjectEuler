count = 0
for x in range (1, 101):
    count = count + x

sumsquares = count**2

count = 0
for x in range (1, 101):
    print(count)
    count = count + (x**2)

squaresum = count

print(sumsquares-squaresum)
