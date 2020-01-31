import unittest
import xmlrunner


class TestTrivialThings(unittest.TestCase):

    def test_int_multiplication(self):
        self.assertEqual(4 * 2, 8)

    def test_str_multiplication(self):
        self.assertEqual(4 * 'a', 'aaaa')


if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        failfast=False,
        buffer=False,
        catchbreak=False
    )
