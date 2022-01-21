import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from home import *

class Login(QDialog):
    def __init__(self, parent = None):
        super(Login, self).__init__(parent)
        self.setWindowTitle("Konter Trunojoyo - Login")
        self.setWindowIcon(QtGui.QIcon('pythonLogo.png'))
        self.setStyleSheet("font-size: 14px;")
        self.setStyleSheet("QPushButton:hover {background-color: gold;}")
        self.menu_login()

    def menu_login(self):
        self.warning = QMessageBox()
        self.warning.setText("Masukkan Username & Password dengan Benar!")
        self.warning.setWindowTitle("Error")
        
        self.lbl = QLabel()
        self.lbl.setPixmap(QPixmap('login.png'))

        self.tittlee = QLabel('Konter Trunojoyo')
        self.user = QLabel()
        self.user.setPixmap(QPixmap('user.png'))
        self.passs = QLabel()
        self.passs.setPixmap(QPixmap('lock.png'))

        self.inpUser = QLineEdit()
        self.inpPasss = QLineEdit()

        self.login = QPushButton('LOGIN')
        self.signUp = QPushButton('SIGN UP')
        
        self.inpUser.setStyleSheet("QLineEdit {"
                                    "color: white;"
                                    "font: 15pt;"
                                    "border-radius: 10px;"
                                    "padding: 0 8px;"
                                    "background: rgb(20, 20, 40);"
                                    "}")
        self.inpPasss.setStyleSheet("QLineEdit {"
                                    "color: white;"
                                    "font: 15pt;"
                                    "border-radius: 10px;"
                                    "padding: 0 8px;"
                                    "background: rgb(20, 20, 40);"
                                    "}")
        self.inpUser.setFocus(True)

        self.login.setStyleSheet("color: black;"
                                      "font: 15pt;"
                                      "border: 2px solid gold;"
                                      "padding: 5px;"
                                      "border-radius: 3px;"
                                      "opacity: 200;"
                                      "")
        self.signUp.setStyleSheet("color: black;"
                                      "font: 15pt;"
                                      "border: 2px solid gold;"
                                      "padding: 5px;"
                                      "border-radius: 3px;"
                                      "opacity: 200;"
                                      "")

        self.tittlee.setStyleSheet("font-size: 28px; color: gold; font-family: Segoe Script;")
        self.tittlee.setAlignment(Qt.AlignCenter)
        self.lbl.setAlignment(Qt.AlignCenter)
        self.inpPasss.setEchoMode(QLineEdit.Password)

        gL = QGridLayout()
        gL.addWidget(self.lbl, 0, 0, 1, 0)
        gL.addWidget(self.tittlee, 1, 0, 1, 0)
        gL.addWidget(self.user, 2, 0)
        gL.addWidget(self.inpUser, 2, 1)
        gL.addWidget(self.passs, 4, 0)
        gL.addWidget(self.inpPasss, 4, 1)
        gL.addWidget(self.signUp, 5, 0)
        gL.addWidget(self.login, 5, 1)
        self.setLayout(gL)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Login()

if win.exec_() == QDialog.Accepted:
    me = Home()
    me.show()
    sys.exit(app.exec_())