n = int(input())
h = 0
a = 256
c = 256**2
test = 0
for i in range(n):
    b = int(input())
    for m in range(256):
        for r in range(256):
            hn = (37 * (m + r + h)) % 256
            if b == hn + a * r + c * m and hn < 100:
                print('m', m, 'r', r, 'hn', hn)
                test = -1
                h = hn
    if test == 0:
        print(b)
        break
    test = 0
    m = 0
    r = 0
if test == -1:
    print(test)