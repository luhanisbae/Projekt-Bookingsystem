import unittest
from User import User_obj


class MyTestCase(unittest.TestCase):

    def test_create_reservation(self):
        a = User_obj()
        a.create_reservation(1530)
        self.assertEqual(a._reservation, [1530])

    def test_delete_reservation(self):
        a = User_obj()
        a.create_reservation(1630)
        a.create_reservation(1530)
        a.delete_reservation(1630)
        self.assertEqual(a._reservation, [1530])

    def test_edit_reservation(self):
        a = User_obj()
        a.create_reservation(1530)
        a.edit_reservation(1530, 1630)
        self.assertEqual(a._reservation, [1630])


if __name__ == '__main__':
    unittest.main()
