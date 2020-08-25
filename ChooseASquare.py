#TRASH


# import itertools

# num_points = int(input())

# points = []
# costs = {}
# for _ in range(num_points):
#     x, y, c = map(int, input().split())
#     points.append((x,y))
#     costs[(x,y)] = c

# # find all squares

# squares = []
# corner_points = []
# #looking for points on y=x
# for point in points:
#     if point[0] == point[1]:
#         corner_points.append(point)

# # square just defined by points on y=x, lower left corner and upper right
# possible_squares = itertools.combinations(corner_points, 2)


# # [((a,b), (c,d)), ((a1,b1), (c1,d1)), ...]
# for_sure_squares = []

# for p in possible_squares:
#     if ((p[0][0], p[1][1]) in points) and ((p[0][1], p[1][0]) in points):
#         for_sure_squares.append(p)

# def enclosed(p1, p2, test):
#     if p1[0] < p2[0]:
#         bl = p1
#         tr = p2
#     else:
#         bl = p2
#         tr = p1
    
#     if (bl[0] <= test[0] <= tr[0]) and bl[1] <= test[1] <= tr[1]:
#         return True
#     else:
#         return False

# max_value = 0
# max_value_square = (corner_points[0],corner_points[0])

# print(points)
# [print(x) for x in possible_squares]
# print(for_sure_squares)


# for sq in for_sure_squares:
#     side_length = abs(sq[0][0] - sq[1][0])

#     # find sum cost of all points enclosed
#     total_cost = sum([costs[p] for p in points if enclosed(sq[0], sq[1], p)])

#     max_value = max(max_value, total_cost - side_length)

# # print(max_value)    


