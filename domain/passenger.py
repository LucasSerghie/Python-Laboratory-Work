class Passenger:
    """
    Represents a passenger which has the following attributes:
            -first name
            -last name
            -passport number
    The class could raise several error in it's methods
    """

    def __init__(self, first_name='', last_name='', passport_number=0):
        """
        Creates a new instance of a passenger
        :param first_name: first name of the passenger
        :param last_name: last name of the passenger
        :param passport_number: passport number of the passenger
        """
        if len(first_name) > 0:
            self.__first_name = first_name
        else:
            raise AttributeError("Please enter a first name.")

        if len(last_name) > 0:
            self.__last_name = last_name
        else:
            raise AttributeError("Please enter a last name.")

        if passport_number > 0:
            self.__passport_number = passport_number
        else:
            raise AttributeError("Passport number has to be greater than 0.")

    def __str__(self):
        """
        :return: The string representation of a vector
        """
        return (
            f"Passenger name: {self.__first_name} {self.__last_name} with passport number {self.__passport_number}.")

    def __eq__(self, other):
        """
        Defines if two passengers are equal or not
        :param other: other vector to be equal to
        :return: boolean value true if equal, false if not
        """
        return self.__first_name == other.__first_name and \
               self.__last_name == other.__last_name and \
               self.__passport_number == other.__passport_number

    def get_first_name(self):
        """
        Get first name
        :return:
        """
        return self.__first_name

    def get_last_name(self):
        """
        Get last name
        :return:
        """
        return self.__last_name

    def get_passport_number(self):
        """
        Get passport number
        :return:
        """
        return self.__passport_number

    def update_first_name(self, new_first_name):
        """
        Update first name
        :param new_first_name:
        :return:
        """
        if len(new_first_name) > 0:
            self.__first_name = new_first_name
        else:
            raise AttributeError("Please enter a first name.")

    def update_last_name(self, new_last_name):
        """
        Update last name
        :param new_last_name:
        :return:
        """
        if len(new_last_name) > 0:
            self.__last_name = new_last_name
        else:
            raise AttributeError("Please enter a last name.")

    def update_passport_number(self, new_passport_number):
        """
        Update passport number
        :param new_passport_number:
        :return:
        """
        if new_passport_number > 0:
            self.__passport_number = new_passport_number
        else:
            raise AttributeError("Passport number has to be greater than 0.")

    def check_first_characters(self):
        """
        Check if passport number starts with the same three numbers
        :return: true if it does, false if not
        """
        if str(self.__passport_number)[0] == str(self.__passport_number)[1] == str(self.__passport_number)[2]:
            return True
        return False

    def check_string_containing(self, string):
        """
        Check if first name or last name contains a given string
        :param string:
        :return: true if it does, false if not
        """
        string = str(string).lower()
        if string in self.__first_name.lower() or string in self.__last_name.lower():
            return True
        return False

    def check_first_name(self, name):
        """
        Check if first name is equal to a given name
        :param name:
        :return: true if it does, false if not
        """
        name = str(name).lower()
        if self.__first_name.lower() == name:
            return True
        return False

    def check_name(self, name):
        """
        Check if first name or last name are equal to a given name
        :param name:
        :return: true if it does, false if not
        """
        name = str(name).lower()
        if self.__first_name.lower() == name or self.__last_name.lower() == name:
            return True
        return False
