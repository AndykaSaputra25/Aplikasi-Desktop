import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

from main import *
from rekap import *
from petugas import *
from bantuan import *

class Home(QMainWindow):

    def __init__(self, parent = None):
        super(Home, self).__init__(parent)
        self.setWindowTitle("Desa Pintar - Home")
        self.setGeometry(150, 50, 400, 220)
        self.setWindowIcon(QtGui.QIcon('gambar/pythonLogo.png'))
        self.setStyleSheet("font-size: 17px")
        self.windows()

    def windows(self):
        self.lbl = QLabel()
        self.lbl.setPixmap(QPixmap('gambar/tampilan.png'))
        self.setCentralWidget(self.lbl)
        self.menuBarr()

    def menuBarr(self):
        self.bar = self.menuBar()
        self.home = self.bar.addMenu('HOME')
        self.main = self.bar.addMenu('MAIN')
        self.rekap = self.bar.addMenu('REKAPITULASI')
        self.perangkat = self.bar.addMenu('PERANGKAT')
        self.help = self.bar.addMenu('BANTUAN')
        
        self.rumah = QAction('Home Page')
        self.utama = QAction('Main Page')
        self.laporan = QAction('Rekapitulasi Page')
        self.perangkatDesa = QAction('Perangkat Page')
        self.tolong = QAction('Help Page')

        self.main.addAction(self.utama)
        self.rekap.addAction(self.laporan)
        self.perangkat.addAction(self.perangkatDesa)
        self.help.addAction(self.tolong)

        self.utama.triggered.connect(self.koneksi_main)
        self.laporan.triggered.connect(self.koneksi_rekap)
        self.perangkatDesa.triggered.connect(self.koneksi_perangkat)
        self.tolong.triggered.connect(self.koneksi_help)

    def koneksi_main(self):
        self.start_main = Main()
        self.start_main.show()

    def koneksi_rekap(self):
        self.start_rekap = Rekapitulasi()
        self.start_rekap.show()

    def koneksi_perangkat(self):
        self.start_perangkat = Petugas()
        self.start_perangkat.show()

    def koneksi_help(self):
        self.start_help = Bantuan()
        self.start_help.show()

def main():
    app = QApplication(sys.argv)
    win = Home()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main() 