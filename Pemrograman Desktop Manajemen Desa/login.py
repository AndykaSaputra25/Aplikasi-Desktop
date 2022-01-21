import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from home import *

class Login(QDialog):
    def __init__(self, parent = None):
        super(Login, self).__init__(parent)
        self.setWindowTitle("Desa Pintar - Login")
        self.setWindowIcon(QtGui.QIcon('gambar/pythonLogo.png'))
        self.setStyleSheet("font-size: 14px")
        self.menu_login()

    def menu_login(self):
        self.lbl = QLabel()
        self.lbl.setPixmap(QPixmap('gambar/login.png'))

        self.tittlee = QLabel('DePin')
        self.user = QLabel('Username : ')
        self.passs = QLabel('Password : ')

        self.inpUser = QLineEdit()
        self.inpPasss = QLineEdit()

        self.login = QPushButton('LOGIN')

        self.tittlee.setStyleSheet("font-size: 28px; color: red; font-family: Segoe Script;")
        self.tittlee.setAlignment(Qt.AlignCenter)
        self.lbl.setAlignment(Qt.AlignCenter)
        self.inpPasss.setEchoMode(QLineEdit.Password)

        self.login.clicked.connect(self.login_koneksi)

        gL = QGridLayout()
        gL.addWidget(self.lbl, 0, 0, 1, 0)
        gL.addWidget(self.tittlee, 1, 0, 1, 0)
        gL.addWidget(self.user, 2, 0)
        gL.addWidget(self.inpUser, 2, 1)
        gL.addWidget(self.passs, 3, 0)
        gL.addWidget(self.inpPasss, 3, 1)
        gL.addWidget(self.login, 4, 0)
        self.setLayout(gL)

    def login_koneksi(self):
        if (self.inpUser.text() == 'admin' and self.inpPasss.text() == 'root'):
            self.accept()
        else :
            QMessageBox.about(self,"Error","Masukkan Username & Password dengan Benar!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Login()

if win.exec_() == QDialog.Accepted:
    me = Home()
    me.show()
    sys.exit(app.exec_())