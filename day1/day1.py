# I wrote this pretty much as soon as I got out of bed... uploaded at school

m, b, d, fa, t = lambda x: abs(x[0]) + abs(x[1]), [], [0] * 4, 0, False
with open("day1.input") as f:
    lst = f.read().strip().split(', ')
for k in lst:
    if k[0] == 'L':
        fa = (fa - 1) % 4
    elif k[0] == 'R':
        fa = (fa + 1) % 4
    for _ in range(int(k[1:])):
        d[fa] += 1
        l = (d[1] - d[3], d[0] - d[2])
        if l in b and not t:
            print("P2:", m(l))
            t = True
        b.append(l)
print("P1:", m(b[-1]))