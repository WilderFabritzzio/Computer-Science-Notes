import sys
data = list(map(int, sys.stdin.read().split()))

t = data[0]
pos = 1

for _ in range(t):

    ax, ay = data[pos], data[pos + 1]
    pos += 2

    bx, by = data[pos], data[pos + 1]
    pos += 2

    fx, fy = data[pos], data[pos + 1]
    pos += 2

    distancia = abs(ax - bx) + abs(ay - by)



    if ay== by:
        if fy == ay and min(ax,bx)< fx < max(ax,bx):
            distancia += 2

    if ax == bx:
        if fx == ax and min(ay,by)< fy < max(ay,by):
            distancia += 2

    print(distancia)
