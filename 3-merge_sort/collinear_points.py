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
        return (that.y - self.y) / (that.x - self.x)


class LineSegment:
    # Define a line segment between two points
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __str__(self):
        return str(self.p) + ' -> ' + str(self.q)


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
    print(a)


if __name__ == '__main__':
    '''
    a = [(19000, 10000), (18000, 10000), (32000, 10000),
         (21000, 10000), (1234, 5678), (14000, 10000)]
    '''

    a = Point(0, 0)
    b = Point(1, 2)
    c = Point(3, 4)
    d = Point(5, 6)

    p = LineSegment(a, b)
    q = LineSegment(c, d)
    print(a, b, c, d)
    print(p)
    print(q)
