from person import Person

class PhysicalPerson(Person):
    @property 
    def Id(self):
        return self.id
    @Id.setter
    def Id(self, id):
        self.id = id
    @property
    def Name(self):
        return self.name
    @Name.setter
    def Name(self, name):
        self.name = name
    @property
    def Email(self):
        return self.email
    @Email.setter
    def Email(self, email):
        self.email = email
    @property
    def Salary(self):
        return self.salary
    @Salary.setter
    def Salary(self, salary):
        self.salary = salary
    @property
    def Birthday(self):
        return self.birthday
    @Birthday.setter
    def Birthday(self, birthday):
        self.birthday = birthday
    @property
    def Gender(self):
        return self.gender
    @Gender.setter
    def Gender(self, gender):
        self.gender = gender