from physicalperson import PhysicalPerson
from controller import Controller

class Crud(object):

    @staticmethod
    def Insert_PhysicalPerson(name, email, salary, birthday, gender):
        pp = PhysicalPerson()
        pp.Name = name
        pp.Email = email
        pp.Salary = salary
        pp.Birthday = birthday
        pp.Gender = gender
        ctr = Controller(pp)
        result = ctr.Insert_PhysicalPerson()
        if result == 1:
            return 1
        else:
            return -1

    @staticmethod
    def Edit_PhysicalPerson(id, name, email, salary, birthday, gender):
        pp = PhysicalPerson()
        pp.Id = id
        pp.Name = name
        pp.Email = email
        pp.Salary = salary
        pp.Birthday = birthday
        pp.Gender = gender
        ctr = Controller(pp)
        result = ctr.Edit_PhysicalPerson()
        if result == 1:
            return 1
        else:
            return -1

    @staticmethod
    def Delete_PhysicalPerson(id):
        pp = PhysicalPerson()
        pp.Id = id
        ctr = Controller(pp)
        result = ctr.Delete_PhysicalPerson()
        if result == 1:
            return 1
        else:
            return -1

    @staticmethod
    def Get_PhysicalPersonForID(id):
        pp = PhysicalPerson()
        pp.Id = id
        ctr = Controller(pp)
        result = ctr.Get_PhysicalPersonForID()
        return result

    @staticmethod
    def Get_PhysicalPersonForName(name):
        pp = PhysicalPerson()
        pp.Name = name
        ctr = Controller(pp)
        result = ctr.Get_PhysicalPersonForName()
        return result
