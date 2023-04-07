import unittest
from controller.airline_controller import AirlineController


class TestAirlineController(unittest.TestCase):
    def setUp(self):
        self.airline_1 = AirlineController([])
        self.airline_2 = AirlineController([])
        self.airline_3 = AirlineController([])
        self.airline_4 = AirlineController([])

        self.airline_2.add_plane(0, '', 0, '', [])
        self.airline_2.add_plane(132, "WizAir", 54, "Milano", [])

        self.airline_3.add_plane(234, "AirFlow", 62, "Dubai", [])
        self.airline_3.add_plane(623, "CompactAir", 86, "China", [])

        self.airline_4.add_plane(0, '', 0, '', [])
        self.airline_4.add_plane(132, "WizAir", 54, "Milano", [])
        self.airline_4.add_plane(234, "AirFlow", 62, "Dubai", [])
        self.airline_4.add_plane(623, "CompactAir", 86, "China", [])

        self.airline_2.add_passenger(2, "Andrei", "Pop", 2348231)
        self.airline_2.add_passenger(2, "Cazacui", "Maria", 723472)
        self.airline_2.add_passenger(2, "Octavian", "Bogdan", 822352)

        self.airline_3.add_passenger(1, "Bicu", "Aida", 72347234)
        self.airline_3.add_passenger(1, "Daniel", "Calin", 24234234)
        self.airline_3.add_passenger(1, "Cernat", "Mihai", 23425423)
        self.airline_3.add_passenger(1, "Bicu", "Ioana", 222346234)

        self.airline_3.add_passenger(2, "Badea", "Nicolae", 222442323)
        self.airline_3.add_passenger(2, "Badea", "Ion", 23423514)
        self.airline_3.add_passenger(2, "Badic", "Mihai", 9834572)

        self.airline_4.add_passenger(2, "Andrei", "Pop", 2348231)
        self.airline_4.add_passenger(2, "Cazacui", "Maria", 723472)
        self.airline_4.add_passenger(2, "Octavian", "Bogdan", 822352)
        self.airline_4.add_passenger(3, "Bicu", "Aida", 72347234)
        self.airline_4.add_passenger(3, "Daniel", "Calin", 24234234)
        self.airline_4.add_passenger(3, "Cernat", "Mihai", 23425423)
        self.airline_4.add_passenger(3, "Bicu", "Ioana", 222346234)
        self.airline_4.add_passenger(4, "Badea", "Nicolae", 222442323)
        self.airline_4.add_passenger(4, "Badea", "Ion", 23423514)
        self.airline_4.add_passenger(4, "Badic", "Mihai", 9834572)

    def test_create(self):
        self.assertEqual(str(self.airline_1), "")

        self.assertEqual(str(self.airline_2), "1: Plane with number:0 from airline company: with number of seats:0\n"
                                              "having the destination: and passengers:\n\n"
                                              "2: Plane with number:132 from airline company:WizAir "
                                              "with number of seats:54\nhaving the destination:Milano and passengers:\n"
                                              "Passenger name: Andrei Pop with passport number 2348231.\n"
                                              "Passenger name: Cazacui Maria with passport number 723472.\n"
                                              "Passenger name: Octavian Bogdan with passport number 822352.\n\n")

        self.assertEqual(str(self.airline_3), "1: Plane with number:234 from airline company:AirFlow "
                                              "with number of seats:62\nhaving the destination:Dubai and passengers:\n"
                                              "Passenger name: Bicu Aida with passport number 72347234.\n"
                                              "Passenger name: Daniel Calin with passport number 24234234.\n"
                                              "Passenger name: Cernat Mihai with passport number 23425423.\n"
                                              "Passenger name: Bicu Ioana with passport number 222346234.\n\n"
                                              "2: Plane with number:623 from airline company:CompactAir "
                                              "with number of seats:86\nhaving the destination:China and passengers:\n"
                                              "Passenger name: Badea Nicolae with passport number 222442323.\n"
                                              "Passenger name: Badea Ion with passport number 23423514.\n"
                                              "Passenger name: Badic Mihai with passport number 9834572.\n\n")

        self.assertEqual(str(self.airline_4), "1: Plane with number:0 from airline company: with number of seats:"
                                              "0\nhaving the destination: and passengers:\n\n"
                                              "2: Plane with number:132 from airline company:WizAir "
                                              "with number of seats:54\nhaving the destination:Milano and passengers:\n"
                                              "Passenger name: Andrei Pop with passport number 2348231.\n"
                                              "Passenger name: Cazacui Maria with passport number 723472.\n"
                                              "Passenger name: Octavian Bogdan with passport number 822352.\n\n"
                                              "3: Plane with number:234 from airline company:AirFlow "
                                              "with number of seats:62\nhaving the destination:Dubai and passengers:\n"
                                              "Passenger name: Bicu Aida with passport number 72347234.\n"
                                              "Passenger name: Daniel Calin with passport number 24234234.\n"
                                              "Passenger name: Cernat Mihai with passport number 23425423.\n"
                                              "Passenger name: Bicu Ioana with passport number 222346234.\n\n"
                                              "4: Plane with number:623 from airline company:CompactAir "
                                              "with number of seats:86\nhaving the destination:China and passengers:\n"
                                              "Passenger name: Badea Nicolae with passport number 222442323.\n"
                                              "Passenger name: Badea Ion with passport number 23423514.\n"
                                              "Passenger name: Badic Mihai with passport number 9834572.\n\n")

        self.assertFalse(self.airline_1 == self.airline_2)
        self.assertFalse(self.airline_1 == self.airline_3)
        self.assertFalse(self.airline_2 == self.airline_3)
        self.assertFalse(self.airline_4 == self.airline_1)
        self.assertFalse(self.airline_4 == self.airline_3)
