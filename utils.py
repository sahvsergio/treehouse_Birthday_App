class MenuOptionError(Exception):
    """Raised when an invalid menu option is used"""
    pass


def list_people(people_list):
    print("Here is a list of people and their IDs")
    for index, person in enumerate(people_list):
        print(f'{index} - {person["name"]}')
    pass


def format_error(error_message):
    print("\n#### ERROR ####")
    print(error_message)
    print("###############\n")
