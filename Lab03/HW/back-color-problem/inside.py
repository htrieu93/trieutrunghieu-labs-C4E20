from random import randint

#ex 11
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

