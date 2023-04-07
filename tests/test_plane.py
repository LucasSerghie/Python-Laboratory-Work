import unittest
from infrastructure.plane import Plane
from domain.passenger import Passenger


class TestPlane(unittest.TestCase):
    """
    Test functions of class Plane
    """

    def setUp(self):
        passenger_list_1 = [Passenger("Andrei", "Pop", 2348231), Passenger("Cazacui", "Maria", 723472),
                            Passenger("Octavian", "Bogdan", 822352)]
        passenger_list_2 = [Passenger("Bicu", "Aida", 72347234), Passenger("Daniel", "Calin", 24234234),
                            Passenger("Cernat", "Mihai", 23425423), Passenger("Bicu", "Ioana", 2346234)]

        self.error_list_1 = [Passenger("Andrei", "Pop", 2348231), Passenger("Cazacui", "Maria", 723472),
                             Passenger("Octavian", "Bogdan", 2348231)]
        self.error_list_2 = [Passenger("Bicu", "Aida", 72347234), Passenger("Daniel", "Calin", 24234234),
                             Passenger("Cernat", "Mihai", 24234234), Passenger("Bicu", "Ioana", 2346234)]

        self.empty_plane = Plane()
        self.plane1 = Plane(132, 'WizAir', 54, 'Milano', passenger_list_1)
        self.plane2 = Plane(234, 'AirFlow', 62, 'Dubai', passenger_list_2)

    def test_create(self):
        self.assertEqual(str(self.empty_plane), "Plane with number:0 from airline company: with number of seats:0\n"
                                                "having the destination: and passengers:\n")

        self.assertEqual(str(self.plane1), "Plane with number:132 from airline company:WizAir "
                                           "with number of seats:54\nhaving the destination:Milano and passengers:\n"
                                           "Passenger name: Andrei Pop with passport number 2348231.\n"
                                           "Passenger name: Cazacui Maria with passport number 723472.\n"
                                           "Passenger name: Octavian Bogdan with passport number 822352.\n")

        self.assertEqual(str(self.plane2), "Plane with number:234 from airline company:AirFlow "
                                           "with number of seats:62\nhaving the destination:Dubai and passengers:\n"
                                           "Passenger name: Bicu Aida with passport number 72347234.\n"
                                           "Passenger name: Daniel Calin with passport number 24234234.\n"
                                           "Passenger name: Cernat Mihai with passport number 23425423.\n"
                                           "Passenger name: Bicu Ioana with passport number 2346234.\n")

        self.assertEqual(self.empty_plane, Plane())

        self.assertEqual(self.plane1, Plane(self.plane1.get_plane_number(), self.plane1.get_company(),
                                            self.plane1.get_seats_number(), self.plane1.get_destination(),
                                            self.plane1.get_list_of_passengers()))

        self.assertEqual(self.plane2, Plane(self.plane2.get_plane_number(), self.plane2.get_company(),
                                            self.plane2.get_seats_number(), self.plane2.get_destination(),
                                            self.plane2.get_list_of_passengers()))

        self.assertFalse(self.plane1 == self.plane2)
        self.assertFalse(self.plane1 == self.empty_plane)
        self.assertFalse(self.plane2 == self.empty_plane)

        self.assertRaises(AttributeError, Plane, 132, 'WizAir', 54, 'Milano', self.error_list_1)
        self.assertRaises(AttributeError, Plane, 132, 'WizAir', 54, 'Milano', self.error_list_2)

        self.plane1.update_seats_number(46)
        self.plane1.update_company("DeltaAir")
        self.plane1.update_destination("Rome")

    def test_sort_passengers_by_last_name(self):
        self.plane1.sort_passengers_by_last_name()
        self.assertEqual(str(self.plane1), "Plane with number:132 from airline company:WizAir "
                                           "with number of seats:54\nhaving the destination:Milano and passengers:\n"
                                           "Passenger name: Octavian Bogdan with passport number 822352.\n"
                                           "Passenger name: Cazacui Maria with passport number 723472.\n"
                                           "Passenger name: Andrei Pop with passport number 2348231.\n")

        self.plane2.sort_passengers_by_last_name()
        self.assertEqual(str(self.plane2), "Plane with number:234 from airline company:AirFlow "
                                           "with number of seats:62\nhaving the destination:Dubai and passengers:\n"
                                           "Passenger name: Bicu Aida with passport number 72347234.\n"
                                           "Passenger name: Daniel Calin with passport number 24234234.\n"
                                           "Passenger name: Bicu Ioana with passport number 2346234.\n"
                                           "Passenger name: Cernat Mihai with passport number 23425423.\n")

    def test_passengers_by_name_beginning(self):
        passengers_0 = self.empty_plane.passengers_by_name_beginning("bi")
        passengers_1 = self.plane1.passengers_by_name_beginning("bi")
        passengers_2 = self.plane2.passengers_by_name_beginning("bi")

        self.assertEqual(passengers_0, 0)
        self.assertEqual(passengers_1, 0)
        self.assertEqual(passengers_2, 2)

    def test_concatenation(self):
        empty_concatenation = self.empty_plane.concatenation()
        concatenation_1 = self.plane1.concatenation()
        concatenation_2 = self.plane2.concatenation()

        self.assertEqual(empty_concatenation, '0')
        self.assertEqual(concatenation_1, '3Milano')
        self.assertEqual(concatenation_2, '4Dubai')

    def test_passport_number_beginning(self):
        passenger_list_1 = [Passenger("Andrei", "Pop", 2222222), Passenger("Cazacui", "Maria", 77723472),
                            Passenger("Octavian", "Bogdan", 88822352)]
        passenger_list_2 = [Passenger("Bicu", "Aida", 72347234), Passenger("Daniel", "Calin", 24234234),
                            Passenger("Cernat", "Mihai", 23425423), Passenger("Bicu", "Ioana", 2346234)]

        plane1 = Plane(132, 'WizAir', 54, 'Milano', passenger_list_1)
        plane2 = Plane(234, 'AirFlow', 62, 'Dubai', passenger_list_2)

        self.assertTrue(plane1.passport_number_beginning())
        self.assertFalse(plane2.passport_number_beginning())
        self.assertFalse(self.empty_plane.passport_number_beginning())

    def test_check_passengers_string(self):
        self.assertEqual(self.plane1.check_passengers_string("o"),
                         [Passenger("Andrei", "Pop", 2348231), Passenger("Octavian", "Bogdan", 822352)])
        self.assertEqual(self.plane2.check_passengers_string('Bi'),
                         [Passenger("Bicu", "Aida", 72347234), Passenger("Bicu", "Ioana", 2346234)])
        self.assertEqual(self.empty_plane.check_passengers_string('su'), [])

    def test_check_passenger_name(self):
        self.assertTrue(self.plane1.check_passenger_name("Andrei"))
        self.assertTrue(self.plane2.check_passengers_string("Bicu"))
        self.assertFalse(self.empty_plane.check_passenger_name('Radu'))
