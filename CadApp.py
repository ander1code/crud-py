import abc
import sqlite3
import hashlib

#####################################################################
class Person(object):
    __metaclass__ = abc.ABCMeta
    @property
    def Code(self):
        pass
    @Code.setter
    def Code(self, code):
        pass 
    @property
    def Name(self):
        pass
    @Name.setter
    def Name(self, name):
        pass
    @property
    def Email(self):
        pass
    @Email.setter
    def Email(self, email):
        pass
#####################################################################

class PhysicalPerson(Person):
    @property 
    def Code(self):
        return self.code
    @Code.setter
    def Code(self, code):
        self.code = code
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
    def DateBirth(self):
        return self.datebirth
    @DateBirth.setter
    def DateBirth(self, datebirth):
        self.datebirth = datebirth
    @property
    def Genre(self):
        return self.genre
    @Genre.setter
    def Genre(self, genre):
        self.genre = genre
#####################################################################

class User(object):
    @property 
    def Code(self):
        return self.code
    @Code.setter
    def Code(self, code):
        self.code = code
    @property
    def Login(self):
        return self.login
    @Login.setter
    def Login(self, login):
        self.login = login
    @property
    def Password(self):
        return self.password
    @Password.setter
    def Password(self, password):
        self.password = password
#####################################################################
 
class Connection(object): 
    @staticmethod
    def ToConnect():
        try:
            conn = sqlite3.connect('db.sqlite')
            return conn
        except:
            return null
#####################################################################

class Controller(object):

    def __init__(self, pf, usu):
        self.conn = Connection.ToConnect()
        self.usu = usu
        self.pf = pf

    def CodeInsertGenerator(self):
        try:
            sql = 'SELECT MAX(CODIGO) + 1 FROM PESSOA'
            curs = self.conn.cursor()
            curs.execute(sql)
            try:
                print('retornando codigo ...')
                return curs.fetchone()[0]
            except:
                print('retornando 1 ...')
                return 1
        except:
            return -1

    def InsertPerson(self, code, name, email):
        try:
            curs = self.conn.cursor()
            name = repr.escape(name).strip()
            email = repr.escape(email).strip()
            curs.execute("INSERT INTO PESSOA (CODIGO, NOME, EMAIL) VALUES (?,?,?)", (code, name, email))
            return 1
        except:
            return -1

    def InsertPhysicalPerson(self):
        try:
            curs = self.conn.cursor()
            code = repr.escape(self.pf.Code).strip()
            salary = repr.escape(self.pf.Salary).strip()
            dateOfBirth = repr.escape(self.pf.DateBirth).strip()
            genre = repr.escape(self.pf.Genre).strip()
            curs.execute('INSERT INTO PESSOAFISICA (CODIGO, PESSOA_CODIGO, RENDA, DATANASC, SEXO) VALUES (?, ?, ?, ?, ?)', (code, code, salary, dateOfBirth, genre))
            return 1
        except:
            return -1

    def Insert_PhysicalPerson(self):
        code = self.CodeInsertGenerator()
        if (code > 0):
            self.pf.Code = code
            if (self.InsertPerson(code, self.pf.Name, self.pf.Email) == 1):
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

    def EditPerson(self, code, name, email):
        try:
            curs = self.conn.cursor()
            curs.execute("UPDATE PESSOA SET NOME = ?, EMAIL = ? WHERE CODIGO = ?", (name, email, code))
            return 1
        except:
            return -1

    def EditPhysicalPerson(self):
        try:
            curs = self.conn.cursor()
            curs.execute('UPDATE PESSOAFISICA SET RENDA = ?, DATANASC = ?, SEXO = ? WHERE CODIGO = ?', (self.pf.Salary, self.pf.DateBirth, self.pf.Genre, self.pf.Code))
            return 1
        except:
            return -1

    def Edit_PhysicalPerson(self):
        if (self.EditPerson(self.pf.Code, self.pf.Name, self.pf.Email) == 1):
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

    def DeletePerson(self, code):
        try:
            curs = self.conn.cursor()
            curs.execute("DELETE FROM PESSOA WHERE CODIGO = ?", (code))
            return 1
        except:
            return -1

    def DeletePhysicalPerson(self):
        try:
            curs = self.conn.cursor()
            curs.execute('DELETE FROM PESSOAFISICA WHERE CODIGO = ?', (self.pf.Code))
            return 1
        except:
            return -1

    def Delete_PhysicalPerson(self):
        if (self.DeletePhysicalPerson() == 1):
            if (self.DeletePerson(self.pf.Code) == 1):
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

    def Get_PhysicalPersonForCode(self):
        try:
            curs = self.conn.cursor()
            curs.execute('SELECT * FROM PESSOA INNER JOIN PESSOAFISICA ON PESSOA.CODIGO = PESSOAFISICA.PESSOA_CODIGO WHERE PESSOA.CODIGO = :CODIGO', {"CODIGO":self.pf.Code})
            lines = curs.fetchall()
            if lines:
                pf_r = PhysicalPerson()
                for row in lines:
                    pf_r.Code = row[0]
                    pf_r.Name = row[1]
                    pf_r.Email = row[2]
                    pf_r.Salary = row[5]
                    pf_r.DateBirth = row[6]
                    pf_r.Genre = row[7]
                return pf_r
            else:
                return ''
        except:
             return ''

    def Get_PhysicalPersonForName(self):
        try:
            curs = self.conn.cursor()
            curs.execute('SELECT * FROM PESSOA INNER JOIN PESSOAFISICA ON PESSOA.CODIGO = PESSOAFISICA.PESSOA_CODIGO WHERE PESSOA.NOME LIKE :NOME', {"NOME":self.pf.Name + '%'})
            lines = curs.fetchall()
            if lines:
                list_physicalperson = []
                for row in lines:
                    pf_r = PhysicalPerson()
                    pf_r.Code = row[0]
                    pf_r.Name = row[1]
                    pf_r.Email = row[2]
                    pf_r.Salary = row[5]
                    pf_r.DateBirth = row[6]
                    pf_r.Genre = row[7]
                    list_physicalperson.append(pf_r)
                return list_physicalperson
            else:
                return ''
        except:
             raise

    def ToLog(self):
        try:
            curs = self.conn.cursor()
            password = hashlib.md5(self.usu.Password.encode('utf-8')).hexdigest()
            curs.execute('SELECT * FROM USUARIO WHERE USUARIO.LOGIN = ? AND USUARIO.SENHA = ?'  , (self.usu.Login, password))
            lines = curs.fetchall()
            if lines:
                return 1
            else:
                return -1
        except:
             return -1        
#####################################################################









class Registration(object):

    @staticmethod
    def Insert_PhysicalPerson(name, email, salary, datebirth, genre):
        pf = PhysicalPerson()
        pf.Name = name
        pf.Email = email
        pf.Salary = salary
        pf.DateBirth = datebirth
        pf.Genre = genre
        ctr = Controller(pf, '')
        retorno = ctr.Insert_PhysicalPerson()
        if retorno == 1:
            return 1
        else:
            return -1


    @staticmethod
    def Edit_PhysicalPerson(code, name, email, salary, datebirth, genre):
        pf = PhysicalPerson()
        pf.Code = code
        pf.Name = name
        pf.Email = email
        pf.Salary = salary
        pf.DateBirth = datebirth
        pf.Genre = genre
        ctr = Controller(pf, '')
        retorno = ctr.Edit_PhysicalPerson()
        if retorno == 1:
            return 1
        else:
            return -1

    @staticmethod
    def Delete_PhysicalPerson(code):
        pf = PhysicalPerson()
        pf.Code = code
        ctr = Controller(pf, '')
        retorno = ctr.Delete_PhysicalPerson()
        if retorno == 1:
            return 1
        else:
            return -1

    @staticmethod
    def Get_PhysicalPersonForCode(code):
        pf = PhysicalPerson()
        pf.Code = code
        ctr = Controller(pf, '')
        retorno = ctr.Get_PhysicalPersonForCode()
        return retorno

    @staticmethod
    def Get_PhysicalPersonForName(name):
        pf = PhysicalPerson()
        pf.Name = name
        ctr = Controller(pf, '')
        retorno = ctr.Get_PhysicalPersonForName()
        return retorno

    @staticmethod
    def ToLog(login, password):
        usu = User()
        usu.Login = login
        usu.Password = password
        ctr = Controller('', usu)
        result = ctr.ToLog()
        return result




retorno = Registration.Insert_PhysicalPerson('Maurina', 'maura@globo.com', 3000, '06/08/1954', 'F');
print(retorno)






