from domain.passenger import Passenger
from infrastructure.plane import Plane
from infrastructure.airline import Airline


def data_examples():
    """
    Data example for user interface
    :return:
    """
    passenger_list_1 = [Passenger("Andrei", "Pop", 2348231), Passenger("Cazacui", "Maria", 723472),
                        Passenger("Octavian", "Bogdan", 822352)]
    passenger_list_2 = [Passenger("Bicu", "Aida", 72347234), Passenger("Daniel", "Calin", 24234234),
                        Passenger("Cernat", "Mihai", 23425423), Passenger("Bicu", "Ioana", 222346234)]
    passenger_list_3 = [Passenger("Badea", "Nicolae", 222442323), Passenger("Badea", "Ion", 23423514),
                        Passenger("Badic", "Mihai", 9834572)]

    empty_plane = Plane()
    plane1 = Plane(132, "WizAir", 54, "Milano", passenger_list_1)
    plane2 = Plane(234, "AirFlow", 62, "Dubai", passenger_list_2)
    plane3 = Plane(623, "CompactAir", 86, "China", passenger_list_3)

    return [empty_plane, plane1, plane2, plane3]
