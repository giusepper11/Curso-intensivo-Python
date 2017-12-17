import unittest
from Cidade_pais import cidade_pais


class CityTestCase(unittest.TestCase):

    def test_Cidade_Pais(self):
        cid_pa = cidade_pais('sao paulo', 'brasil', 100)
        self.assertEqual(cid_pa, 'Sao Paulo Brasil - 100')


unittest.main
