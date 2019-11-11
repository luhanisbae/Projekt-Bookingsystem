import unittest
from User import User_obj
from Data_layer import UsernameAndPass


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

    def test_show_reservation_interval(self):
        a = User_obj()
        for i in range(5):
            a.create_reservation(1500 + i*100)
        self.assertEqual(a.show_reservation_interval(1600, 1800), [1600, 1700, 1800])

    def test_create_user(self):
        a = UsernameAndPass()
        a.create_user("gamer", "tyler")
        self.assertEqual(a._userspass["gamer"], "tyler")



if __name__ == '__main__':
    unittest.main()
