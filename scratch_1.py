def nth(n, x):
    return (n % 10**x - n % 10**(x - 1)) // 10**(x - 1)


k = int(input())
s = ''
for i in range(len(str(k)), 0, -1):
    q = nth(k, i)
    if q % 2 == 1:
        s += str(q)
print(s)