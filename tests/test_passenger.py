import unittest
from domain.passenger import Passenger


class TestPassenger(unittest.TestCase):
    """
    Test functions of class Passenger
    """
    def setUp(self):
        self.passenger_1 = Passenger('Andrei', 'Pop', 534532423)
        self.passenger_2 = Passenger('Ana', 'Manule', 934233441)
        self.passenger_3 = Passenger("Gheorghe", "Pavel", 926384)

    def test_create(self):
        self.assertEqual(self.passenger_1.get_first_name(), 'Andrei')
        self.assertEqual(self.passenger_2.get_last_name(), 'Manule')
        self.assertEqual(self.passenger_3.get_passport_number(), 926384)

        self.assertEqual(str(self.passenger_1), "Passenger name: Andrei Pop with passport number 534532423.")
        self.assertEqual(str(self.passenger_2), "Passenger name: Ana Manule with passport number 934233441.")
        self.assertEqual(str(self.passenger_3), "Passenger name: Gheorghe Pavel with passport number 926384.")

        self.assertRaises(AttributeError, Passenger, '', 'Andrei', 832423524)
        self.assertRaises(AttributeError, Passenger, 'Andrei', '', 345346345)
        self.assertRaises(AttributeError, Passenger, 'Andrei', 'Radu', 0)

        self.assertRaises(AttributeError, self.passenger_1.update_first_name, '')
        self.assertRaises(AttributeError, self.passenger_1.update_last_name, '')
        self.assertRaises(AttributeError, self.passenger_1.update_passport_number, 0)

        self.passenger_1.update_first_name('Alessia')
        self.assertEqual(self.passenger_1.get_passport_number(), 534532423)
        self.assertEqual(self.passenger_1.get_first_name(), 'Alessia')
        self.assertEqual(self.passenger_1.get_last_name(), 'Pop')

        self.passenger_2.update_last_name('Jordan')
        self.assertEqual(self.passenger_2.get_passport_number(), 934233441)
        self.assertEqual(self.passenger_2.get_first_name(), 'Ana')
        self.assertEqual(self.passenger_2.get_last_name(), 'Jordan')

        self.passenger_3.update_passport_number(7234613)
        self.assertEqual(self.passenger_3.get_passport_number(), 7234613)
        self.assertEqual(self.passenger_3.get_first_name(), 'Gheorghe')
        self.assertEqual(self.passenger_3.get_last_name(), 'Pavel')

        self.assertEqual(str(self.passenger_1), "Passenger name: Alessia Pop with passport number 534532423.")
        self.assertEqual(str(self.passenger_2), "Passenger name: Ana Jordan with passport number 934233441.")
        self.assertEqual(str(self.passenger_3), "Passenger name: Gheorghe Pavel with passport number 7234613.")

    def test_equal(self):
        passenger_1 = Passenger(self.passenger_1.get_first_name(), self.passenger_1.get_last_name(),
                                self.passenger_1.get_passport_number())
        self.assertEqual(passenger_1, self.passenger_1)
        passenger_2 = Passenger(self.passenger_2.get_first_name(), self.passenger_2.get_last_name(),
                                self.passenger_2.get_passport_number())
        self.assertEqual(passenger_2, self.passenger_2)

    def test_check_first_characters(self):
        self.assertEqual(self.passenger_1.check_first_characters(), False)
        self.assertEqual(self.passenger_2.check_first_characters(), False)

        self.equal_characters_1 = self.passenger_1 = Passenger('Andrei', 'Pop', 55555555)
        self.assertEqual(self.equal_characters_1.check_first_characters(), True)

        self.equal_characters_2 = self.passenger_2 = Passenger('Ana', 'Manule', 99924523)
        self.assertEqual(self.equal_characters_2.check_first_characters(), True)

    def test_check_string_containing(self):
        self.assertEqual(self.passenger_1.check_string_containing('reI'), True)
        self.assertEqual(self.passenger_2.check_string_containing('xle'), False)

        self.equal_characters_1 = self.passenger_1 = Passenger('Xzlams', 'Pop', 55555555)
        self.assertEqual(self.equal_characters_1.check_string_containing('XZ'), True)

        self.equal_characters_2 = self.passenger_2 = Passenger('Ana', 'Manule', 99924523)
        self.assertEqual(self.equal_characters_2.check_string_containing('xz'), False)

    def test_check_name(self):
        self.assertEqual(self.passenger_1.check_name('andrei'), True)
        self.assertEqual(self.passenger_2.check_name('xle'), False)

        self.equal_characters_1 = self.passenger_1 = Passenger('Xzlams', 'Pop', 55555555)
        self.assertEqual(self.equal_characters_1.check_name('xzlaMS'), True)

        self.equal_characters_2 = self.passenger_2 = Passenger('Ana', 'Manule', 99924523)
        self.assertEqual(self.equal_characters_2.check_name('Manule'), True)
