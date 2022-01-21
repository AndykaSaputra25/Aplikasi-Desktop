import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtSql, QtGui
from PyQt5.QtSql import *


class Main(QWidget):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.setWindowTitle("Desa Pintar - Main")
        self.setGeometry(150, 50, 900, 700)
        self.setWindowIcon(QtGui.QIcon('gambar/pythonLogo.png'))
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
        noKK = QLabel('NIK')
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
        self.btnSearch.clicked.connect(self.search_koneksi)

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
        self.db.setDatabaseName('sedatiAgung.db')	
        if not self.db.open():
            self.lblKoneksi.setText("Gagal")
            self.open.setEnabled(False)
        else:
            self.lblKoneksi.setText("Sukses")
            self.open.setEnabled(True)
            self.read_data()
            pass
    def read_data(self):    
        self.model.setTable('penduduk')
        #_Semua perubahan model segera di terapkan ke database
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
            query.prepare("INSERT INTO penduduk (Tanggal_Pembuatan,NIK,Nama_Lengkap,Alamat,RT,Tempat_Lahir,Tanggal_Lahir,Agama,Pendidikan,Jenis_Kelamin,Status_Nikah,Pekerjaan,Kewarnegaraan,Status_Warga) VALUES (:pembuatan,:kk,:nama,:alamat,:rt,:tempat,:lahir,:agama,:pendidikan,:jk,:sn,:pekerjaan,:wn,:sw)")
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
            QMessageBox.about(self,"Berhasil","Berhasil Delete Data")
        else:
            QMessageBox.warning(self,'Message', "Pilih data yang ingin dihapus")

    def update_koneksi(self):
        if self.tableView.currentIndex().row() > -1:
            if str(self.btnUpdate.text()) == "Edit":
                self.btnUpdate.setText("Update")
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
                query = QSqlQuery()
                query.prepare("UPDATE penduduk SET Nama_Lengkap=:nama, Alamat=:alamat, RT=:rt, Agama=:agama, Pendidikan=:pendidikan, Status_Nikah=:sn,Pekerjaan=:pekerjaan, Status_Warga=:sw WHERE  NIK = :nik")
                query.bindValue(":nik", self.nik)
                query.bindValue(":nama", nama)
                query.bindValue(":alamat", alamat)
                query.bindValue(":tempat", tempat)
                query.bindValue(":pekerjaan", pekerjaan)
                if query.exec_():
                    QMessageBox.about(self,"Berhasil","Berhasil Update Data")
                else:
                    print(query.lastError().text())
            else:
                self.btnUpdate.setText("Edit")
                index = self.tableView.selectedIndexes()[1]
                self.nik = self.tableView.model().data(index)
                query = QSqlQuery()
                query.prepare("SELECT * FROM penduduk WHERE NIK = :id")
                query.bindValue(":id", self.nik)
                if query.exec_():
                    while query.next():
                        self.inpNoKK.setText(query.value(1))
                        self.inpNama.setText(query.value(2))
                        self.inpAlamat.setText(query.value(3))
                        self.inpRt.setCurrentText(query.value(4))
                        self.inpTempatLahir.setText(query.value(5))
                        self.inpAgama.setCurrentText(query.value(7))
                        self.inpPendidikan.setCurrentText(query.value(8))
                        self.inpStatusNikah.setCurrentText(query.value(10))
                        self.inpPekerjaan.setText(query.value(11))
                        self.inpStatusWarga.setCurrentText(query.value(13))
        else:
            QMessageBox.warning(self,'Message', "Pilih data yang ingin di update")
            
    def clear_koneksi(self):
        self.searchKK.clear()
        self.inpNama.clear()
        self.inpTempatLahir.clear()
        self.inpAlamat.clear()
        self.inpNoKK.clear()
        self.inpPekerjaan.clear()

    def search_koneksi(self):
        query = QSqlQueryModel()
        cari = str(self.searchKK.text())
        if cari == "":
            sql = "SELECT * FROM penduduk"
        else:
            sql = "SELECT * FROM penduduk WHERE NIK LIKE '%" + str(cari) + "%' or Nama_Lengkap LIKE '%" + str(cari) + "%' "
        query.setQuery(sql)
        query.setHeaderData(0, Qt.Horizontal, "Tanggal_Pembuatan")
        query.setHeaderData(1, Qt.Horizontal, "NIK")
        query.setHeaderData(2, Qt.Horizontal, "Nama_Lengkap")
        query.setHeaderData(3, Qt.Horizontal, "Alamat")
        query.setHeaderData(4, Qt.Horizontal, "RT")
        query.setHeaderData(5, Qt.Horizontal, "Tempat_Lahir")
        query.setHeaderData(6, Qt.Horizontal, "Tanggal_Lahir")
        query.setHeaderData(7, Qt.Horizontal, "Agama")
        query.setHeaderData(8, Qt.Horizontal, "Pendidikan")
        query.setHeaderData(9, Qt.Horizontal, "Jenis_Kelamin")
        query.setHeaderData(10, Qt.Horizontal, "Status_Nikah")
        query.setHeaderData(11, Qt.Horizontal, "Pekerjaan")
        query.setHeaderData(12, Qt.Horizontal, "Kewarnegaraan")
        query.setHeaderData(13, Qt.Horizontal, "Status_Warga")
        self.tableView.setModel(query)

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
