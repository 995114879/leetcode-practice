a, b = map(int, input().split())
m = a * 10 + b
for i in range(1, a+1):
    t = i * 19
    if t > m:
        break
print(i-1)