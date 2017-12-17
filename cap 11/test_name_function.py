import unittest
import name_function


class NamesTestCase(unittest.TestCase):
    """Testes para 'name_function'"""

    def test_first_last_name(self):
        """Nomes como 'Janis Joplin funcionam?"""
        formated_name = name_function.get_formated('janis', 'joplin', )
        self.assertEqual(formated_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        fomated_name = name_function.get_formated('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(fomated_name, 'Wolfgang Amadeus Mozart')
        


unittest.main