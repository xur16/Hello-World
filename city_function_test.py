from city_functions import city_country
import unittest


class CityTest(unittest.TestCase):
    '测试函数city-function'

    def test_city_function(self):
        name = city_country('taian', 'china')
        self.assertEqual(name, 'Taian, China')


unittest.main()