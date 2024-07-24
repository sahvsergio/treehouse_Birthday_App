import csv
import menus


if __name__ == '__main__':
    PEOPLE = []
    print("WELCOME TO THE BIRTHDAY DATABASE APP")
    print("Loading data...")
    with open('birthdays.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            PEOPLE.append({
                'name': row['name'],
                'birthday': row['birthday']
            })
    menu_choice = 0
    while menu_choice != 4:
        menu_choice = menus.main_menu()
        if menu_choice == 1:
            menus.upcoming_birthdays_menu(PEOPLE)
        if menu_choice == 2:
            menus.check_ages_menu(PEOPLE)
        if menu_choice == 3:
            menus.age_difference_menu(PEOPLE)
    print("Have a great day!")
