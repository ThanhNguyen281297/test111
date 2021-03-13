import sys
from tkinter import messagebox
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.QtWebEngineWidgets import*



class Loginpage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.resize(350,150)
        layout = QGridLayout()
        lbl_Username = QLabel('<font size="5"> Username </font>')
        self.txtUser = QLineEdit()
        layout.addWidget(lbl_Username, 0, 0)
        layout.addWidget(self.txtUser, 0, 1)
        lbl_Password = QLabel('<font size="5"> Password </font>')
        self.txtPassword = QLineEdit()
        self.txtPassword.setEchoMode(QLineEdit.Password)
        layout.addWidget(lbl_Password, 1, 0)
        layout.addWidget(self.txtPassword, 1, 1)
        btn_Login = QPushButton('Login')
        btn_Login.clicked.connect(self.login_here)
        layout.addWidget(btn_Login, 1, 0, 2, 2)
        self.setLayout(layout)
    def login_here(self):
        if self.txtUser.text() =="thanhnd" and self.txtPassword.text()=="123456":
            global form
            form = Main()
        if self.txtUser.text() =="" or self.txtPassword.text()=="":
            messagebox.showerror("","")
        if self.txtUser.text()!="thanhnd" or self.txtPassword.text()!="123456":
            messagebox.showerror("","")

class Main(QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        self.setWindowTitle('Test')
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://facebook.com'))
        self.setCentralWidget(self.browser)
        self.resize(1200,700)
        self.show()

app = QApplication(sys.argv)
form = Loginpage()
form.show()
sys.exit(app.exec_())