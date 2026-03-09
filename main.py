from typing import List, Tuple

Point = Tuple[float, float]

def convex_hull_jarvis(points: List[Point]) -> List[Point]:
   pass


if __name__ == "__main__":
    points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)] 
    hull = convex_hull_jarvis(points) 
    print("Convex Hull:", hull)


#Convex Hull: [(0, 0), (0, 3), (3, 3), (3, 0)]