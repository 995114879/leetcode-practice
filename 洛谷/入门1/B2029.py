h, r = map(int, input().split())
v = 3.14 * r * r * h
n = (20000 - 1) // v + 1
print(int(n))
