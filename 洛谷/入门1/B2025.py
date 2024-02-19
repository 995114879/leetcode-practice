for i in range(5):
    for j in range(5):
        if i == 0 or i == 4:
            if j == 2:
                print("*", end="")
                break
            print(" ", end="")
        if i == 1 or i == 3:
            if j == 0:
                print(" ", end="")
            if 1 <= j < 3:
                print("*", end="")
            if j == 3:
                print("*", end="")
                break
        if i == 2:
            print("*", end="")
    print("")
            
