import math
queries = int(input())

for _ in range(queries):
    r1, r2, neit = map(int, input().split())
    limiting = min(r1, r2)
    nonlimiting = max(r1, r2)
    # scraping off extra from nonlimiting and adding to neit
    excess = nonlimiting - limiting
    nonlimiting -= excess
    neit += excess

    if neit >= limiting:
        print(limiting)
    else:
        # not enough neithers
        # at this point r1 and r2 are the same
        ideal_middle = math.floor(sum([limiting, nonlimiting, neit]) / 3)
        print(ideal_middle)

