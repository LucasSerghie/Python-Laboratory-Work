from infrastructure.plane import Plane


class Airline:
    """
    Represents an airline which has the following attributes:
                -list of plane
    The class could raise several error in it's methods

    """
    def __init__(self, plane_list=None):
        """
        Creates a new instance of a airline
        :param plane_list: list of planes
        """
        if plane_list is None:
            plane_list = []
        self.__planes = []
        for plane in plane_list:
            if plane not in self.__planes:
                self.__planes.append(plane)

    def __str__(self):
        """
        Defines the string representation of a airline
        :return:
        """
        index = 1
        string = ""
        for plane in self.__planes:
            string += f"{index}: " + str(plane) + "\n"
            index += 1
        return string

    def __eq__(self, other):
        """
        Defines if two airlines are equal
        :param other:
        :return:
        """
        return self.__planes == other.__planes

    def __len__(self):
        """
        Defines the length of the airline
        :return:
        """
        return len(self.__planes)

    def get_plane(self, index):
        return self.__planes[index-1]

    def add_passenger(self, index, new_first_name, new_last_name, new_passport_number):
        self.__planes[index - 1].add_passenger(new_first_name, new_last_name, new_passport_number)

    def update_passenger_first_name(self, index, new_first_name):
        self.__planes[index].update_passenger_first_name(index, new_first_name)

    def add_plane(self, plane_number, company, seats_number, destination, list_of_passengers=None):
        """
        Adds new plane in the airline
        :param plane_number:
        :param company:
        :param seats_number:
        :param destination:
        :param list_of_passengers:
        :return:
        """
        self.__planes.append(Plane(plane_number, company, seats_number, destination, list_of_passengers))

    def delete_passenger(self, plane_index, passenger_index):
        """
        Delete passenger from a chosen plane in the airline
        :param plane_index:
        :param passenger_index:
        :return:
        """
        self.__planes[plane_index].delete_passenger(passenger_index)

    def delete_plane(self, index):
        """
        Delete a chosen plane from the airline
        :param index:
        :return:
        """
        if index < 1 or index > len(self.__planes):
            raise IndexError("Index out of range.")
        else:
            del self.__planes[index - 1]

    def sort_passengers_by_last_name(self, index):
        """
        Sort passengers from a chosen plane by last name
        :param index:
        :return:
        """
        self.__planes[index-1].sort_passengers_by_last_name()

    def sort_planes_by_passenger_number(self):
        """
        Sort planes by passenger number
        :return:
        """
        ordered = False
        i = 0
        while i < len(self.__planes) and not ordered:
            ordered = True
            for j in range(len(self.__planes) - i - 1):
                if len(self.__planes[j].get_list_of_passengers()) > len(self.__planes[j + 1].get_list_of_passengers()):
                    self.__planes[j], self.__planes[j + 1] = self.__planes[j + 1], self.__planes[j]
                    ordered = False

    def sort_passengers_by_name_beginning(self, name_beginning):
        """
        Sort planes by name beginning
        :param name_beginning:
        :return:
        """
        ordered = False
        i = 0
        while i < len(self.__planes) and not ordered:
            ordered = True
            for j in range(len(self.__planes) - i - 1):
                if self.__planes[j].passengers_by_name_beginning(name_beginning) > \
                        self.__planes[j + 1].passengers_by_name_beginning(name_beginning):
                    self.__planes[j], self.__planes[j + 1] = self.__planes[j + 1], self.__planes[j]
                    ordered = False

    def sort_by_concatenation(self):
        ordered = False
        i = 0
        while i < len(self.__planes) and not ordered:
            ordered = True
            for j in range(len(self.__planes) - i - 1):
                if self.__planes[j].concatenation() > self.__planes[j + 1].concatenation():
                    self.__planes[j], self.__planes[j + 1] = self.__planes[j + 1], self.__planes[j]
                    ordered = False

    def identify_planes_with_first_three(self):
        planes = []
        for plane in self.__planes:
            if plane.passport_number_beginning() is True:
                planes.append(plane)
        return Airline(planes)

    def check_plane_with_string(self, index, string):
        index -= 1
        if index > len(self.__planes):
            raise IndexError("Index out of range")
        passengers = self.__planes[index].check_passengers_string(string)
        return passengers

    def check_planes_by_passengers_with_name(self, name):
        planes = []
        for plane in self.__planes:
            if plane.check_passenger_name(name) is True:
                planes.append(plane)
        return Airline(planes)
