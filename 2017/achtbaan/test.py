#!/usr/bin/env python3

import unittest
import oplossing as o

class OplossingTests(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_wedstrijd(self):
        with open("wedstrijd.invoer") as file:
            in_data = file.readlines()
        with open("wedstrijd.uitvoer") as file:
            ex_data = file.readlines()
        self.file_test(in_data, ex_data)

    def test_voorbeeld(self):
        with open("voorbeeld.invoer") as file:
            in_data = file.readlines()
        with open("voorbeeld.uitvoer") as file:
            ex_data = file.readlines()
        self.file_test(in_data, ex_data)

    def file_test(self, in_data, ex_data):
        """Test program from file input"""
        pass

if __name__ == "__main__":
    unittest.main()
