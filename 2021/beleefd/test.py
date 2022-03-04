#!/usr/bin/env python3

import unittest
import oplossing as o

class OplossingTests(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_case1(self):
        in_data = [1, 4, 4, 5, 6, 4, 5, 5, 10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6]
        ex_data = "5 14 29 49 60 61 77 97 117 133"
        self.assertEqual(ex_data, o.parse_game(in_data), "Should be valid")

    def test_invalid(self):
        in_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ex_data = "INVALID"
        self.assertEqual(ex_data, o.parse_game(in_data), "Should be invalid")

    def test_case2(self):
        in_data = list(map(int, "2 4 4 6 6 0 6 0 6 0 3 3 3 3 2 3 7 0 3 5".split(" ")))
        ex_data = "6 22 28 34 40 46 52 57 64 72"
        self.assertEqual(ex_data, o.parse_game(in_data), "Should be valid")

if __name__ == "__main__":
    unittest.main()
