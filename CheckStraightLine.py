# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
# Check if these points make a straight line in the XY plane.
#
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
#
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false
#
# Constraints:
#     2 <= coordinates.length <= 1000
#     coordinates[i].length == 2
#     -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
#     coordinates contains no duplicate point.


def check_straight_line(coordinates):
    if len(coordinates) == 2:
        return True
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    if x1 == x0:
        slope = None
    else:
        slope = (y1 - y0) / (x1 - x0)
    for x, y in coordinates[2:]:
        if x == x0:
            if slope is not None:
                return False
        elif (y - y0) / (x - x0) != slope:
            return False
    return True


assert check_straight_line([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) is True
assert check_straight_line([[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]]) is True
assert check_straight_line([[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]) is True
