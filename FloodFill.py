#  An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0
#  to 65535).
#
# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value
# newColor, "flood fill" the image.
#
# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting
# pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with
# the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the
# newColor.
#
# At the end, return the modified image.
#
# Example 1:
# Input:
# image = [[1,1,1],
#          [1,1,0],
#          [1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],
#          [2,2,0],
#          [2,0,1]]
# Explanation:
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.
#
# Note:
# The length of image and image[0] will be in the range [1, 50].
# The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
# The value of each color in image[i][j] and newColor will be an integer in [0, 65535].


def flood_fill(image, sr, sc, new_color):
    def flood_fillx(image, sr, sc):
        nonlocal old_color, numrows, numcols
        image[sr][sc] = new_color  # update image
        visited.add((sr, sc))

        xy_delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for xd, yd in xy_delta:
            if -1 < sr + xd < numrows and -1 < sc + yd < numcols \
                    and image[sr + xd][sc + yd] == old_color and (sr + xd, sc + yd) not in visited:
                flood_fillx(image, sr + xd, sc + yd)

    visited = set()
    numrows = len(image)
    numcols = len(image[0])
    old_color = image[sr][sc]
    flood_fillx(image, sr, sc)
    return image


def flood_fill1(image, sr, sc, new_color):
    numrows = len(image)
    numcols = len(image[0])
    old_color = image[sr][sc]
    if old_color == new_color:
        return image

    def dfs(r, c):
        image[r][c] = new_color
        if (r - 1) > -1 and image[r - 1][c] == old_color:
            dfs(r - 1, c)
        if (r + 1) < numrows and image[r + 1][c] == old_color:
            dfs(r + 1, c)
        if (c - 1) > -1 and image[r][c - 1] == old_color:
            dfs(r, c - 1)
        if (c + 1) < numcols and image[r][c + 1] == old_color:
            dfs(r, c + 1)

    dfs(sr, sc)
    return image


# image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
assert flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
assert flood_fill([[0, 0, 0], [0, 1, 1]], 1, 1, 1) == [[0, 0, 0], [0, 1, 1]]

assert flood_fill1([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
assert flood_fill1([[0, 0, 0], [0, 1, 1]], 1, 1, 1) == [[0, 0, 0], [0, 1, 1]]

# [[0, 0, 0],
#  [0, 1, 1]]
