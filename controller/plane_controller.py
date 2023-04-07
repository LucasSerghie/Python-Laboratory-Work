from infrastructure.plane import Plane


class PlaneController:
    def __init__(self, plane_number=0, company='', seats_number=0, destination='', list_of_passengers=None):
        self.__plane = Plane(plane_number, company, seats_number, destination, list_of_passengers)

    def __str__(self):
        return str(self.__plane)

    def get_passenger(self, passport_number):
        return self.get_passenger(passport_number)

    def add_passenger(self, new_first_name, new_last_name, new_passport_number):
        self.__plane.add_passenger(new_first_name, new_last_name, new_passport_number)

    def update_passenger_first_name(self, index, new_first_name):
        self.__plane.update_passenger_first_name(index, new_first_name)

    def update_passenger_last_name(self, index, new_last_name):
        self.__plane.update_passenger_last_name(index, new_last_name)

    def update_passenger_passport_number(self, index, new_passport_number):
        self.__plane.update_passenger_passport_number(index, new_passport_number)

    def get_plane_number(self):
        return self.__plane.get_plane_number()

    def get_company(self):
        return self.__plane.get_company()

    def get_seats_number(self):
        return self.__plane.get_seats_number()

    def get_destination(self):
        return self.__plane.get_destination()

    def get_list_of_passengers(self):
        return self.__plane.get_list_of_passengers()

    def update_company(self, new_company):
        self.__plane.update_company(new_company)

    def update_seats_number(self, new_seats_number):
        self.__plane.update_seats_number(new_seats_number)

    def update_destination(self, new_destination):
        self.__plane.update_destination(new_destination)

    def delete_passenger(self, passport_number):
        self.__plane.delete_passenger(passport_number)
