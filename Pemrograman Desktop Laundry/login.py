import sys,datetime
from PyQt5 import QtWidgets,uic,QtSql,QtCore
from PyQt5.QtWidgets import QMessageBox , QLineEdit
from PyQt5.QtSql import QSqlTableModel

import main2

class Registrasi(QtWidgets.QMainWindow):
    def __init__(self):
        super(Registrasi, self).__init__()
        uic.loadUi('form_register.ui', self)
        self.show()
        self.reg2.clicked.connect(self.input_field)
        self.log2.clicked.connect(self.kembali)
        self.rpass.setEchoMode(QLineEdit.Password)
        self.newpass.setEchoMode(QLineEdit.Password)
        
        self.log2.setStyleSheet('border: 1px solid; border-radius : 5px;')
        self.reg2.setStyleSheet('border: 1px solid; border-radius : 5px;')

    def input_field(self):
        if len(self.ruser.text()) == 0 or len(self.email.text())==0 or len(self.rpass.text())==0 or len(self.newpass.text()) == 0:
            warning = QMessageBox()
            warning.setText('Please isi Field')
            warning.exec()
        else :
            if self.rpass.text() != self.newpass.text():
                warning = QMessageBox()
                warning.setText('Password yang anda inputkan tidak sesuai')
                warning.exec()
            else :
                id_admin = str(self.id.text())
                nama = str(self.ruser.text())
                email = str(self.email.text())
                passw = str(self.rpass.text())
                query = QtSql.QSqlQuery()
                query.exec_("insert into admin values ('"+id_admin+"','"+nama+"','"+email+"','"+passw+"')")
                warning = QMessageBox()
                warning.setText('Data berhasil disimpan')
                warning.exec()
            
    def kembali (self):
        self.form_login = loginUser()
        self.hide()
        self.form_login.show()

class loginUser(QtWidgets.QMainWindow):
    def __init__(self):
        super(loginUser, self).__init__()
        self.model = QSqlTableModel()
        uic.loadUi('form_login.ui', self)
        self.show()
        self.opendatabase()
        self.lpass.setEchoMode(QLineEdit.Password)
        self.log1.clicked.connect(self.input_login)
        self.reg1.clicked.connect(self.regis)

        self.log1.setStyleSheet('border: 1px solid; border-radius : 5px;')
        self.reg1.setStyleSheet('border: 1px solid; border-radius : 5px;')

    def opendatabase(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('dbLaundry2.db')

        if not db.open():
            return False
        else :
            return True
    
    def input_login(self):
        name = str(self.luser.text())
        passw = str(self.lpass.text())
        query = QtSql.QSqlQuery("select * from admin where Username = '"+name+"' and password = '"+passw+"'")
        while (query.next()):
            data = query.value(1)
            print(data)
            self.main2 = main2.Ui()
            self.hide()
            self.main2.users(data)
            self.main2.show()

    def regis(self):
        self.form_register = Registrasi()
        self.hide()
        self.form_register.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = loginUser()
    sys.exit(app.exec_())
