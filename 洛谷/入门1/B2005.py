m = input()
for i in range(3):
    for j in range(5):
        if i == 0:
            if j == 2:
                print(m)
                break
            print(" ", end="")
        if i == 1:
            if j == 0:
                print(" ", end="")
            if 1 <= j < 3:
                print(m, end="")
            if j == 3:
                print(m)
                break
        if i == 2:
            print(m, end="")
