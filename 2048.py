queries = int(input())

for _ in range(queries):
    cardinality = int(input())

    multiset = map(int, input().split())
    # strip values above 2048
    multiset = filter(lambda x: x <= 2048, multiset)
    
    # print("Here is multiset: ")
    # [print(x) for x in multiset]

    if sum(multiset) < 2048:
        print("NO")
    else:
        print("yes")
    
    
