from abc import ABC, abstractmethod

class Person(ABC):
    @property
    @abstractmethod
    def Id(self):
        pass

    @Id.setter
    @abstractmethod
    def Id(self, value):
        pass

    @property
    @abstractmethod
    def Name(self):
        pass

    @Name.setter
    @abstractmethod
    def Name(self, value):
        pass

    @property
    @abstractmethod
    def Email(self):
        pass

    @Email.setter
    @abstractmethod
    def Email(self, value):
        pass


class NaturalPerson(Person):
    def __init__(self, Id=None, Name=None, Email=None, Salary=None, Birthday=None, Gender=None):
        self._id = Id
        self._name = Name
        self._email = Email
        self._salary = Salary
        self._birthday = Birthday
        self._gender = Gender

    @property
    def Id(self):
        return self._id

    @Id.setter
    def Id(self, value):
        self._id = value

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, value):
        self._name = value

    @property
    def Email(self):
        return self._email

    @Email.setter
    def Email(self, value):
        self._email = value

    @property
    def Salary(self):
        return self._salary

    @Salary.setter
    def Salary(self, value):
        self._salary = value

    @property
    def Birthday(self):
        return self._birthday

    @Birthday.setter
    def Birthday(self, value):
        self._birthday = value

    @property
    def Gender(self):
        return self._gender

    @Gender.setter
    def Gender(self, value):
        self._gender = value
