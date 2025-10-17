from models.models import NaturalPerson
from controllers.controller import Controller

class Crud:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Crud, cls).__new__(cls)
        return cls._instance

    def insert_natural_person(self, name, email, salary, birthday, gender):
        pp = NaturalPerson()
        pp.Name = name
        pp.Email = email
        pp.Salary = salary
        pp.Birthday = birthday
        pp.Gender = gender
        ctr = Controller(pp)
        result = ctr.insert_natural_person()
        return 1 if result == 1 else -1

    def edit_natural_person(self, id, name, email, salary, birthday, gender):
        pp = NaturalPerson()
        pp.Id = id
        pp.Name = name
        pp.Email = email
        pp.Salary = salary
        pp.Birthday = birthday
        pp.Gender = gender
        ctr = Controller(pp)
        result = ctr.edit_natural_person()
        return 1 if result == 1 else -1
    
    def delete_natural_person(self, id):
        pp = NaturalPerson()
        pp.Id = id
        ctr = Controller(pp)
        result = ctr.delete_natural_person()
        return 1 if result == 1 else -1
    
    def get_natural_person_by_id(self, id):
        pp = NaturalPerson()
        pp.Id = id
        ctr = Controller(pp)
        return ctr.get_natural_person_by_id()
    
    def get_natural_person_by_name(self, name):
        pp = NaturalPerson()
        pp.Name = name
        ctr = Controller(pp)
        return ctr.get_natural_person_by_name()

    def is_email_not_registered(self, email):
        pp = NaturalPerson()
        pp.Email = email
        ctr = Controller(pp)
        return ctr.is_email_not_registered()