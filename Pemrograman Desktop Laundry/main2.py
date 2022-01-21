import sys, datetime
from PyQt5 import QtWidgets, uic, QtSql, QtCore
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QMessageBox
import cari, cetak

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
            super(Ui, self).__init__()
            self.model = QSqlTableModel()
            uic.loadUi('cus_laundry2.ui', self)
            self.show()
            self.OpenDB()
            self.model = QtSql.QSqlTableModel()
            self.TampilTabel('')
            self.BuatTabel()
            self.btn_tambah.clicked.connect(self.MasukkanData)
            self.btn_hitung.clicked.connect(self.Hitung)
            self.btn_hapus.clicked.connect(self.Hapus)
            self.btn_cari.clicked.connect(self.Cari)
            self.btn_cetak_nota.clicked.connect(self.cetakNota)
            
    def OpenDB(self):
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('dbLaundry2.db')
            if not db.open():
                self.label_db.setText("connect db error")
                self.label_db.setStyleSheet("background-color:red; color:white; border-radius:10px;")
                self.btn_tambah.setEnabled(False)
                return False
            else:
                self.label_db.setText("connect db OK")
                self.label_db.setStyleSheet("background-color:blue; color:white; border-radius:10px;")
                self.btn_tambah.setEnabled(False)
                return True
            
    def BuatTabel(self):
            query = QtSql.QSqlQuery()
            if not query.exec_("create table dataPelanggan("
                               "nota integer primary key,"
                               "nama varchar(50),"
                               "nohp varchar(15),"
                               "alamat varchar(50),"
                               "paket varchar(20),"
                               "berat integer,"
                               "jumlah varchar(100),"
                               "status varchar(30),"
                               "total integer,"
                               "masuk datetime,"
                               "selesai datetime)"):
                    self.label_tabel.setText("Create Table Ok")
                    self.label_tabel.setStyleSheet("background-color:green; color:white; border-radius:10px;")
                    return False
            else:
                    self.label_tabel.setText("Tabel Berhasil Ditambahkan Ke Database")
                    self.label_tabel.setStyleSheet("background-color:green; color:white; border-radius:10px;")
                    return True
                
    def MasukkanData(self):
            nota = str(self.ln_nota.text())
            nama = self.ln_nama.text()
            nohp = self.ln_hp.text()
            alamat = self.ln_alamat.text()
            paket = self.cb_paket.currentText()
            berat = str(self.sb_berat.value())
            jumlah = str(self.sb_jumlah.value())
            total = str(self.ln_total.text())
            date1 = self.calendarWidget.selectedDate()
            masuk = date1.toString()
            date2 = self.calendarWidget_2.selectedDate()
            selesai = date2.toString()
            
            if(self.lunas.isChecked()):
                status = "Lunas"
            elif(self.belum_bayar.isChecked()):
                status = "Belum"
                
            query = QtSql.QSqlQuery()
            eksekusi = query.exec_("insert into dataPelanggan values ('%s','%s', '%s','%s','%s','%s','%s','%s','%s','%s','%s')"%
                               (''.join(nota),''.join(nama),''.join(nohp),''.join(alamat),''.join(paket),''.join(berat),''.join(jumlah),''.join(status),
                                ''.join(total),''.join(masuk),''.join(selesai)))
            
            if not eksekusi:
                self.label_info.setText("Nota Tidak Boleh Sama")
                self.label_info.setStyleSheet("background-color:Orange; color:white; border-radius:10px;")
            else:
                warning = QMessageBox()
                warning.setText('Data Telah Ditambahkan')
                warning.exec()
                self.label_info.setText("Data Berhasil Dimasukkan") 
                self.label_info.setStyleSheet("background-color:Blue; color:white; border-radius:10px;")
                self.ln_nama.setText("")
                self.ln_hp.setText("")
                self.ln_alamat.setText("")
                self.sb_berat.setValue(0)
                self.sb_jumlah.setValue(0)
                self.ln_total.setText("")
                self.TampilTabel("")
                self.btn_tambah.setEnabled(False)
      
    def Hitung(self):
        berat = int(self.sb_berat.value())
        paket = self.cb_paket.currentText()
        if(paket=="Cuci Basah"):
            biaya = 3000
        elif(paket=="Cuci Kering"):
            biaya = 4000
        elif(paket=="Cuci Setrika"):
            biaya = 5000
        hasil_total = self.ln_total.setText(str(berat*biaya))
        self.btn_tambah.setEnabled(True)
        
    def TampilTabel(self, p_filter):
            if p_filter == "":
                self.model.setTable('dataPelanggan')
            else:
                query = QtSql.QSqlQuery("select * from dataPelanggan "
                                        "where nama like '%"+p_filter + "%' OR nota like '%"+p_filter + "%'")
                
                self.model.setTable("")
                self.model.setQuery(query)
                
            self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            self.model.select()
            self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Nota")
            self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Nama")
            self.model.setHeaderData(2, QtCore.Qt.Horizontal, "No.Hp")
            self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Alamat")
            self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Paket Laundry")
            self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Berat Cucian")
            self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Jumlah Cucian")
            self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Status")
            self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Total Harga")
            self.model.setHeaderData(9, QtCore.Qt.Horizontal, "Tanggal Masuk")
            self.model.setHeaderData(10, QtCore.Qt.Horizontal,"Tanggal Selesai")
            self.tableView.setModel(self.model)
        
    def Hapus(self):
        self.model.removeRow(self.tableView.currentIndex().row())
        self.label_info.setText("Data Berhasil Dihapus") 
        self.label_info.setStyleSheet("background-color:Red; color:white; border-radius:10px;")
        self.TampilTabel('')
            
    def users(self,data):
        self.ln_admin.setText(data)
        
    def Cari(self):
        self.pencarian=cari.search()
        self.hide()
        self.pencarian.show()
        
    def cetakNota(self):
        c_nota = str(self.ln_nota.text())
        c_nama = str(self.ln_nama.text())
        c_hp = str(self.ln_hp.text())
        c_alamat = str(self.ln_alamat.text())
        c_paket = str(self.cb_paket.currentText())
        c_berat = str(self.sb_berat.value())
        c_jumlah = str(self.sb_jumlah.value())
        c_total = str(self.ln_total.text())
        
        if(self.lunas.isChecked()):
            c_status = "Lunas"
        elif(self.belum_bayar.isChecked()):
            c_status = "Belum"
            
        date1 = self.calendarWidget.selectedDate()
        date2 = self.calendarWidget_2.selectedDate()
        c_masuk = date1.toString()
        c_selesai = date2.toString()
        
        if c_nota == '' :
            c_warning = QMessageBox()
            c_warning.setText('Simpan Data terlebih dahulu')
            c_warning.exec()
        else :
            self.tampil = cetak.Cetak()
            self.hide()
            self.tampil.id(str(c_nota),str(c_nama),str(c_hp),str(c_alamat),str(c_paket),str(c_berat),str(c_jumlah),str(c_total),str(c_status),str(c_masuk),str(c_selesai))
            self.tampil.sambungkan()
            self.tampil.show()
            
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
