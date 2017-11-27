import exceptions
import sys
from classes import *

def PrintMessage(method, result):
    if(method == 1):
        if(result == 1):
            print "Successfully registered."
        if(result == -1):
            print "Error registering."

    if(method == 2):
        if(result == 1):
            print "Edited successfully."
        if(result == -1):
            print "Error editing."

    if(method == 3):
        if(result == 1):
            print "Deleted successfully."
        if(result == -1):
            print "Error deleting."


def InsertPhysicalPerson():
    print "----------------------------------------|"
    print "INSERT PHYSICAL PERSON                  |"
    print "----------------------------------------|"
    try:
         name = raw_input("Name: ")
         email = raw_input("Email: ")
         salary = raw_input("Salary: ")
         birthday = raw_input("Birthday (YYYY-MM-DD): ")
         gender = raw_input("GENDER (M or F): ")
         
         try:
             result = Crud.Insert_PhysicalPerson(name, email, salary, birthday, gender)
         except exceptions.Exception as e:
             print e.message
         
         print "\n----------------------------------------|"
         PrintMessage(1, result)
         print "----------------------------------------|\n\n"
    except:
      print "Error in data entry."
    print "----------------------------------------|"
    
def EditPhysicalPerson():
    print("\n\n----------------------------------------|")
    print("EDIT PHYSICAL PERSON                    |")
    print("----------------------------------------|")
    try:
        id = input("ID: ")
        pp = Crud.Get_PhysicalPersonForID(id)
        if pp:
            print "----------------------------------------|"
            print "RECORD WITH ID = {0}".format(id)
            print "Name: {0}".format(pp.Name)
            print "Email: {0}".format(pp.Email) 
            print "Birthday: {0}".format(pp.Birthday) 
            print "Salary: {0}".format(pp.Salary) 
            print "Gender: {0}".format(pp.Gender) 
            print "----------------------------------------|"
            try:
                name = raw_input("Name: ")
                email = raw_input("Email: ")
                salary = input("Salary: ")
                birthday = raw_input("Birthday (YYYY-MM-DD): ")
                gender = raw_input("GENDER (M or F): ")
                result = Crud.Edit_PhysicalPerson(id, name, email, salary, birthday, gender)
                print("\n----------------------------------------|")
                PrintMessage(2, result)
                print("----------------------------------------|\n\n")
            except:
                print "\n\nError in data entry.\n\n"
        else:
            print "\n\nNo records found with this ID.\n\n"
    except:
        pass

def DeletePhysicalPerson():
    print "----------------------------------------|"
    print "DELETE PHYSICAL PERSON                  |"
    print "----------------------------------------|"
    id = input("ID: ")
    pp = Crud.Get_PhysicalPersonForID(id)
    if pp:
        print "----------------------------------------|"
        print "RECORD WITH ID = {0}".format(id)
        print "Name: {0}".format(pp.Name)
        print "Email: {0}".format(pp.Email) 
        print "Birthday: {0}".format(pp.Birthday) 
        print "Salary: {0}".format(pp.Salary) 
        print "Gender: {0}".format(pp.Gender) 
        print "----------------------------------------|"
        try:
            opc = raw_input("\nDo you want delete this record? (1 - Yes or 0 - No): ")
            if opc == '1':
               result = Crud.Delete_PhysicalPerson(id)
               print("\n----------------------------------------|")
               PrintMessage(3, result)
            else:
               print "No record deleted."
            print("----------------------------------------|\n\n")
        except Exception as e:
           print "Error in data entry."
    else:
        print "No records found with this ID."

def Get_PhysicalPersonForName():
    print "----------------------------------------|"
    print "GET PHYSICAL PERSON BY NAME             |"
    print "----------------------------------------|"
    try:
        name = input("Name: ")
    except  :
        name = ''
    listpp = Crud.Get_PhysicalPersonForName(name)
    if listpp:
        print("\n----------------------------------------|")
        print("PHYSICAL PERSONS FOUND:                 |")
        print("----------------------------------------|")
        for pp in listpp:
            print "ID = {0}".format(pp.Id)
            print "Name: {0}".format(pp.Name)
            print "Email: {0}".format(pp.Email) 
            print "Birthday: {0}".format(pp.Birthday) 
            print "Salary: {0}".format(pp.Salary) 
            print "Gender: {0}".format(pp.Gender) 
            print("----------------------------------------|\n")
    else:
        print "No records found with this NAME."
        print("----------------------------------------|\n\n\n")

def Get_PhysicalPersonForID():
    print "\n\n----------------------------------------|"
    print "GET PHYSICAL PERSON BY ID               |"
    print "----------------------------------------|"
    try:
        id = input("ID: ")
        print("----------------------------------------|")
        pp = Crud.Get_PhysicalPersonForID(id)
        if pp:
            print "ID: {0}".format(id)
            print "Name: {0}".format(pp.Name)
            print "Email: {0}".format(pp.Email) 
            print "Birthday: {0}".format(pp.Birthday) 
            print "Salary: {0}".format(pp.Salary) 
            print "Gender: {0}".format(pp.Gender) 
        else:
            print "No records found with this ID."
    except:
        print "No valid ID was entered."
    print("----------------------------------------|\n\n\n")
   

##############################################################

def CallMethod():
    if opc == 1:
        InsertPhysicalPerson()
    if opc == 2:
        EditPhysicalPerson()
    if opc == 3:
        DeletePhysicalPerson()
    if opc == 4:
        Get_PhysicalPersonForName()
    if opc == 5:
        Get_PhysicalPersonForID()
    if opc == 0:
        sys.exit(0)

opc = 1
while opc <> 0:
    print("########################################|")
    print(" REGISTRATION PHYSICAL PERSON           |")
    print("########################################|")
    print(" 1 - INSERT PHYSICAL PERSON             |")
    print(" 2 - EDIT PHYSICAL PERSON               |")
    print(" 3 - DELETE PHYSICAL PERSON             |")
    print(" 4 - GET PHYSICAL PERSON BY NAME        |")
    print(" 5 - GET PHYSICAL PERSON BY ID          |")
    print(" 0 - FINISH                             |")
    print("########################################|\n")
    try:
        opc = input("Enter your option: ")
        if opc == 1:
            InsertPhysicalPerson()
        if opc == 2:
            EditPhysicalPerson()
        if opc == 3:
            DeletePhysicalPerson()
        if opc == 4:
            Get_PhysicalPersonForName()
        if opc == 5:
            Get_PhysicalPersonForID()
        if opc == 0:
            sys.exit(0)
    except:
        print "Finish."
        sys.exit(0)