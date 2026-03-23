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

import unittest
from main import convex_hull_jarvis


class TestMathFunctions(unittest.TestCase):

    def test_example_from_prompt(self):
        points = [(0,3),(2,2),(1,1),(2,1),(3,0),(0,0),(3,3)]
        expected = {(0,0),(0,3),(3,3),(3,0)}
        result = set(convex_hull_jarvis(points))
        self.assertEqual(result, expected)

    def test_square_with_inner_points(self):
        points = [(0,0),(0,4),(4,4),(4,0),(2,2),(1,1),(3,3)]
        expected = {(0,0),(0,4),(4,4),(4,0)}
        result = set(convex_hull_jarvis(points))
        self.assertEqual(result, expected)

    def test_duplicates(self):
        points = [(0,0),(0,0),(4,0),(4,4),(0,4),(4,0)]
        expected = {(0,0),(0,4),(4,4),(4,0)}
        result = set(convex_hull_jarvis(points))
        self.assertEqual(result, expected)

    def test_all_collinear(self):
        points = [(0,0),(1,1),(2,2),(3,3)]
        expected = {(0,0),(3,3)}
        result = set(convex_hull_jarvis(points))
        self.assertTrue(expected.issubset(result))

    def test_two_points(self):
        points = [(1,1),(3,3)]
        expected = {(1,1),(3,3)}
        result = set(convex_hull_jarvis(points))
        self.assertEqual(result, expected)

    def test_single_point(self):
        points = [(2,2)]
        expected = {(2,2)}
        result = set(convex_hull_jarvis(points))
        self.assertEqual(result, expected)

    def test_triangle(self):
        points = [(0,0),(2,0),(1,2)]
        expected = {(0,0),(2,0),(1,2)}
        result = set(convex_hull_jarvis(points))
        self.assertEqual(result, expected)

    def test_collinear_on_edges(self):
        points = [(0,0),(2,0),(4,0),(4,4),(0,4)]
        expected = {(0,0),(4,0),(4,4),(0,4)}
        result = set(convex_hull_jarvis(points))
        self.assertTrue(expected.issubset(result))


if __name__ == "__main__":
    unittest.main()