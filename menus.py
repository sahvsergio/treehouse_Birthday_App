import utils
import functions


def main_menu():
    try:
        print("======== MENU ========")
        print("1 - See upcoming Birthdays")
        print("2 - Check a someone's age")
        print("3 - Compare two people's ages")
        print("4 - Quit the app")
        print("======================")
        choice = input("What would you like to do? ")
        if choice not in ["1", "2", "3", "4"]:
            raise utils.MenuOptionError
        return int(choice)
    except utils.MenuOptionError:
        utils.format_error("That is not a valid menu option, please try again!")


def back_to_main_menu():
    input("Press any key to return to main menu...")


def upcoming_birthdays_menu(people_list):
    print("\n======== UPCOMING BIRTHDAYS ========")
    functions.upcoming_birthdays(people_list, 90)
    print("====================================\n")
    back_to_main_menu()


def check_ages_menu(people_list):
    print("\n======== CHECK AGE ========")
    # Define and start the loop
    running = True
    while running:
        utils.list_people(people_list)
        try:
            print("Who's age do you want to check? ")

            # Cast input to integer. If not an integer, it'll raise ValueError
            person_index = int(input("Please enter their ID: "))

            # Grab person by index. If invalid, it'll raise IndexError
            person = people_list[person_index]

            # Call function to display person's age
            functions.display_age(person)

            # Stop the loop
            running = False
        except ValueError:
            utils.format_error("That's not a valid input. Please enter an ID of a person")
        except IndexError:
            utils.format_error("That ID doesn't exist. Please enter an ID of a person")

    print("\n=======================")
    back_to_main_menu()


def age_difference_menu(people_list):
    print("\n======== CHECK AGE DIFFERENCE ========")
    running = True
    while running:
        utils.list_people(people_list)
        try:
            print("Who's ages do you want to compare?'")
            print("Please enter their IDs with a space in between: ")
            input_indexes = input("For example, '4 5': ")

            # first check if there are 2. If there is more/less than 2, it'll raise the MenuOptionError
            if len(input_indexes.split(' ')) != 2:
                raise utils.MenuOptionError

            # then cast them to int. If any are not integers it'll raise the ValueError
            indexes = [int(index) for index in input_indexes.split()]

            # Grab people by indexes. If any are invalid it'll raise the Index Error
            people = [people_list[index] for index in indexes]

            # Display the age of selected people
            functions.display_age(people[0])
            functions.display_age(people[1])

            # Display the age difference
            functions.display_age_difference(people)

            # Stop the loop
            running = False
        except ValueError:
            utils.format_error("One or more of the inputted values were not valid")
        except IndexError:
            utils.format_error("One or more of the inputted IDs were not valid")
        except utils.MenuOptionError:
            utils.format_error("There must be exactly 2 IDs")

    print("===================================\n")
    back_to_main_menu()

