import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtSql import *

from main import *

class Rekapitulasi(QWidget):

    def __init__(self, parent = None):
        super(Rekapitulasi, self).__init__(parent)
        self.setWindowTitle("Desa Pintar - Rekapitulasi")
        self.setGeometry(150, 50, 900, 220)
        self.setWindowIcon(QtGui.QIcon('gambar/pythonLogo.png'))
        self.setStyleSheet("font-size: 17px; margin: 10px 35px;")
        self.windows()

    def windows(self):
        self.judul1 = QLabel('Data Warga Desa Sedati Agung')
        self.judul2 = QLabel('Sedati-Sidoarjo-Jawa Timur')

        self.penduduk = QLabel('Jumlah Penduduk')
        self.pria = QLabel('Jumlah Pria')
        self.wanita = QLabel('Jumlah Wanita')
        self.wargaTetap = QLabel('Jumlah Warga Tetap')
        self.pendatang = QLabel('Jumlah Pendatang')

        self.blank = QLabel()
        self.btn = QPushButton('REKAP')

        self.hslPenduduk = QLabel()
        self.hslPria = QLabel()
        self.hslWanita = QLabel()
        self.hslWargaTetap = QLabel()
        self.hslPendatang = QLabel()

        tempat = ["01","02","03","04","05"]
        self.inpTempat = QComboBox()
        for i in tempat:
            self.inpTempat.addItem(i)

        self.judul1.setStyleSheet("font-size: 30px; font-weight: bold; color: brown;")
        self.judul2.setStyleSheet("font-size: 30px; font-weight: bold; color: brown;")
        self.judul1.setAlignment(Qt.AlignCenter)
        self.judul2.setAlignment(Qt.AlignCenter)

        self.btn.clicked.connect(self.hitung)

        self.gL = QGridLayout()
        self.gL.addWidget(self.judul1, 0, 0, 1, 0)
        self.gL.addWidget(self.judul2, 1, 0, 1, 0)
        self.gL.addWidget(self.blank, 2, 0, 1, 0)
        self.gL.addWidget(self.penduduk, 3, 0)
        self.gL.addWidget(self.hslPenduduk, 3, 1)
        self.gL.addWidget(self.inpTempat, 4, 1)
        self.gL.addWidget(self.btn, 4, 2)
        self.gL.addWidget(self.blank, 5, 0)
        self.gL.addWidget(self.pria, 6, 0)
        self.gL.addWidget(self.hslPria, 6, 1)
        self.gL.addWidget(self.wanita, 7, 0)
        self.gL.addWidget(self.hslWanita, 7, 1)
        self.gL.addWidget(self.wargaTetap, 8, 0)
        self.gL.addWidget(self.hslWargaTetap, 8, 1)
        self.gL.addWidget(self.pendatang, 9, 0)
        self.gL.addWidget(self.hslPendatang, 9, 1)
        self.setLayout(self.gL)

    def hitung(self):
        desa = {"Pria": 0,"Wanita":0}
        keterangan = {"Tetap":0, "Sementara":0}
        query = QSqlQuery()
        query.prepare("SELECT * FROM penduduk  WHERE RT = :tempat")
        query.bindValue(":tempat", str(self.inpTempat.currentText()))
        yreuq = QSqlQuery()
        yreuq.prepare("SELECT COUNT(NIK) FROM penduduk")
        if query.exec_():
            while query.next():
                for i in desa.keys():
                    if query.value(9) == i:
                        desa[query.value(9)] += 1
                for j in keterangan.keys():
                    if query.value(13) == j:
                        keterangan[query.value(13)] +=1
            if yreuq.exec_():
                while yreuq.next():
                    self.jumlah = yreuq.value(0)
        else:
            print(query.lastError().text())
        self.hslPenduduk.setText(str(self.jumlah))
        self.hslPria.setText(str(desa.get("Pria")))
        self.hslWanita.setText(str(desa.get("Wanita")))
        self.hslWargaTetap.setText(str(keterangan.get("Tetap")))
        self.hslPendatang.setText(str(keterangan.get("Sementara")))
        

def main():
    app = QApplication(sys.argv)
    win = Rekapitulasi()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 