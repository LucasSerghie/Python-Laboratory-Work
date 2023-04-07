from controller.plane_controller import PlaneController
import unittest


class TestPlaneController(unittest.TestCase):
    def setUp(self):
        self.empty_plane = PlaneController()
        self.plane1 = PlaneController(132, 'WizAir', 54, 'Milano', [])
        self.plane2 = PlaneController(234, 'AirFlow', 62, 'Dubai', [])

        self.plane1.add_passenger("Andrei", "Pop", 2348231)
        self.plane1.add_passenger("Cazacui", "Maria", 723472)
        self.plane1.add_passenger("Octavian", "Bogdan", 822352)

        self.plane2.add_passenger("Bicu", "Aida", 72347234)
        self.plane2.add_passenger("Daniel", "Calin", 24234234)
        self.plane2.add_passenger("Cernat", "Mihai", 23425423)
        self.plane2.add_passenger("Bicu", "Ioana", 2346234)

    def test_create(self):
        self.assertEqual(str(self.empty_plane),
                         "Plane with number:0 from airline company: with number of seats:0\n"
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

        self.assertEqual(self.empty_plane.get_plane_number(), PlaneController().get_plane_number())
        self.assertEqual(self.empty_plane.get_company(), PlaneController().get_company())
        self.assertEqual(self.empty_plane.get_seats_number(), PlaneController().get_seats_number())
        self.assertEqual(self.empty_plane.get_destination(), PlaneController().get_destination())
        self.assertEqual(self.empty_plane.get_list_of_passengers(), PlaneController().get_list_of_passengers())

        self.assertEqual(self.plane1.get_plane_number(),
                         PlaneController(self.plane1.get_plane_number(), self.plane1.get_company(),
                                         self.plane1.get_seats_number(), self.plane1.get_destination(),
                                         self.plane1.get_list_of_passengers()).get_plane_number())
        self.assertEqual(self.plane1.get_company(),
                         PlaneController(self.plane1.get_plane_number(), self.plane1.get_company(),
                                         self.plane1.get_seats_number(), self.plane1.get_destination(),
                                         self.plane1.get_list_of_passengers()).get_company())
        self.assertEqual(self.plane1.get_seats_number(),
                         PlaneController(self.plane1.get_plane_number(), self.plane1.get_company(),
                                         self.plane1.get_seats_number(), self.plane1.get_destination(),
                                         self.plane1.get_list_of_passengers()).get_seats_number())
        self.assertEqual(self.plane1.get_destination(),
                         PlaneController(self.plane1.get_plane_number(), self.plane1.get_company(),
                                         self.plane1.get_seats_number(), self.plane1.get_destination(),
                                         self.plane1.get_list_of_passengers()).get_destination())
        self.assertEqual(self.plane1.get_list_of_passengers(),
                         PlaneController(self.plane1.get_plane_number(), self.plane1.get_company(),
                                         self.plane1.get_seats_number(), self.plane1.get_destination(),
                                         self.plane1.get_list_of_passengers()).get_list_of_passengers())

        self.plane1.update_company("Polar")
        self.plane1.update_seats_number(94)
        self.plane1.update_destination("Budapest")

        self.plane2.update_company("LightAir")
        self.plane2.update_seats_number(76)
        self.plane2.update_destination("Madrid")

        self.assertEqual(self.plane1.get_plane_number(), 132)
        self.assertEqual(self.plane1.get_company(), "Polar")
        self.assertEqual(self.plane1.get_seats_number(), 94)
        self.assertEqual(self.plane1.get_destination(), "Budapest")

        self.assertEqual(self.plane2.get_plane_number(), 234)
        self.assertEqual(self.plane2.get_company(), "LightAir")
        self.assertEqual(self.plane2.get_seats_number(), 76)
        self.assertEqual(self.plane2.get_destination(), "Madrid")
