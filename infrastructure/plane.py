from domain.passenger import Passenger


class Plane:
    """
        Represents a plane which has the following attributes:
                -plane number
                -company
                -seats number
                -destination
                -list of passengers(of type Passenger)
        The class could raise several error in it's methods
        """
    def __init__(self, plane_number=0, company='', seats_number=0, destination='', list_of_passengers=None):
        """
        Creates a new instance of a plane
        :param : unique identifier of a vector
        :param color: color of vector (has to be from list r, g, b, y, m)
        :param type: type of vector
        :param values: values of the vector tip
        """
        if list_of_passengers is None:
            list_of_passengers = []
        self.__passengers = []

        if plane_number >= 0:
            self.__plane_number = plane_number
        else:
            raise AttributeError("Plane number must be greater than 0.")

        self.__company = company

        if seats_number >= 0:
            self.__seats_number = seats_number
        else:
            raise ValueError("Seats number must be greater than 0.")

        self.__destination = destination

        for passenger in list_of_passengers:
            if self.unique_passport_number(passenger.get_passport_number()) is False and len(self.__passengers)+1 < self.__seats_number:
                self.__passengers.append(passenger)
            else:
                raise AttributeError("Two passengers have the same passport number.")

    def __str__(self):
        """
        Return the string representation of a plane
        :return:
        """
        string = f"Plane with number:{self.__plane_number} from airline company:{self.__company} with number of seats:" \
                 f"{self.__seats_number}\nhaving the destination:{self.__destination} and passengers:\n"
        for passenger in self.__passengers:
            string += str(passenger) + "\n"
        return string

    def __eq__(self, other):
        """
        Defines if two planes are equal or not
        :param other:
        :return:
        """
        return self.__plane_number == other.__plane_number and \
               self.__company == other.__company and \
               self.__seats_number == other.__seats_number and \
               self.__destination == other.__destination and \
               self.__passengers == other.__passengers

    def get_passenger(self, passport_number):
        for passenger in self.__passengers:
            if passenger.get_passport_number() == passport_number:
                return passenger

    def add_passenger(self, new_first_name, new_last_name, new_passport_number):
        self.__passengers.append(Passenger(new_first_name, new_last_name, new_passport_number))

    def unique_passport_number(self, passport_number):
        for passenger in self.__passengers:
            if passenger.get_passport_number() is passport_number:
                return True
        return False

    def get_plane_number(self):
        return self.__plane_number

    def get_company(self):
        return self.__company

    def get_seats_number(self):
        return self.__seats_number

    def get_destination(self):
        return self.__destination

    def get_list_of_passengers(self):
        return self.__passengers

    def update_company(self, new_company):
        self.__company = new_company

    def update_seats_number(self, new_seats_number):
        if new_seats_number > 0:
            self.__seats_number = new_seats_number
        else:
            raise ValueError("Seats number must be greater than 0.")

    def update_destination(self, new_destination):
        self.__destination = new_destination

    def update_passenger_first_name(self, index, new_first_name):
        if index > len(self.__passengers) or index < 1:
            raise IndexError("Index out of range.")
        else:
            self.__passengers[index - 1].update_first_name(new_first_name)

    def update_passenger_last_name(self, index, new_last_name):
        if index > len(self.__passengers) or index < 1:
            raise IndexError("Index out of range.")
        else:
            self.__passengers[index - 1].update_last_name(new_last_name)

    def update_passenger_passport_number(self, index, new_passport_number):
        if index > len(self.__passengers) or index < 1:
            raise IndexError("Index out of range.")
        else:
            if self.unique_passport_number(new_passport_number) is False:
                self.__passengers[index - 1].update_passport_number(new_passport_number)
            else:
                raise AttributeError("Two passengers have the same passport number.")

    def delete_passenger(self, passport_number):
        """
        Delete passenegr by passport number
        :param passport_number:
        :return:
        """
        for passenger in self.__passengers:
            if passenger.get_passport_number() == passport_number:
                del passenger

    def sort_passengers_by_last_name(self):
        """
        Sort passengers alphabetically by last name
        :return:
        """
        ordered = False
        i = 0
        while i < len(self.__passengers) and not ordered:
            ordered = True
            for j in range(len(self.__passengers) - i - 1):
                if self.__passengers[j].get_last_name() > self.__passengers[j + 1].get_last_name():
                    self.__passengers[j], self.__passengers[j + 1] = self.__passengers[j + 1], self.__passengers[j]
                    ordered = False

    def passengers_by_name_beginning(self, name_beginning):
        """
        Counts passengers that have a given name beginning
        :param name_beginning:
        :return:
        """
        name_beginning = str(name_beginning).lower()
        number_of_passengers = 0
        for passenger in self.__passengers:
            if str(passenger.get_first_name()).lower().startswith(name_beginning):
                number_of_passengers += 1
        return number_of_passengers

    def concatenation(self):
        """
        Creates the concatenation between number of passengers and the destination
        :return:
        """
        concatenation = str(len(self.__passengers))
        concatenation += str(self.__destination)
        return concatenation

    def passport_number_beginning(self):
        """
        Check if there is a passenger that has the same first three numbers in the passport number the same
        :return:
        """
        if len(self.__passengers) == 0:
            return False
        for passenger in self.__passengers:
            if passenger.check_first_characters() is True:
                return True
        return False

    def check_passengers_string(self, string):
        """
        Check if there is a passenger that has a name that contains a given string
        :param string:
        :return:
        """
        passengers = []
        string = str(string).lower()
        for passenger in self.__passengers:
            if passenger.check_string_containing(string) is True:
                passengers.append(passenger)
        return passengers

    def check_passenger_name(self, name):
        """
        Check if there is a passenger that has the last name equal to a given name
        :param name:
        :return:
        """
        name = str(name).lower()
        for passenger in self.__passengers:
            if passenger.check_name(name) is True:
                return True
        return False

    def group_passengers_by_last_name(self):
        pass
