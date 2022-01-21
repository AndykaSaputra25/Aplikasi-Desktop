from PyQt5 import QtWidgets,uic,QtSql,QtCore
from PyQt5.QtWidgets import QMessageBox , QLineEdit
import sys
import cari
from PyQt5.QtSql import QSqlTableModel

class Edit(QtWidgets.QMainWindow):
    def __init__(self):
        super(Edit, self).__init__()
        self.model = QSqlTableModel()
        uic.loadUi('Upstatus.ui', self)
        self.openDB()
        self.model = QtSql.QSqlTableModel()
        self.display()
        self.show()
        self.simpan.clicked.connect(self.save)
        self.kembali.clicked.connect(self.back)

    def openDB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('dbLaundry2.db')

        if not db.open():
            return False
        else :
            return True
        
    def display(self):
        nonota = self.up_nota.text()
        query = QtSql.QSqlQuery("select * from dataPelanggan where nota = '"+nonota+"' ")
        self.model.setTable('dataPelanggan')
        self.model.setTable("")
        self.model.setQuery(query)        
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.tableView.setModel(self.model)
        
    def save (self) :
        if self.status.currentIndex() == 0:
            sts = str(self.status.currentText())
            Notanya = str(self.up_nota.text())
            query = QtSql.QSqlQuery()
            query.exec_("update dataPelanggan set Status ='"+sts+"' where nota ='"+str(Notanya)+"' ")      
         
        else :
            sts = str(self.status.currentText())
            Notanya = str(self.up_nota.text())
            query = QtSql.QSqlQuery()
            query.exec_("update dataPelanggan set Status ='"+sts+"' where nota ='"+str(Notanya)+"' ")      
        
        Msg = QMessageBox()
        Msg.setText('Data Berhasil Diedit')
        Msg.exec()
            
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.tableView.setModel(self.model)
        self.display()
                              
    def back(self):
        self.a = cari.search()
        self.hide()
        self.a.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Edit()
    sys.exit(app.exec_())
