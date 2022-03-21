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
        in_index = 0
        out_index = 0

        N = int(in_data[in_index])
        in_index += 1
        for n in range(N):
            p, l, w = list(map(int, in_data[in_index].split(" ")))
            in_index += 1
            number_of_steps = int(in_data[in_index])
            in_index += 1

            def splitted(in_index):
                in_index += 1
                return in_data[in_index-1].split(" ")
            steps = [splitted(in_index) for _ in range(number_of_steps)]
            heuristics = o.get_heuristics(steps)
            reduced = o.reduce_heuristic(heuristics, o.get_number_of_carts_per_player(p, l, w))
            self.assertEqual(ex_data[out_index], f"{n+1} " + " ".join(reduced))
            out_index += 1


if __name__ == "__main__":
    unittest.main()
