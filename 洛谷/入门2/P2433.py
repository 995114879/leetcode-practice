from math import sqrt


T = map(int, input())
if T == 1:
    print("I love Luogu!")
elif T == 2:
    print(2 + 4, 10 - 2 - 4, sep=" ")
elif T == 3:
    print(14 // 4)
    print((14 // 4) * 4)
    print(14 - (14 // 4) * 4)
elif T == 4:
    print(round(500/3, 6))
elif T == 5:
    print((260 + 220) // (12 + 20))
elif T == 6:
    print(sqrt(6**2 + 9**2))
elif T == 7:
    print(100 + 10)
    print(100 + 10 - 20)
    print(0)
elif T == 8:
    pi = 3.141593
    r = 5
    print(2 * pi * 5)
    print(pi * r * r)
    print(4 / 3.0 * pi * r**3)
elif T == 9:
    print(((((1+1)*2)+1*2)+1)*2)
elif T == 10:
    print(9)
elif T == 11:
    print(1.0*100/3)
elif T == 12:
    print(13)
    print("R")
elif T == 13:
    pi = 3.141593
    print(int(pow(4/3*pi*(4*4*4+10*10*10),1.0*1/3)))
elif T == 14:
    print(50)