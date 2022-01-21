import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtSql, QtGui
from PyQt5.QtSql import *


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desa Pintar - Main")
        self.setGeometry(150, 50, 900, 700)
        self.setWindowIcon(QtGui.QIcon('pythonLogo.png'))
        self.setStyleSheet("font-size: 17px")
        self.windows()
    
    def windows(self):
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.model = QtSql.QSqlTableModel()
        
        self.lbl = QLabel("SEDATI AGUNG")
        cekBox1 = QCheckBox("Nonaktifkan")
        self.lbl.setStyleSheet("font-size: 30px; margin: 2px 5px; font-weight: bold; color: brown;")

        self.menuGroupBox()
        self.createTopGroupBox()
        self.createBottomGroupBox()
        
        cekBox1.toggled.connect(self.topLeftGroupBox.setDisabled)
        cekBox1.toggled.connect(self.topRightGroupBox.setDisabled)

        topLayout = QHBoxLayout()
        topLayout.addWidget(self.lbl)
        topLayout.addStretch(1)
        topLayout.addWidget(cekBox1)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0)
        mainLayout.addWidget(self.iniMenu, 1, 0)
        mainLayout.addWidget(self.topLeftGroupBox, 2, 0)
        mainLayout.addWidget(self.topRightGroupBox, 3, 0)
        self.setLayout(mainLayout)
        
    def menuGroupBox(self):
        self.iniMenu = QGroupBox("menu")
        self.searchKK = QLineEdit()

        self.sekat = QLabel("            ")

        self.btnSearch = QPushButton('Search')
        self.btnAdd = QPushButton('Add')
        self.btnDelete = QPushButton('Delete')
        self.btnUpdate = QPushButton('Update')
        self.btnClear = QPushButton('Clear')

        layout = QHBoxLayout()
        layout.addWidget(self.searchKK)
        layout.addWidget(self.btnSearch)
        layout.addWidget(self.sekat)
        layout.addWidget(self.btnClear)
        layout.addWidget(self.btnAdd)
        layout.addWidget( self.btnUpdate)
        layout.addWidget(self.btnDelete)
        self.iniMenu.setLayout(layout)

    def createTopGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Input Data Penduduk")
        nama = QLabel('Nama Lengkap')
        tempatLahir = QLabel('Tempat Lahir')
        tanggalLahir = QLabel('Tanggal Lahir')
        alamat = QLabel('Alamat')
        rt = QLabel('RT')
        noKK = QLabel('No. KK')
        pendidikan = QLabel('Pendidikan')
        jenisKelamin = QLabel('Jenis Kelamin')
        agama = QLabel('Agama')
        statusNikah = QLabel('Status Nikah')
        pekerjaan = QLabel('Pekerjaan')
        kewarnegaraan = QLabel('Kewarnegaraan')
        statusWarga = QLabel('Status Warga')

        self.inpNama = QLineEdit()
        self.inpTempatLahir = QLineEdit()
        self.inpAlamat = QLineEdit()
        self.inpNoKK = QLineEdit()
        self.inpPekerjaan = QLineEdit()

        self.inpTanggalLahir = QDateTimeEdit()
        self.inpTanggalLahir.setDisplayFormat("dd/MM/yyyy")

        qRt = ["01","02","03","04","05"]
        self.inpRt = QComboBox()
        for i in qRt:
            self.inpRt.addItem(i)

        qPendidikan = ["SD","SMP","SMA","D1","D2","D3","D4","S1","S2","S3"]
        self.inpPendidikan = QComboBox()
        for i in qPendidikan:
            self.inpPendidikan.addItem(i)

        qJk = ["Pria","Wanita"]
        self.inpJenisKelamin = QComboBox()
        for i in qJk:
            self.inpJenisKelamin.addItem(i)

        qAgama = ["Islam","Kristen","Katolik","Hindu","Buddha","Konghucu"]
        self.inpAgama = QComboBox()
        for i in qAgama:
            self.inpAgama.addItem(i)

        qNikah = ["Nikah","Belum Nikah"]
        self.inpStatusNikah = QComboBox()
        for i in qNikah:
            self.inpStatusNikah.addItem(i)

        qNegara = ["WNI","WNA"]
        self.inpKewarnegaraan = QComboBox()
        for i in qNegara:
            self.inpKewarnegaraan.addItem(i)

        qWarga = ["Tetap","Sementara"]
        self.inpStatusWarga = QComboBox()
        for i in qWarga:
            self.inpStatusWarga.addItem(i)

        self.lblKoneksi = QLabel('Reload')
        self.open = QPushButton('Reload')

        self.dateTimeEdit = QDateTimeEdit()
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.dateTimeEdit.setDisplayFormat("dd/MM/yyyy")

        self.open.clicked.connect(self.open_koneksi)
        self.btnAdd.clicked.connect(self.add_koneksi)
        self.btnDelete.clicked.connect(self.delete_koneksi)
        self.btnUpdate.clicked.connect(self.update_koneksi)
        self.btnClear.clicked.connect(self.clear_koneksi)

        layout = QGridLayout()
        layout.addWidget(nama, 0, 0)
        layout.addWidget(self.inpNama, 0, 1)
        layout.addWidget(noKK, 0, 2)
        layout.addWidget(self.inpNoKK, 0, 3)
        layout.addWidget(statusNikah, 0, 4)
        layout.addWidget(self.inpStatusNikah, 0, 5)
        layout.addWidget(tempatLahir, 1, 0)
        layout.addWidget(self.inpTempatLahir,1, 1)
        layout.addWidget(pendidikan,1, 2)
        layout.addWidget(self.inpPendidikan,1, 3)
        layout.addWidget(pekerjaan,1, 4)
        layout.addWidget(self.inpPekerjaan,1, 5)
        layout.addWidget(tanggalLahir, 2, 0)
        layout.addWidget(self.inpTanggalLahir, 2, 1)
        layout.addWidget(jenisKelamin, 2, 2)
        layout.addWidget(self.inpJenisKelamin, 2, 3)
        layout.addWidget(kewarnegaraan, 2, 4)
        layout.addWidget(self.inpKewarnegaraan, 2, 5)
        layout.addWidget(alamat, 3, 0)
        layout.addWidget(self.inpAlamat, 3, 1)
        layout.addWidget(agama, 3, 2)
        layout.addWidget(self.inpAgama, 3, 3)
        layout.addWidget(statusWarga, 3, 4)
        layout.addWidget(self.inpStatusWarga, 3, 5)
        layout.addWidget(rt, 4, 0)
        layout.addWidget(self.inpRt, 4, 1)
        layout.addWidget(self.dateTimeEdit, 4, 3)
        layout.addWidget(self.lblKoneksi, 4, 4)
        layout.addWidget(self.open, 4, 5)
        self.topLeftGroupBox.setLayout(layout)  

    def open_koneksi(self):    
        self.db.setDatabaseName('dbPulsa.db')	
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

    def add_koneksi(self):
        pembuatan = str(self.dateTimeEdit.date().toPyDate())
        kk = str(self.inpNoKK.text())
        nama = str(self.inpNama.text())
        alamat = str(self.inpAlamat.text())
        rt = str(self.inpRt.currentText())
        tempat = str(self.inpTempatLahir.text())
        lahir = str(self.inpTanggalLahir.date().toPyDate())
        agama = str(self.inpAgama.currentText())
        pendidikan = str(self.inpPendidikan.currentText())
        jk = str(self.inpJenisKelamin.currentText())
        sn = str(self.inpStatusNikah.currentText())
        pekerjaan = str(self.inpPekerjaan.text())
        wn = str(self.inpKewarnegaraan.currentText())
        sw = str(self.inpStatusWarga.currentText())
        if kk == "" or nama == "" or alamat == "" or tempat == "" or pekerjaan == "":
                QMessageBox.warning(self,"WARNING","Lengkapi Data !!!")
        else:
            query = QSqlQuery()
            query.prepare("INSERT INTO " + "pulsa" + " (Tanggal_Pembuatan,NIK,Nama_Lengkap,Alamat,RT,Tempat_Lahir,Tanggal_Lahir,Agama,Pendidikan,Jenis_Kelamin,Status_Nikah,Pekerjaan,Kewarnegaraan,Status_Warga) VALUES (:pembuatan,:kk,:nama,:alamat,:rt,:tempat,:lahir,:agama,:pendidikan,:jk,:sn,:pekerjaan,:wn,:sw)")
            # query.bindValue(":tabel", self.table)
            query.bindValue(":pembuatan",pembuatan)
            query.bindValue(":kk", kk)
            query.bindValue(":nama", nama)
            query.bindValue(":alamat", alamat)
            query.bindValue(":rt",rt)
            query.bindValue(":tempat", tempat)
            query.bindValue(":lahir", lahir)
            query.bindValue(":agama", agama)
            query.bindValue(":pendidikan",pendidikan)
            query.bindValue(":jk", jk)
            query.bindValue(":sn", sn)
            query.bindValue(":pekerjaan", pekerjaan)
            query.bindValue(":wn",wn)
            query.bindValue(":sw", sw)
            if query.exec_():
                QMessageBox.about(self,"Berhasil","Berhasil Input Data")
            else:
                print(query.lastError().text())

    def delete_koneksi(self):
        if self.tableView.currentIndex().row() > -1:
            self.model.removeRow(self.tableView.currentIndex().row())
            self.model.select()
        else:
            QMessageBox.question(self,'Message', "Pilih data yang ingin dihapus", QMessageBox.Ok)
            self.show()

    def update_koneksi(self):
        if self.tableView.currentIndex().row() > -1:
            record = self.model.record(self.tableView.currentIndex().row())
            record.setValue("Tanggal_Pembuatan",self.inpNoKK.text())
            record.setValue("NIK",self.inpNoKK.text())
            record.setValue("Nama_Lengkap",self.inpNama.text())
            record.setValue("Alamat", self.inpAlamat.text())
            record.setValue("RT", self.inpRt.text())
            record.setValue("Tempat_Lahir", self.inpTempatLahir.text())
            record.setValue("Tanggal_Lahir",self.inpTanggalLahir.text())
            record.setValue("Agama",self.inpAgama.text())
            record.setValue("Pendidikan", self.inpPendidikan.text())
            record.setValue("Jenis_Kelamin", self.inpJenisKelamin.text())
            record.setValue("Status Nikah", self.inpStatusNikah.text())
            record.setValue("Pekerjaan",self.inpPekerjaan.text())
            record.setValue("Kewarnegaraan", self.inpKewarnegaraan.text())
            record.setValue("Status_Warga", self.inpStatusWarga.text())
            self.model.setRecord(self.tableView.currentIndex().row(), record)
        else:
            QMessageBox.question(self,'Message', "Pilih data yang ingin di update", QMessageBox.Ok)
            self.show()

    def clear_koneksi(self):
        self.searchKK.clear()
        self.inpNama.clear()
        self.inpTempatLahir.clear()
        self.inpTanggalLahir.clear()
        self.inpAlamat.clear()
        self.inpRt.clear()
        self.inpNoKK.clear()
        self.inpPendidikan.clear()
        self.inpJenisKelamin.clear()
        self.inpAgama.clear()
        self.inpStatusNikah.clear()
        self.inpPekerjaan.clear()
        self.inpKewarnegaraan.clear()
        self.inpStatusWarga.clear()

#__Group-2
    def createBottomGroupBox(self):
        self.topRightGroupBox = QGroupBox("Database Penduduk")

        self.tableView = QTableView()

        layout = QVBoxLayout()
        layout.addWidget( self.tableView)
        self.topRightGroupBox.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()    
