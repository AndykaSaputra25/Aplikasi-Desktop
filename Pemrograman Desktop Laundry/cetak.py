import sys
from PyQt5 import QtWidgets,uic,QtSql,QtCore
from PyQt5.QtWidgets import QMessageBox , QLineEdit
from PyQt5.QtSql import QSqlTableModel
import main2

class Cetak (QtWidgets.QMainWindow) :
    def __init__ (self):
        super(Cetak, self).__init__()
        self.model = QSqlTableModel()
        uic.loadUi('cetak.ui', self)
        self.setWindowTitle('Cetak Nota')
        self.openDB()
        self.model = QtSql.QSqlTableModel()
        self.show()
        self.btn_kembali.clicked.connect(self.kembali)
        self.btn_kembali.setStyleSheet('border: 1px solid; border-radius : 5px;')
        self.sambungkan()
        
    def openDB(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('dbLaundry2.db')

        if not db.open():
            return False
        else :
            return True
        
    def id (self,c_nota,c_nama,c_hp,c_alamat,c_paket,c_berat,c_jumlah,c_masuk,c_selesai,c_total,c_status):
        self.lb_nota.setText(c_nota)
        self.lb_nama.setText(c_nama)
        self.lb_hp.setText(c_hp)
        self.lb_alamat.setText(c_alamat)
        self.lb_paket.setText(c_paket)
        self.lb_berat.setText(c_berat)
        self.lb_jumlah.setText(c_jumlah)
        self.lb_masuk.setText(c_masuk)
        self.lb_selesai.setText(c_selesai)
        self.lb_total.setText(c_total)
        self.lb_status.setText(c_status)

    def sambungkan(self):
        nonota = self.lb_nota.text()
        query = QtSql.QSqlQuery("select * from dataPelanggan where nota = '"+nonota+"' ")
        while (query.next()):
            ln_nota = query.value(0)
            ln_nama = query.value(1)
            ln_hp = query.value(2)
            ln_alamat = query.value(3)
            cb_paket = query.value(4)
            sb_berat = query.value(5)
            sb_jumlah = query.value(6)
            date1 = query.value(9)
            date2 = query.value(10)
            ln_total = query.value(8)
            ln_status = query.value(7)

            self.lb_nota.setText(str(ln_nota))
            self.lb_nama.setText(str(ln_nama))
            self.lb_hp.setText(str(ln_hp))
            self.lb_alamat.setText(str(ln_alamat))
            self.lb_paket.setText(str(cb_paket))
            self.lb_berat.setText(str(sb_berat))
            self.lb_jumlah.setText(str(sb_jumlah))
            self.lb_masuk.setText(str(date1))
            self.lb_selesai.setText(str(date2))
            self.lb_total.setText(str(ln_total))
            self.lb_status.setText(str(ln_status))

    def kembali(self):
        self.bck = main2.Ui()
        self.hide()
        self.bck.show()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Cetak()
    sys.exit(app.exec_())
