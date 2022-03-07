#!/usr/bin/env python3

import unittest
import oplossing as o

class OplossingTests(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def collect_data(self, start_id: int, lijst: list[str]) -> list[int]:
        n = int(lijst[start_id])
        return [int(i) for i in lijst[start_id+1:start_id+n+1]]

    def test_wedstrijd(self):
        with open("wedstrijd.invoer") as file:
            in_data = file.readlines()
        with open("wedstrijd.uitvoer") as file:
            ex_data = file.readlines()
        start_id = 1
        for k in range(int(in_data[0])):
            data = self.collect_data(start_id, in_data)
            self.assertEqual(ex_data[k].strip(), " ".join(map(str, o.minmax(k+1, data))))
            start_id += len(data) + 1


if __name__ == "__main__":
    unittest.main()
