import unittest
from domain.passenger import Passenger
from infrastructure.plane import Plane
from infrastructure.airline import Airline


class TestAirline(unittest.TestCase):
    """
    Test functions of class Airline
    """

    def setUp(self):
        passenger_list_1 = [Passenger("Andrei", "Pop", 2348231), Passenger("Cazacui", "Maria", 723472),
                            Passenger("Octavian", "Bogdan", 822352)]
        passenger_list_2 = [Passenger("Bicu", "Aida", 72347234), Passenger("Daniel", "Calin", 24234234),
                            Passenger("Cernat", "Mihai", 23425423), Passenger("Bicu", "Ioana", 222346234)]
        passenger_list_3 = [Passenger("Badea", "Nicolae", 222442323), Passenger("Badea", "Ion", 23423514),
                            Passenger("Badic", "Mihai", 9834572)]

        self.passenger_list_update = [Passenger("Andrei", "Pop", 2348231), Passenger("Carla", "Tim", 72342372),
                                      Passenger("Octavian", "Bogdan", 822352)]

        self.empty_plane = Plane()
        self.plane1 = Plane(132, "WizAir", 54, "Milano", passenger_list_1)
        self.plane2 = Plane(234, "AirFlow", 62, "Dubai", passenger_list_2)
        self.plane3 = Plane(623, "CompactAir", 86, "China", passenger_list_3)

        self.airline_1 = Airline([])
        self.airline_2 = Airline([self.empty_plane, self.plane1])
        self.airline_3 = Airline([self.plane2, self.plane3])
        self.airline_4 = Airline([self.empty_plane, self.plane1, self.plane2, self.plane3])

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
