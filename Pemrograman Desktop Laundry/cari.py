from PyQt5 import QtWidgets,uic,QtSql,QtCore
from PyQt5.QtWidgets import QMessageBox , QLineEdit
import sys
from PyQt5.QtSql import QSqlTableModel

import main2, update, total

class search(QtWidgets.QMainWindow):
    def __init__(self):
        super(search, self).__init__()        
        self.model = QSqlTableModel()
        uic.loadUi('cari.ui', self)
        self.openDB()
        self.model = QtSql.QSqlTableModel()
        self.displaytable('')
        self.show()
        self.cari.clicked.connect(self.caridata)
        self.tambah.clicked.connect(self.tambahdata)
        self.updatestatus.clicked.connect(self.status)
        self.btn_total.clicked.connect(self.total)
        
    def openDB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('dbLaundry2.db')

        if not db.open():
            return False
        else :
            return True

    def displaytable(self, p_filter):
        if p_filter == '':
            query = QtSql.QSqlQuery("select * from dataPelanggan")
            self.model.setTable('')
            self.model.setQuery(query)
                                    
        else:
            query = QtSql.QSqlQuery("select * from dataPelanggan where nota like '%"+p_filter + "%' ")
            self.model.setTable('')
            self.model.setQuery(query)        
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.tableView.setModel(self.model)

    def caridata(self):
        cari =(self.ln_cari.text())
        self.displaytable(cari)

    def tambahdata(self):
        self.tambah = main2.Ui()
        self.hide()
        self.tambah.show()
        
    def edit (self):
        rows = self.tableView.selectionModel().selectedRows()
        for row in rows :
            current = self.model.data(self.model.index(row.row(),0))
        self.tampil = status.Edit.id(current)
        
    def status(self):
        self.open = update.Edit()
        self.hide()
        self.open.show()
        
    def total(self):
        self.tot = total.Totalnya()
        self.hide()
        self.tot.show()
                
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = search()
    sys.exit(app.exec_())
