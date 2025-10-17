import sys
from services.crud import Crud
from utils.validations import *

def show_message(method, result):
    messages = {
        1: ("Successfully registered.", "Error registering."),
        2: ("Edited successfully.", "Error editing."),
        3: ("Deleted successfully.", "Error deleting.")
    }
    success, error = messages.get(method, ("Operation succeeded.", "Operation failed."))
    print(success if result == 1 else error)

def insert_natural_person():
    print("----------------------------------------|")
    print("INSERT NATURAL PERSON                   |")
    print("----------------------------------------|")
    try:
        try:
            data = input_data()
            crud = Crud()
            result = crud.insert_natural_person(data['name'], data['email'], data['salary'], data['birthday'], data['gender'])
        except Exception as e:
            print(f"Exception: {e}")
            result = -1

        print("\n----------------------------------------|")
        show_message(1, result)
        print("----------------------------------------|\n\n")
    except Exception:
        print("Error in data entry.")
    print("----------------------------------------|")


def input_data():
    while True:
        name = input("Name: ")
        error = validate_name(name)
        if error:
            print("Error:", error)
        else:
            break

    while True:
        email = input("Email: ")
        error = validate_email(email)
        if error:
            print("Error:", error)
        else:
            break

    while True:
        salary = input("Salary: ")
        error = validate_salary(salary)
        if error:
            print("Error:", error)
        else:
            salary = float(salary) 
            break

    while True:
        birthday = input("Birthday (YYYY-MM-DD): ")
        error = validate_birthday(birthday)
        if error:
            print("Error:", error)
        else:
            break

    while True:
        gender = input("Gender (M or F): ")
        error = validate_gender(gender)
        if error:
            print("Error:", error)
        else:
            break

    return {
        'name': name,
        'email': email,
        'salary': salary,
        'birthday': birthday,
        'gender': gender
    }

def input_edit_data(pp):
    def get_input(label, current, validator=None, cast_func=None, validate_if_filled=True):
        while True:
            user_input = input(f"{label} [{current}]: ").strip()
            if not user_input:
                return current
            if validator and validate_if_filled:
                error = validator(user_input)
                if error:
                    print("Error:", error)
                    continue
            return cast_func(user_input) if cast_func else user_input

    name = get_input("Name", pp.Name, validate_name)
    email = get_input("Email", pp.Email, validate_email, validate_if_filled=True)
    salary = get_input("Salary", pp.Salary, validate_salary, float)
    birthday = get_input("Birthday (YYYY-MM-DD)", pp.Birthday, validate_birthday)
    gender = get_input("Gender (M or F)", pp.Gender, validate_gender)

    return {
        'name': name,
        'email': email,
        'salary': salary,
        'birthday': birthday,
        'gender': gender
    }

def show_natural_person(pp):
    print("\n" + "-" * 100)
    print("| {:^10} | {:^20} | {:^25} | {:^12} | {:^10} | {:^8} |".format(
        "ID", "Name", "Email", "Birthday", "Salary", "Gender"
    ))
    print("-" * 100)
    print("| {:<10} | {:<20} | {:<25} | {:<12} | {:>10} | {:^8} |".format(
        pp.Id, pp.Name, pp.Email, str(pp.Birthday), str(pp.Salary), pp.Gender
    ))
    print("-" * 100 + "\n")


def edit_natural_person():
    print("\n" + "-" * 40)
    print("EDIT NATURAL PERSON")
    print("-" * 40)

    try:
        person_id = input("Enter ID: ").strip()
        pp = Crud().get_natural_person_by_id(int(person_id))

        if pp:
            show_natural_person(pp)
            try:
                data = input_edit_data(pp)
                crud = Crud()
                result = crud.edit_natural_person(person_id, data['name'], data['email'], data['salary'], data['birthday'], data['gender'])
                print("\n" + "-" * 40)
                show_message(2, result)
                print("-" * 40 + "\n")
            except Exception as entry_error:
                print(f"\nError during data entry: {entry_error}\n")
        else:
            print("\nNo records found with this ID.\n")
    except Exception as e:
        print(f"\nUnexpected error: {e}\n")


def delete_natural_person():
    print("----------------------------------------|")
    print("DELETE NATURAL PERSON                  |")
    print("----------------------------------------|")
    try:
        id = input("ID: ")
        pp = Crud().get_natural_person_by_id(id)
        if pp:
            show_natural_person(pp)
            opc = input("\nDo you want to delete this record? (1 - Yes or 0 - No): ")
            if opc == '1':
                result = Crud().delete_natural_person(id)
                print("\n----------------------------------------|")
                show_message(3, result)
            else:
                print("No record deleted.")
            print("----------------------------------------|\n\n")
        else:
            print("No records found with this ID.")
    except Exception:
        print("Error in data entry.")

def get_natural_person_by_name():
    print("----------------------------------------|")
    print("GET NATURAL PERSON BY NAME             |")
    print("----------------------------------------|")
    try:
        name = input("Name: ")
        listpp = Crud().get_natural_person_by_name(name)
        if listpp:
            print("\n----------------------------------------|")
            print("NATURAL PERSONS FOUND:                 |")
            print("----------------------------------------|")
            for pp in listpp:
                show_natural_person(pp)
                print("----------------------------------------|\n")
        else:
            print("No records found with this NAME.")
            print("----------------------------------------|\n\n\n")
    except Exception as error:
        print("Error during search.")

def get_natural_person_by_id():
    print("\n\n----------------------------------------|")
    print("GET NATURAL PERSON BY ID               |")
    print("----------------------------------------|")
    try:
        id = input("ID: ")
        pp = Crud().get_natural_person_by_id(id)
        print("----------------------------------------|")
        if pp:
            show_natural_person(pp)
        else:
            print("No records found with this ID.")
    except Exception:
        print("No valid ID was entered.")
    print("----------------------------------------|\n\n\n")


# Menu principal
def main():
    while True:
        print("########################################|")
        print(" REGISTRATION NATURAL PERSON           |")
        print("########################################|")
        print(" 1 - INSERT NATURAL PERSON             |")
        print(" 2 - EDIT NATURAL PERSON               |")
        print(" 3 - DELETE NATURAL PERSON             |")
        print(" 4 - GET NATURAL PERSON BY NAME        |")
        print(" 5 - GET NATURAL PERSON BY ID          |")
        print(" 0 - FINISH                             |")
        print("########################################|\n")
        try:
            opc = int(input("Enter your option: "))
            if opc == 1:
                insert_natural_person()
            elif opc == 2:
                edit_natural_person()
            elif opc == 3:
                delete_natural_person()
            elif opc == 4:
                get_natural_person_by_name()
            elif opc == 5:
                get_natural_person_by_id()
            elif opc == 0:
                print("Exiting...")
                sys.exit(0)
            else:
                print("Invalid option. Please try again.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Exiting...")
            sys.exit(0)

if __name__ == "__main__":
    main()
