import unittest
from User import User_obj


class MyTestCase(unittest.TestCase):

    def test_create_reservation(self):
        a = User_obj()
        print(a)
        a.create_reservation(1530)
        self.assertEqual(a._reservation, [1530])


if __name__ == '__main__':
    unittest.main()
