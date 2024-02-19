from math import sqrt
a, b, c = input().split()
a, b, c = float(a), float(b), float(c)
p = 0.5*(a + b + c)
s = sqrt(p*(p - a) * (p - b) * (p - c))
print(f"{s:.1f}")
