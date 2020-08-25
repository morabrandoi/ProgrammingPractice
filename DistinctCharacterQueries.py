mainString = list(input())
numQ = int(input())

for _ in range(numQ):
    qType, p1, p2 = input().split()

    if qType == "1":
        mainString[int(p1) - 1] = p2
    else:
        # sub = set(mainString[int(p1)-1:int(p2)])
        distinctChar = set(mainString[int(p1)-1:int(p2)])
        # print(sub)
        print(len(distinctChar))

