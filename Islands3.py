import queue

mapMat = []
row, col = map(int, input().split())
for _ in range(row):
    mapMat.append(list(input()))

    
def printMat(mat):
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            print(mat[r][c], end=" ")
        print()

