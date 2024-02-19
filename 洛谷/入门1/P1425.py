a, b, c, d = map(int, input().split())
if d - b < 0:
    h = c - a - 1
    m = d + 60 - b
else:
    h = c - a
    m = d - b
print(h, m, sep=" ")
