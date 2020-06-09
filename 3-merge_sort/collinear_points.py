#!/usr/bin/python3
# Given a set of n distinct points in the plane, find every
# (maximal) line segment that connects a subset of 4 or more
# of the points


class Point():
    # Define a point
    def __init__(self, x, y):
        # Initialize a point
        self.x = x
        self.y = y

    def __str__(self):
        # Return a string
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __eq__(self, that):
        # Check if two points are equal
        return self.y == that.y and self.x == that.x

    def __ne__(self, that):
        # Check if two points are not equal
        return self.y != that.y or self.x != that.x

    def __lt__(self, that):
        # Check if self is less than that
        if self.y == that.y:
            return self.x - that.x < 0
        return self.y - that.y < 0

    def __le__(self, that):
        # Check if self is less than or equal to that
        return self.__eq__(that) or self.__lt__(that)

    def __gt__(self, that):
        # Check if self is greater than that
        if self.y == that.y:
            return self.x - that.x > 0
        return self.y - that.y > 0

    def __ge__(self, that):
        # Check if self is greater than or equal to that
        return self.__eq__(that) or self.__gt__(that)

    def compare(self, that):
        # Compare two points by y-coordinates,
        # breaking ties by x-coordinates
        # Return 0 if equal, negative int if self is less than that,
        # positive int if self is greater than that
        if self.y == that.y:
            return self.x - that.x
        return self.y - that.y

    def slope(self, that):
        # Return the slope between two points
        if self == that:
            return float('-inf')
        elif that.x - self.x == 0:
            return float('inf')
        return (that.y - self.y) / (that.x - self.x)


class LineSegment:
    # Define a line segment between two points
    def __init__(self, p, q):
        # Initialize a line segment
        self.p = p
        self.q = q

    def __str__(self):
        # Return a string
        return str(self.p) + ' -> ' + str(self.q)


class BruteCollinearPoints:
    # Examine 4 points at a time and check whether they all lie
    # on the same line segment
    def __init__(self, points):
        # Find all line segments containing 4 points
        if not points:
            raise Exception('No points provided')
        self.segments = []
        for i in range(0, len(points), 4):
            if (points[i].slope(points[i + 1]) ==
                points[i].slope(points[i + 2]) ==
                    points[i].slope(points[i + 3])):
                minimum = min(points[i], points[i + 1],
                              points[i + 2], points[i + 3])
                maximum = max(points[i], points[i + 1],
                              points[i + 2], points[i + 3])
                line = LineSegment(minimum, maximum)
                self.segments.append(line)

    def __str__(self):
        # Return a string
        s = ''
        for segment in self.segments:
            s += str(segment) + '\n'
        return s


class FastCollinearPoints:
    # Sort points according to the slope they make
    def __init__(self, points):
        # Find all line segments containing 4 or more points
        if not points:
            raise Exception('No points provided')
        self.segments = []
        for p in range(len(points)):
            self.p = points[p]
            self.slopes = []
            for i in range(len(points)):
                if p != i:
                    self.slopes.append(self.p.slope(points[i]))
                else:
                    self.slopes.append(float('-inf'))
            merge_sort(self.slopes)
            for i in range(2, len(self.slopes)):
                if self.slopes[i] == self.slopes[i - 2]:
                    # Bad logic here, indexes don't line up correctly
                    minimum = min(self.p, points[i],
                                  points[i - 1], points[i - 2])
                    maximum = max(self.p, points[i],
                                  points[i - 1], points[i - 2])
                    line = LineSegment(minimum, maximum)
                    self.segments.append(line)

    def __str__(self):
        # Return a string
        s = ''
        for segment in self.segments:
            s += str(segment) + '\n'
        return s


def merge_sort(a):
    # Implement merge sort
    if len(a) < 2:
        return
    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__':
    a = Point(10000, 0)
    b = Point(0, 10000)
    c = Point(3000, 7000)
    d = Point(7000, 3000)
    e = Point(20000, 21000)
    f = Point(3000, 4000)
    g = Point(14000, 15000)
    h = Point(6000, 7000)

    points = [a, b, c, d, e, f, g, h]
    brute = BruteCollinearPoints(points)
    print(brute)

    fast = FastCollinearPoints(points)
    print(fast)

    a = Point(19000, 10000)
    b = Point(18000, 10000)
    c = Point(32000, 10000)
    d = Point(21000, 10000)
    e = Point(1234, 5678)
    f = Point(14000, 10000)
    points = [a, b, c, d, e, f]
    fast = FastCollinearPoints(points)
    print(fast)
