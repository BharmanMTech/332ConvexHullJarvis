"""
Brock Harman
CSCI 332 Spring 2026
Programming Assignment #class18
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""

from typing import List, Tuple

Point = Tuple[float, float]


def orientation(p: Point, q: Point, r: Point) -> int:

    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1]) # determinant equation

    # orientation based on determinant sign
    if val == 0:
        return 0
    
    elif val > 0:
        return 1
    
    else:
        return 2


def convex_hull_jarvis(points: List[Point]) -> List[Point]:


    n = len(points)
    if n < 3:
        return points

    hull = []

    # find left most point
    left = 0

    for i in range(1, n):

        if points[i][0] < points[left][0]:
            left = i

    p = left

    while True:

        hull.append(points[p])

        q = (p + 1) % n

        #compares points to find more counter clockwise point
        for r in range(n):

            if orientation(points[p], points[r], points[q]) == 2:
                q = r

        p = q

        if p == left:
            break

    return hull


if __name__ == "__main__":

    points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]

    hull = convex_hull_jarvis(points)

    print("Convex Hull:", hull)