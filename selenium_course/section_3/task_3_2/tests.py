import unittest
from task_1_6_11 import check_registration


class TestRegistration(unittest.TestCase):
    def test_first_page(self):
        self.assertEqual(
            check_registration('http://suninjuly.github.io/registration1.html'),
            'Congratulations! You have successfully registered!',
            'First page test failed')

    def test_second_page(self):
        self.assertEqual(
            check_registration('http://suninjuly.github.io/registration2.html'),
            'Congratulations! You have successfully registered!',
            'Second page test failed')


if __name__ == '__main__':
    unittest.main()
