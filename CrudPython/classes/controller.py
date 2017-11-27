import connection
import sqlite3
from physicalperson import PhysicalPerson
from connection import Connection

class Controller(object):

    def __init__(self, pp):
        self.conn = Connection.Connect()
        self.pp = pp

    def GeneratorID(self):
        try:
            sql = 'SELECT MAX(ID) + 1 FROM PERSON'
            curs = self.conn.cursor()
            curs.execute(sql)
            try:
                return curs.fetchone()[0]
            except:
                return 1
        except:
            return -1

    def InsertPerson(self, id, name, email):
        try:
            curs = self.conn.cursor()
            curs.execute("INSERT INTO PERSON (ID,NAME,EMAIL) VALUES (:ID,:NAME,:EMAIL)", {"ID":id,"NAME":name,"EMAIL":email})
            return 1
        except:
            return -1

    def InsertPhysicalPerson(self):
        try:
            curs = self.conn.cursor()
            curs.execute('INSERT INTO PHYSICALPERSON (ID, PERSON_ID, SALARY, BIRTHDAY, GENDER) VALUES (:ID, :ID, :SALARY, :BIRTHDAY, :GENDER)', {"ID":self.pp.Id ,"ID":self.pp.Id,"SALARY":self.pp.Salary,"BIRTHDAY":self.pp.Birthday,"GENDER":self.pp.Gender})
            return 1
        except:
            return -1

    def Insert_PhysicalPerson(self):
        id = self.GeneratorID()
        if (id > 0):
            self.pp.Id = id
            if (self.InsertPerson(self.pp.Id, self.pp.Name, self.pp.Email) == 1):
                if (self.InsertPhysicalPerson() == 1):
                    self.conn.commit()
                    self.conn.close()
                    return 1
                else:
                    self.conn.rollback()
                    self.conn.close()
                    return -1
            else:
                self.conn.rollback()
                self.conn.close()
                return -1
        else:
            self.conn.close()
            return -1

    def EditPerson(self, id, name, email):
        try:
            curs = self.conn.cursor()
            curs.execute("UPDATE PERSON SET NAME = :NAME, EMAIL = :EMAIL WHERE ID = :ID", {"NAME":name,"EMAIL":email,"ID":id})
            return 1
        except:
            return -1

    def EditPhysicalPerson(self):
        try:
            curs = self.conn.cursor()
            curs.execute('UPDATE PHYSICALPERSON SET SALARY = :SALARY, BIRTHDAY = :BIRTHDAY, GENDER = :GENDER WHERE ID = :ID', {"SALARY":self.pp.Salary, "BIRTHDAY":self.pp.Birthday, "GENDER":self.pp.Gender, "ID":self.pp.Id})
            return 1
        except:
            return -1

    def Edit_PhysicalPerson(self):
        if (self.EditPerson(self.pp.Id, self.pp.Name, self.pp.Email) == 1):
            if (self.EditPhysicalPerson() == 1):
                self.conn.commit()
                self.conn.close()
                return 1
            else:
                self.conn.rollback()
                self.conn.close()
                return -1
        else:
            self.conn.rollback()
            self.conn.close()
            return -1

    def DeletePerson(self, id):
        try:
            curs = self.conn.cursor()
            curs.execute('DELETE FROM PERSON WHERE ID = :ID', {"ID":id})
            return 1
        except:
            return -1

    def DeletePhysicalPerson(self):
        try:
            curs = self.conn.cursor()
            curs.execute('DELETE FROM PHYSICALPERSON WHERE ID = :ID', {"ID":self.pp.Id})
            return 1
        except Exception as e:
            print e.message
            return -1

    def Delete_PhysicalPerson(self):
        if (self.DeletePhysicalPerson() == 1):
            if (self.DeletePerson(self.pp.Id) == 1):
                self.conn.commit()
                self.conn.close()
                return 1
            else:
                self.conn.rollback()
                self.conn.close()
                return -1
        else:
            self.conn.rollback()
            self.conn.close()
            return -1

    def Get_PhysicalPersonForID(self):
        try:
            curs = self.conn.cursor()
            curs.execute('SELECT * FROM PERSON INNER JOIN PHYSICALPERSON ON PERSON.ID = PHYSICALPERSON.PERSON_ID WHERE PERSON.ID = :ID', {"ID":self.pp.Id})
            lines = curs.fetchall()
            if lines:
                pp_r = PhysicalPerson()
                for row in lines:
                    pp_r.Id = row[0]
                    pp_r.Name = row[1]
                    pp_r.Email = row[2]
                    pp_r.Salary = row[5]
                    pp_r.Birthday = row[6]
                    pp_r.Gender = row[7]
                return pp_r
            else:
                return ''
        except:
             return ''

    def Get_PhysicalPersonForName(self):
        try:
            curs = self.conn.cursor()
            curs.execute('SELECT * FROM PERSON INNER JOIN PHYSICALPERSON ON PERSON.ID = PHYSICALPERSON.PERSON_ID WHERE PERSON.NAME LIKE :NAME', {"NAME":self.pp.Name + '%'})
            lines = curs.fetchall()
            if lines:
                list_physicalperson = []
                for row in lines:
                    pp_r = PhysicalPerson()
                    pp_r.Id = row[0]
                    pp_r.Name = row[1]
                    pp_r.Email = row[2]
                    pp_r.Salary = row[5]
                    pp_r.Birthday = row[6]
                    pp_r.Gender = row[7]
                    list_physicalperson.append(pp_r)
                return list_physicalperson
            else:
                return ''
        except:
             raise