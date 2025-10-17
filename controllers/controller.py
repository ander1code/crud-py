from services.connection import ConnectionFactory
from models.models import NaturalPerson

class Controller(object):

    def __init__(self, pp):
        self.__conn = ConnectionFactory.get_connection()
        self.__pp = pp

    def __insert_person(self, name, email):
        try:
            curs = self.__conn.cursor()
            curs.execute(
                "INSERT INTO PERSON (NAME, EMAIL) VALUES (:NAME, :EMAIL)",
                {"NAME": name, "EMAIL": email}
            )
            self.__conn.commit()
            return curs.lastrowid
        except Exception as e:
            print(f"__insert_person error: {e}")
            return -1

    def __insert_natural_person(self, person_id, salary, birthday, gender):
        try:
            curs = self.__conn.cursor()
            curs.execute(
                'INSERT INTO NATURALPERSON (PERSON_ID, SALARY, BIRTHDAY, GENDER) VALUES (:PERSON_ID, :SALARY, :BIRTHDAY, :GENDER)',
                {
                    "PERSON_ID": person_id,
                    "SALARY": salary,
                    "BIRTHDAY": birthday,
                    "GENDER": gender
                }
            )
            return 1
        except Exception as e:
            print(f"__insert_natural_person error: {e}")
            return -1

    def insert_natural_person(self):
        try:
            person_id = self.__insert_person(self.__pp.Name, self.__pp.Email)
            if person_id == -1:
                self.__conn.rollback()
                return -1

            result = self.__insert_natural_person(
                person_id,
                self.__pp.Salary,
                self.__pp.Birthday,
                self.__pp.Gender
            )
            if result != 1:
                self.__conn.rollback()
                return -1

            self.__conn.commit()
            return 1
        except Exception as e:
            print(f"insert_natural_person error: {e}")
            self.__conn.rollback()
            return -1

    def is_email_not_registered(self):
        try:
            curs = self.__conn.cursor()
            curs.execute(
                'SELECT 1 FROM PERSON WHERE EMAIL = :EMAIL LIMIT 1',
                {"EMAIL": self.__pp.Email}
            )
            result = curs.fetchone()
            return result is None  
        except Exception as e:
            print(f"is_email_not_registered error: {e}")
            return False  

    def __edit_person(self, id, name, email):
        try:
            curs = self.__conn.cursor()
            curs.execute(
                "UPDATE PERSON SET NAME = :NAME, EMAIL = :EMAIL WHERE ID = :ID",
                {"NAME": name, "EMAIL": email, "ID": id}
            )
            return 1
        except Exception as e:
            print(f"__edit_person error: {e}")
            return -1

    def __edit_natural_person(self):
        try:
            curs = self.__conn.cursor()
            curs.execute(
                "UPDATE NATURALPERSON SET SALARY = :SALARY, BIRTHDAY = :BIRTHDAY, GENDER = :GENDER WHERE PERSON_ID = :PERSON_ID",
                {
                    "SALARY": self.__pp.Salary,
                    "BIRTHDAY": self.__pp.Birthday,
                    "GENDER": self.__pp.Gender,
                    "PERSON_ID": self.__pp.Id
                }
            )
            return 1
        except Exception as e:
            print(f"__edit_natural_person error: {e}")
            return -1

    def edit_natural_person(self):
        try:
            res_person = self.__edit_person(self.__pp.Id, self.__pp.Name, self.__pp.Email)
            if res_person == -1:
                self.__conn.rollback()
                return -1

            res_natural = self.__edit_natural_person()
            if res_natural == -1:
                self.__conn.rollback()
                return -1

            self.__conn.commit()
            return 1
        except Exception as e:
            print(f"edit_natural_person error: {e}")
            self.__conn.rollback()
            return -1
        
    def get_natural_person_by_id(self):
        query = '''
            SELECT 
                PERSON.ID, PERSON.NAME, PERSON.EMAIL,
                NATURALPERSON.SALARY, NATURALPERSON.BIRTHDAY, NATURALPERSON.GENDER
            FROM PERSON
            INNER JOIN NATURALPERSON ON PERSON.ID = NATURALPERSON.PERSON_ID
            WHERE PERSON.ID = :ID
        '''
        try:
            cursor = self.__conn.cursor()
            cursor.execute(query, {"ID": self.__pp.Id})
            row = cursor.fetchone()
            cursor.close()

            if row is None:
                return None

            return NaturalPerson(
                Id=row[0],
                Name=row[1],
                Email=row[2],
                Salary=row[3],
                Birthday=row[4],
                Gender=row[5]
            )
        except Exception as e:
            print(f"get_natural_person_by_id error: {e}")
            return None

    def __delete_person(self, id):
        try:
            curs = self.__conn.cursor()
            curs.execute('DELETE FROM PERSON WHERE ID = :ID', {"ID": id})
            return 1
        except Exception as e:
            print(f"__delete_person error: {e}")
            return -1

    def __delete_natural_person(self):
        try:
            curs = self.__conn.cursor()
            curs.execute('DELETE FROM NATURALPERSON WHERE ID = :ID', {"ID": self.__pp.Id})
            return 1
        except Exception as e:
            print(f"__delete_natural_person error: {e}")
            return -1

    def delete_natural_person(self):
        try:
            if self.__delete_natural_person() != 1:
                self.__conn.rollback()
                return -1
            if self.__delete_person(self.__pp.Id) != 1:
                self.__conn.rollback()
                return -1
            self.__conn.commit()
            return 1
        except Exception as e:
            print(f"delete_natural_person error: {e}")
            self.__conn.rollback()
            return -1

    def get_natural_person_by_name(self):
        query = '''
            SELECT 
                p.ID, p.NAME, p.EMAIL,
                np.SALARY, np.BIRTHDAY, np.GENDER
            FROM PERSON p
            INNER JOIN NATURALPERSON np ON p.ID = np.PERSON_ID
            WHERE p.NAME LIKE :NAME
        '''
        try:
            curs = self.__conn.cursor()
            curs.execute(query, {"NAME": self.__pp.Name + '%'})
            rows = curs.fetchall()
            curs.close()

            if not rows:
                return []

            people = []
            for row in rows:
                person = NaturalPerson(
                    Id=row[0],
                    Name=row[1],
                    Email=row[2],
                    Salary=row[3],
                    Birthday=row[4],
                    Gender=row[5]
                )
                people.append(person)

            return people

        except Exception as e:
            print(f"get_natural_person_by_name: {e}")
            raise
