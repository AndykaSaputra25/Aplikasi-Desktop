from PyQt5 import QtWidgets,uic,QtSql,QtCore
from PyQt5.QtWidgets import QMessageBox , QLineEdit
import sys
from PyQt5.QtSql import QSqlTableModel

import cari

class Totalnya (QtWidgets.QMainWindow):
    def __init__(self):
        super(Totalnya, self).__init__()        
        self.model = QSqlTableModel()
        uic.loadUi('total.ui', self)
        self.openDB()
        self.model = QtSql.QSqlTableModel()
        self.show()
        self.btn_kembali.clicked.connect(self.caridata)
        self.btn_total.clicked.connect(self.total)
        
    def openDB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('dbLaundry2.db')

        if not db.open():
            return False
        else :
            return True
        
    def total(self):
        query = QtSql.QSqlQuery("select sum(total) from dataPelanggan where status='Lunas'")
        while (query.next()):
            if query.value(0)=='':
                pass
            else:
                self.ln_total.setText('Rp. '+str(int(query.value(0))))
                
    def caridata(self):
        self.a = cari.search()
        self.hide()
        self.a.show()
                
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Totalnya()
    sys.exit(app.exec_())
