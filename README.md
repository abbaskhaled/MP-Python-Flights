# Fork & Clone

Fork and clone [this repository](https://github.com/JoinCODED/MP-Python-Flights) in your `python` directory.

---

# Task

In this task, you'll be creating the Passengers system for an airline. This airline has two types of people: passengers and captains.

Here is an example of what the output would look like:

```
Welcome to CODED Airline.
Options:
1. Show persons
2. Show captains
3. Add person
4. Add captain
Choose a number:1
Name: Laila, Age: 23, Passport: 854534, Bags: 2, Destination: Japan
Name: Shereen, Age: 25, Passport: 9876542, Bags: 3, Destination: Germany

------------

Welcome to CODED Airline.
Options:
1. Show persons
2. Show captains
3. Add person
4. Add captain
Choose a number:2
Name: Mohammad, Age: 25, Passport: 54645, Experience Years: 4, Salary: 5555
Name: Sara, Age: 29, Passport: 84395, Experience Years: 9, Salary: 7000

-----------

Welcome to CODED Airline.
Options:
1. Show persons
2. Show captains
3. Add person
4. Add captain
Choose a number:3
Name: Laila
Age: 33
Passport Numbers: 4354
Num of Bags: 3
Destination: Kuwait
Name: Laila, Age: 33, Passport: 4354, Bags: 3, Destination: Kuwait


--------

Welcome to CODED Airline.
Options:
1. Show persons
2. Show captains
3. Add person
4. Add captain
Choose a number:4
Name: Abdallah
Age: 44
Passport Numbers: 976665
Experience Years: 3
Salary: 3333
Name: Abdallah, Age: 44, Passport: 976665, Experience Years: 3, Salary: 3333

```

## Steps:

1.  In this task you need to create three classes:

    a. `Person` class:

        - `name`
        - `age`
        - `passport_number`

    b. `Passenger` class:

        - Where the `Passenger` class inherits from the `Person` class.
        - `name`
        - `age`
        - `passport_number`
        - `number_of_bags`
        - `destination`
        - `get_bag_weight()`:
        	- Every bag's weight is 23KG
        	- Return the total weight for this passenger (number of bags \* 23)
        - Add an `__str` method that prints the `name`, `age`, `passport_number`, `number_of_bags` and `destination`.

    c. `Captain`:

        - Where the `Captain` class inherits from the `Person` class.
        - `name`
        - `age`
        - `passport_number`
        - `experience_years`
        - `salary`
        - `get_bonus()`:
        	- Every year of experience gives 1% bonus, example: if captain has five years of experience, his bonus will be 5% (`5/100`) multiplied by his salary.
        	- Return the bonus ((experience years /100) \* salary)
        - Add an `__str` method that prints the `name`, `age`, `passport_number`, `experience_years` and `salary`.

2.  Define a list of two `Passenger` objects.
3.  Create a list of two `Captain` objects.
4.  Print the following options to the airline user. It doesn't need to be a list, just regular prints.

    ```shell
    Welcome to CODED Airline.
    Options:
    	1. Show persons
    	2. Show captains
    	3. Add person
    	4. Add captain
    Choose a number:
    ```

5.  If `1` was chosen, print the passengeres information (the passengeres list).
6.  If `2` was chosen, print the captains information (the captains list).
7.  If `3` was chosen, allow the user to create a passenger and then add it to the system (the passengers list).
8.  If `4` was chosen, allow the user to create a captain and then add it to the system (the captains list).
9.  Push your code.
