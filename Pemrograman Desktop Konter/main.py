import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtSql, QtGui
from PyQt5.QtSql import *


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Konter Trunojoyo - Main")
        self.setGeometry(150, 50, 900, 690)
        self.setWindowIcon(QtGui.QIcon('pythonLogo.png'))
        self.setStyleSheet("font-size: 17px")
        self.windows()
    
    def windows(self):
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.model = QtSql.QSqlTableModel()
        
        self.lbl = QLabel("KONTER TRUNOJOYO")
        cekBox1 = QCheckBox("Nonaktifkan")
        self.lbl.setStyleSheet("font-size: 30px; margin: 2px 5px; font-weight: bold; color: brown;")

        self.menuGroupBox()
        self.createTopGroupBox()
        self.createBottomGroupBox()
        
        cekBox1.toggled.connect(self.iniMenu.setDisabled)
        cekBox1.toggled.connect(self.centerGroupBox.setDisabled)
        cekBox1.toggled.connect(self.bottomGroupBox.setDisabled)

        topLayout = QHBoxLayout()
        topLayout.addWidget(self.lbl)
        topLayout.addStretch(1)
        topLayout.addWidget(cekBox1)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0)
        mainLayout.addWidget(self.iniMenu, 1, 0)
        mainLayout.addWidget(self.centerGroupBox, 2, 0)
        mainLayout.addWidget(self.bottomGroupBox, 3, 0)
        self.setLayout(mainLayout)
        
    def menuGroupBox(self):
        self.iniMenu = QGroupBox("menu")
        self.searchKK = QLineEdit()

        self.sekat = QLabel("       ")

        qcari = ["Nama","Alamat","Nomor HP"]
        self.inpCari = QComboBox()
        for i in qcari:
            self.inpCari.addItem(i)

        self.btnSearch = QPushButton('Search')
        self.btnAdd = QPushButton('Add')
        self.btnDelete = QPushButton('Delete')
        self.btnUpdate = QPushButton('Update')
        self.btnClear = QPushButton('Clear')

        layout = QHBoxLayout()
        layout.addWidget(self.inpCari)
        layout.addWidget(self.searchKK)
        layout.addWidget(self.btnSearch)
        layout.addWidget(self.sekat)
        layout.addWidget(self.btnClear)
        layout.addWidget(self.btnAdd)
        layout.addWidget( self.btnUpdate)
        layout.addWidget(self.btnDelete)
        self.iniMenu.setLayout(layout)

    def createTopGroupBox(self):
        self.centerGroupBox = QGroupBox("Input Data Customers")
        nama = QLabel('Nama Lengkap')
        alamat = QLabel('Alamat')
        status = QLabel('Status')
        nomor = QLabel('Nomor HP')
        harga = QLabel('Harga')
        total = QLabel('Total Pembayaran')
        jenisKelamin = QLabel('Jenis Kelamin')
        waktu = QLabel('Tanggal Pembelian')

        self.inpNama = QLineEdit()
        self.inpAlamat = QLineEdit()
        self.inpNomor = QLineEdit()
        self.inpHarga = QLineEdit()
        self.inpTotal = QLineEdit()

        qStatus = ["Berhasil","Gagal"]
        self.inpStatus = QComboBox()
        for i in qStatus:
            self.inpStatus.addItem(i)

        qJk = ["Pria","Wanita"]
        self.inpJenisKelamin = QComboBox()
        for i in qJk:
            self.inpJenisKelamin.addItem(i)

        self.lblKoneksi = QLabel('Reload')
        self.open = QPushButton('Reload')

        self.dateTimeEdit = QDateTimeEdit()
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.dateTimeEdit.setDisplayFormat("dd/MM/yyyy")

        self.open.clicked.connect(self.open_koneksi)

        layout = QGridLayout()
        layout.addWidget(nama, 0, 0)
        layout.addWidget(self.inpNama, 0, 1)
        layout.addWidget(alamat, 0, 2)
        layout.addWidget(self.inpAlamat, 0, 3)
        layout.addWidget(nomor, 0, 4)
        layout.addWidget(self.inpNomor,0, 5)
        layout.addWidget(status, 1, 0)
        layout.addWidget(self.inpStatus, 1, 1)
        layout.addWidget(harga,1, 2)
        layout.addWidget(self.inpHarga,1, 3)
        layout.addWidget(total,1, 4)
        layout.addWidget(self.inpTotal, 1, 5)
        layout.addWidget(jenisKelamin, 2, 0)
        layout.addWidget(self.inpJenisKelamin, 2, 1)
        layout.addWidget(waktu, 2, 2)
        layout.addWidget(self.dateTimeEdit, 2, 3)
        layout.addWidget(self.lblKoneksi, 3, 4)
        layout.addWidget(self.open, 3, 5)
        self.centerGroupBox.setLayout(layout) 

    def open_koneksi(self):    
        self.db.setDatabaseName('dbPulsaTrunojoyo.db')	
        if not self.db.open():
            self.lblKoneksi.setText("Gagal")
            self.open.setEnabled(False)
        else:
            self.lblKoneksi.setText("Sukses")
            self.open.setEnabled(True)
            self.read_data()
            pass
    def read_data(self):    
        self.model.setTable('pulsa')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.tableView.setModel(self.model)

#__Group-2
    def createBottomGroupBox(self):
        self.bottomGroupBox = QGroupBox("Database Customer")

        self.tableView = QTableView()

        layout = QVBoxLayout()
        layout.addWidget( self.tableView)
        self.bottomGroupBox.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()    
