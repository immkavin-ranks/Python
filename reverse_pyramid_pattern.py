# reverse pyramid
n = 9
for i in range(n):
    for j in range(i * 2):
        print(" ", end=" ")
    print("* " * (2 * (n - i) - 1))
