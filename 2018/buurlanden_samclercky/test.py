#!/usr/bin/env python3

import unittest
import oplossing as o

def data_gen(in_data):
    in_ptr = 0
    for line in in_data:
        yield line

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
        input = data_gen(in_data)
        output = data_gen(ex_data)

        N = int(next(input))

        for n in range(N):
            width, height = list(map(int, next(input).rstrip().split(" ")))

            kaart = []
            for h in range(height):
                kaart.append([c for c in next(input).rstrip()])

            o.print_kaart(kaart)

            o.make_unique(kaart, width, height)

            o.print_kaart(kaart)

            nbs = o.count_neightbours(kaart, width, height)
            o.nbs_to_kaart(kaart, nbs, width, height)

            for y in range(height):
                self.assertEqual(next(output).rstrip(), str(n+1) + " " + " ".join(map(str, kaart[y])))


if __name__ == "__main__":
    unittest.main()
