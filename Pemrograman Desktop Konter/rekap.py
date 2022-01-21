import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtSql import *

from main import *

class Rekapitulasi(QWidget):

    def __init__(self):
        super(Rekapitulasi, self).__init__()
        self.setWindowTitle("Desa Pintar - Rekapitulasi")
        self.setGeometry(150, 50, 400, 220)
        self.setWindowIcon(QtGui.QIcon('pythonLogo.png'))
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
        self.rtOne = QLabel('Jumlah RT 01')
        self.rtTwo = QLabel('Jumlah RT 02')
        self.rtTree = QLabel('Jumlah RT 03')
        self.rtFour = QLabel('Jumlah RT 04')
        self.rtFive = QLabel('Jumlah RT 05')

        self.blank = QLabel()
        self.btn = QPushButton('REKAP')

        self.hslPenduduk = QLabel('50')
        self.hslPria = QLabel('23')
        self.hslWanita = QLabel('27')
        self.hslWargaTetap = QLabel('33')
        self.hslPendatang = QLabel('17')
        self.hslRtOne = QLabel('9')
        self.hslRtTwo = QLabel('6')
        self.hslRtTree = QLabel('11')
        self.hslRtFour = QLabel('8')
        self.hslRtFive = QLabel('16')

        self.judul1.setStyleSheet("font-size: 30px; font-weight: bold; color: brown;")
        self.judul2.setStyleSheet("font-size: 30px; font-weight: bold; color: brown;")
        self.judul1.setAlignment(Qt.AlignCenter)
        self.judul2.setAlignment(Qt.AlignCenter)

        self.btn.clicked.connect(self.hitung)

        self.gL = QGridLayout()
        self.gL.addWidget(self.judul1, 0, 0, 1, 0)
        self.gL.addWidget(self.judul2, 1, 0, 1, 0)
        self.gL.addWidget(self.blank, 2, 0, 1, 0)
        self.gL.addWidget(self.btn, 3, 0)
        self.gL.addWidget(self.penduduk, 4, 0)
        self.gL.addWidget(self.pria, 4, 1)
        self.gL.addWidget(self.wanita, 4, 2)
        self.gL.addWidget(self.wargaTetap, 4, 3)
        self.gL.addWidget(self.pendatang, 4, 4)
        self.gL.addWidget(self.hslPenduduk, 5, 0)
        self.gL.addWidget(self.hslPria, 5, 1)
        self.gL.addWidget(self.hslWanita, 5, 2)
        self.gL.addWidget(self.hslWargaTetap, 5, 3)
        self.gL.addWidget(self.hslPendatang, 5, 4)
        self.gL.addWidget(self.blank, 6, 0, 1, 0)
        self.gL.addWidget(self.rtOne, 7, 0)
        self.gL.addWidget(self.rtTwo, 7, 1)
        self.gL.addWidget(self.rtTree, 7, 2)
        self.gL.addWidget(self.rtFour, 7, 3)
        self.gL.addWidget(self.rtFive, 7, 4)
        self.gL.addWidget(self.hslRtOne, 8, 0)
        self.gL.addWidget(self.hslRtTwo, 8, 1)
        self.gL.addWidget(self.hslRtTree, 8, 2)
        self.gL.addWidget(self.hslRtFour, 8, 3)
        self.gL.addWidget(self.hslRtFive, 8, 4)
        self.gL.addWidget(self.blank, 9, 0, 1, 0)
        
        self.setLayout(self.gL)

    def hitung(self):
        nik = {"NIK": 0}
    #     query = QSqlQuery()
    #     query.prepare("SELECT COUNT(NIK) "+" FROM pulsa")
    #     query.bindValue(":nik", nik)
    #     self.hslPenduduk.setText(str(nik.get("NIK")))
        

def main():
    app = QApplication(sys.argv)
    win = Rekapitulasi()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 