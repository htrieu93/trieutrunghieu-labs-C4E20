from random import randint

#Ex 11:
def is_inside(point, rec):
    if point[0] < rec[0]:
        return False
    elif point[1] < rec[1]:
        return False
    elif point[0] > rec[0] + rec[2]:
        return False
    elif point[1] > rec[1] + rec[3]:
        return False
    else:
        return True

# print(is_inside([100, 120], [140, 60, 100, 200]))
# print(is_inside([200, 120], [140, 60, 100, 200]))

#Ex 12: Test case 
for i in range(4):
    point_x = randint(100, 300)
    point_y = randint(100, 300)
    rec = [140, 60, 100, 200]
    check = is_inside([point_x, point_y], rec)
    if check:
        print("Point ({}, {}) is inside the rectangle {}".format(point_x, point_y, rec))
    else:
        print("Point ({}, {}) is outside of the rectangle {}".format(point_x, point_y, rec))

