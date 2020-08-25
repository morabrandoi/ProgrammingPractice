import math
cases = int(input())

for _ in range(cases):
    input()
    all_prices = list(map(int, input().split()))

    new_price = math.ceil(sum(all_prices) / len(all_prices))
    print(new_price)
