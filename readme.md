Birthday App
---

### Introduction
Welcome to the birthday app! When the app is run, it loads data from `birthdays.csv`, and users get presented with a menu.

Users can:
- See upcoming Birthdays, which are birthdays within the next 90 days
- Check someone's age by entering their ID as prompted
- Compare two people's ages by entering their IDs as prompted
- Quit the app

Much of the logic and navigation of the app has already been written by other developers of your team. Your job is to complete the `datetime` related functions of the app. It is recommended to explore the files and run the app to see what has already been done, and what data you have to work with.

### Getting started:
1. Create a virtual environment for this project
2. Install `dateutil` (the PPI name is `python-dateutil`!)
3. Tackle the three `datetime` related functions below

### Your mission, should you choose to accept it:
1. `display_age()` in `functions.py`
2. `display_age_differences()` in `functions.py`
3. `upcoming_birthdays()` in `functions.py`

### Extra challenges
- Create a helper function that determines the age, which both `display_age()` and `upcoming_birthdays()` can use.
- Create a helper function that takes the date string and returns a datetime object (all 3 functions can use this!)
- List the upcoming birthdays chronologically
- Try to handle plural cases! Create a function in `utils.py` that will determine whether we print plural words or singular words. For example, "0 months", "1 month", "2 months".
- Handle upcoming birthdays for the following year
---

Created for the [Team Treehouse](https://teamtreehouse.com/) Python Dates and Times (2023) course