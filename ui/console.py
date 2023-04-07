from controller.airline_controller import AirlineController
from data_examples.data_examples import data_examples


def print_menu():
    print("Commands:\n"
          "0 - Exit program.\n"
          "1 - Review commands.\n"
          "2 - View all the planes in the airport.\n"
          "3 - Add new planes in the airport.\n"
          "4 - Add passenger into a plane.\n"
          "5 - Update the data about a passenger.\n"
          "6 - Sort the passengers in a plane by last name.\n"
          "7 - Sort planes according to the number of passengers.\n"
          "8 - Sort planes according to the number of passengers with the first name starting with a given substring.\n"
          "9 - Sort planes according to the string obtained by concatenation of the number of passengers and the destination.\n"
          "10 - Identify  planes  that  have  passengers  with  passport  numbers  starting  with  the  same 3 letters.\n"
          "11 - Identify  passengers  from  a  given  plane  for  which  the  first  name  or  last  name contains a given string.\n"
          "12 - Identify plane/planes where there is a passenger with given name.\n"
          "13 - Identify passengers with passport number.\n"
          "14 - Form groups of k passengers from the same plane but with different last names.\n"
          "15 - Form  groups  of  k  planes  with  the  same  destination  but  belonging  to  different.\n"
          "16 - Delete passenger with passport number.\n")


def start():
    print_menu()
    planes = AirlineController(data_examples())
    command = -1
    while command != 0:
        try:
            command = int(input("Enter command: "))

            if command == 1:
                print_menu()

            elif command == 2:
                print(planes)

            elif command == 3:
                plane_number = int(input("Enter plane number: "))
                company = str(input("Enter plane company: "))
                seat_number = int(input("Enter number of seats: "))
                destination = str(input("Enter destination: "))
                planes.add_plane(plane_number, company, seat_number, destination, [])

            elif command == 4:
                index = int(input("Enter passenger in plane with index: "))
                first_name = str(input("Enter first name of the passenger: "))
                last_name = str(input("Enter last name of the passenger: "))
                passport_number = int(input("Enter passport number: "))
                planes.add_passenger(index, first_name, last_name, passport_number)

            elif command == 5:
                plane_index = int(input("Update passenger from plane with index: "))
                passenger_index = int(input("Passenger index: "))
                print("Which one would you like to update?\n"
                      "1 - First name\n"
                      "2 - Last name\n"
                      "3 - Passport number\n")
                command_2 = int(input("Enter update choice: "))
                if command_2 == 1:
                    first_name = str(input("Enter new first name: "))
                    planes.get_plane(plane_index).update_passenger_first_name(passenger_index, first_name)
                elif command_2 == 2:
                    last_name = str(input("Enter new first name: "))
                    planes.get_plane(plane_index).update_passenger_last_name(passenger_index, last_name)
                elif command_2 == 3:
                    passport_number = int(input("Enter new passport number: "))
                    planes.get_plane(plane_index).update_passenger_passport_number(passenger_index, passport_number)

            elif command == 6:
                index = int(input("Enter plane index: "))
                planes.sort_passengers_by_last_name(index)

            elif command == 7:
                planes.sort_planes_by_passenger_number()

            elif command == 8:
                name_beginning = str(input("Enter name beginning: "))
                planes.sort_passengers_name_beginning(name_beginning)

            elif command == 9:
                planes.sort_by_concatenation()

            elif command == 10:
                print(planes.identify_planes_with_first_three())

            elif command == 11:
                string = str(input("Enter string: "))
                index = int(input("Enter plane index: "))
                print(planes.check_plane_with_string(index, string))

            elif command == 12:
                name = str(input("Enter name: "))
                print(planes.check_planes_by_passengers_with_name(name))

            elif command == 13:
                index = int(input("Enter plane index: "))
                passport_number = int(input("Enter passport number: "))
                print(planes.get_plane(index).get_passenger(passport_number))

            elif command == 14:
                pass

            elif command == 15:
                pass

            elif command == 16:
                index = int(input("Enter plane index: "))
                passport_number = int(input("Enter passport number: "))
                planes.get_plane(index).delete_passenger(passport_number)
        except IndexError as ie:
            print(ie)
        except AttributeError as ae:
            print(ae)
        except ValueError as ve:
            print(ve)
