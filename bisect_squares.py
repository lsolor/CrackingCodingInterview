class Square:

    def __init__(self, top_left, top_right, bot_left, bot_right):
        self.tl = top_left
        self.tr = top_right
        self.bl = bot_left
        self.br = bot_right


class Point:

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)


def find_center(sq):
    center_x = sq.tl.x + abs(sq.tr.x - sq.tl.x)/2
    center_y = sq.bl.y + abs(sq.tl.y - sq.bl.y)/2
    return Point(center_x, center_y)


def find_slope(center_a, center_b):
    return (center_a.y - center_b.y) / (center_a.x - center_b.x)


def find_b(center, slope):
    return center.y - (center.x * slope)


def bisect_square(sq_a, sq_b):

    center_a = find_center(sq_a)
    center_b = find_center(sq_b)
    slope = find_slope(center_a, center_b)
    y_int = find_b(center_a, slope)

    print("y = %.2fx + %.2f" %(slope, y_int))


if __name__ == "__main__":
    square_a = Square(Point(1, 3), Point(3, 3), Point(1, 1), Point(3, 1))
    square_b = Square(Point(2, -1), Point(4, -1), Point(2, -4), Point(4, -4))
    bisect_square(square_a, square_b)