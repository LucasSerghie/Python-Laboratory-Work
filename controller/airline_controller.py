from infrastructure.airline import Airline


class AirlineController:
    def __init__(self, plane_list=None):
        self.__planes = Airline(plane_list)

    def __str__(self):
        return str(self.__planes)

    def add_passenger(self, index, new_first_name, new_last_name, new_passport_number):
        self.__planes.add_passenger(index, new_first_name, new_last_name, new_passport_number)

    def add_plane(self, plane_number, company, seats_number, destination, list_of_passengers):
        self.__planes.add_plane(plane_number, company, seats_number, destination, list_of_passengers)

    def get_plane(self, index):
        return self.__planes.get_plane(index)

    def delete_passenger(self, plane_index, passenger_index):
        self.__planes.delete_passenger(plane_index, passenger_index)

    def delete_plane(self, index):
        self.__planes.delete_plane(index)

    def sort_passengers_by_last_name(self, index):
        self.__planes.sort_passengers_by_last_name(index)

    def sort_planes_by_passenger_number(self):
        self.__planes.sort_planes_by_passenger_number()

    def sort_passengers_name_beginning(self, name_beginning):
        self.__planes.sort_passengers_by_name_beginning(name_beginning)

    def sort_by_concatenation(self):
        self.__planes.sort_by_concatenation()

    def identify_planes_with_first_three(self):
        return self.__planes.identify_planes_with_first_three()

    def check_plane_with_string(self, index, string):
        return self.__planes.check_plane_with_string(index, string)

    def check_planes_by_passengers_with_name(self, name):
        return self.__planes.check_planes_by_passengers_with_name(name)
