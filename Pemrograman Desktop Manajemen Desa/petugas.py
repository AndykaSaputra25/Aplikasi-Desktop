import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtSql, QtGui
from PyQt5.QtSql import *

class Petugas(QWidget):
    def __init__(self, parent = None):
        super(Petugas, self).__init__(parent)
        self.setWindowTitle("Desa Pintar - Petugas")
        self.setGeometry(150, 50, 900, 700)
        self.setWindowIcon(QtGui.QIcon('gambar/pythonLogo.png'))
        self.setStyleSheet("font-size: 17px")
        self.windows()

    def windows(self):
        self.lbl = QLabel("PERANGKAT DESA")
        self.lbl.setStyleSheet("font-size: 30px; margin: 2px 5px; font-weight: bold; color: brown;")

        self.menuGroupBox()
        self.createBottomGroupBox()

        self.btnSearch.clicked.connect(self.search_koneksi)

        topLayout = QHBoxLayout()
        topLayout.addWidget(self.lbl)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0)
        mainLayout.addWidget(self.iniMenu, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 2, 0)
        self.setLayout(mainLayout)
        
    def menuGroupBox(self):
        self.iniMenu = QGroupBox("menu")
        self.search = QLineEdit()

        self.btnSearch = QPushButton('Search')

        layout = QHBoxLayout()
        layout.addWidget(self.search)
        layout.addWidget(self.btnSearch)
        self.iniMenu.setLayout(layout)

    def createBottomGroupBox(self):
        self.topRightGroupBox = QGroupBox("Database Perangkat Desa")
        self.tableView = QTableView()
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.model = QtSql.QSqlTableModel(self)

        self.db.setDatabaseName('sedatiAgung.db')	
        self.db.open()
        self.model.setTable('petugas')
        self.model.select()
        self.tableView.setModel(self.model)
        
        layout = QVBoxLayout()
        layout.addWidget( self.tableView)
        self.topRightGroupBox.setLayout(layout)

    def search_koneksi(self):
        model = QSqlQueryModel()
        cari = str(self.search.text())
        if cari == "":
            sql = "SELECT * FROM petugas"
        else:
            sql = "SELECT * FROM petugas WHERE nama LIKE '%" + str(cari) + "%' or jabatan LIKE '%" + str(cari) + "%' "
        model.setQuery(sql)
        model.setHeaderData(0, Qt.Horizontal, "nama")
        model.setHeaderData(1, Qt.Horizontal, "jabatan")
        model.setHeaderData(2, Qt.Horizontal, "alamat")
        model.setHeaderData(3, Qt.Horizontal, "noHP")
        self.tableView.setModel(model)

def main():
    app = QApplication(sys.argv)
    win = Petugas()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()    
