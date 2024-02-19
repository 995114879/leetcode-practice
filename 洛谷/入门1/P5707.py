s, v = input().split()
s, v = int(s), int(v)
n = 8 * 60 + 24 * 60
t = (s - 1) // v + 1 + 10
t = n - t
if t >= 24 * 60:
    t -= 24 * 60
h = t // 60
t = t % 60
if t < 10:
    t = "0" + str(t)
else:
    t = str(t)
if t == "60":
    t = "00"
if h < 10:
    h = "0" + str(h)
else:
    h = str(h)
print(h + ":" + t)


