import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtSql, QtGui


class Bantuan(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desa Pintar - Bantuan")
        self.setGeometry(150, 50, 400, 220)
        self.setWindowIcon(QtGui.QIcon('pythonLogo.png'))
        self.setStyleSheet("font-size: 17px")
        self.windows()
    
    def windows(self):
        self.judul = QLabel("Butuh Bantuan ?")
        self.lbl = QLabel("Mungkin dibawah ini adalah jawaban yang Anda cari")

        self.judul.setStyleSheet("font-size: 30px; font-weight: bold; color: brown;")

        self.menuGroupBox()
        self.createTopGroupBox()
        self.createBottomGroupBox()

        topLayout = QVBoxLayout()
        topLayout.addWidget(self.judul)
        topLayout.addWidget(self.lbl)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0)
        mainLayout.addWidget(self.iniMenu, 1, 0)
        mainLayout.addWidget(self.topLeftGroupBox, 2, 0)
        mainLayout.addWidget(self.topRightGroupBox, 3, 0)
        self.setLayout(mainLayout)
        
    def menuGroupBox(self):
        self.iniMenu = QGroupBox()
        tanya = QLabel('Bagaimana menambah data ?')
        jawab = QLabel('Pada halaman Home pilih menu Main dan isi semua inputan. Jika sudah klik Add pada bagian atas')

        tanya.setStyleSheet("font-size: 20px; font-weight: bold; color: blue;")

        layout = QVBoxLayout()
        layout.addWidget(tanya)
        layout.addWidget(jawab)
        self.iniMenu.setLayout(layout)

#__Group-1
    def createTopGroupBox(self):
        self.topLeftGroupBox = QGroupBox()

        tanya = QLabel('Bagaimana menacari data ?')
        jawab = QLabel('Pada halaman Home pilih menu Main dan cukup isi No. KK pada box Menu. Jika sudah klik Search pada bagian sampingnya')

        tanya.setStyleSheet("font-size: 20px; font-weight: bold; color: blue;")

        layout = QVBoxLayout()
        layout.addWidget(tanya)
        layout.addWidget(jawab)

        self.topLeftGroupBox.setLayout(layout)  

#__Group-2
    def createBottomGroupBox(self):
        self.topRightGroupBox = QGroupBox()

        tanya = QLabel('Bagaimana cara keluar dari aplikasi ?')
        jawab = QLabel('Pada bagian atas sebelah kanan terdapat simbol X, klik simbol tersebut maka akan keluar dari aplikasi')

        tanya.setStyleSheet("font-size: 20px; font-weight: bold; color: blue;")

        layout = QVBoxLayout()
        layout.addWidget(tanya)
        layout.addWidget(jawab)
        self.topRightGroupBox.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    win = Bantuan()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()    
