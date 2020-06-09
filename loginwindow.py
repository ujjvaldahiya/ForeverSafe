# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Python\SafeWare\loginwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import json
import os
import sys
import mainwindowblack
from functools import partial
import uinfdecrypt

class Ui_LoginWindow(object):
    
    def setupUi(self, LoginWindow):
        self.variablesinit()
        
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(800, 450)
        LoginWindow.setMinimumSize(QtCore.QSize(800, 450))
        LoginWindow.setMaximumSize(QtCore.QSize(800, 450))
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        LoginWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/logo_transparent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-color: #2a2a2a;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setStyleSheet("b")
        self.centralwidget.setObjectName("centralwidget")
        self.userlbl = QtWidgets.QLabel(self.centralwidget)
        self.userlbl.setGeometry(QtCore.QRect(341, 140, 174, 26))
        self.userlbl.setStyleSheet("QLabel#userlbl{\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"color: white;\n"
"}")
        self.userlbl.setObjectName("userlbl")
        self.passlbl = QtWidgets.QLabel(self.centralwidget)
        self.passlbl.setGeometry(QtCore.QRect(340, 200, 176, 26))
        self.passlbl.setStyleSheet("QLabel#passlbl{\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"color: white;\n"
"}")
        self.passlbl.setObjectName("passlbl")
        self.userin = QtWidgets.QLineEdit(self.centralwidget)
        self.userin.setGeometry(QtCore.QRect(530, 140, 251, 31))
        self.userin.setStyleSheet("QLineEdit#userin{\n"
"background-color: white;\n"
"color: black;\n"
"border-color: lightblue;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"}\n"
"QLineEdit#userin:focus{\n"
"border-color: blue;\n"
"}")
        self.userin.setObjectName("userin")
        self.passin = QtWidgets.QLineEdit(self.centralwidget)
        self.passin.setGeometry(QtCore.QRect(530, 200, 251, 31))
        self.passin.setStyleSheet("QLineEdit#passin{\n"
"background-color: white;\n"
"color: black;\n"
"border-color: lightblue;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"}\n"
"QLineEdit#passin:focus{\n"
"border-color: blue;\n"
"}")
        self.passin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passin.setObjectName("passin")
        self.resetbtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetbtn.setGeometry(QtCore.QRect(530, 260, 121, 41))
        self.resetbtn.setStyleSheet("QPushButton#resetbtn{\n"
"background-color: #4a4a4a;\n"
"color: white;\n"
"border: none;\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#resetbtn:hover{\n"
"background-color: #787878;\n"
"}")
        self.resetbtn.setObjectName("resetbtn")
        self.loginbtn = QtWidgets.QPushButton(self.centralwidget)
        self.loginbtn.setGeometry(QtCore.QRect(660, 260, 121, 41))
        self.loginbtn.setStyleSheet("QPushButton#loginbtn{\n"
"background-color: #006ab6 ;\n"
"color: white;\n"
"border: none;\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#loginbtn:hover{\n"
"background-color: #008be8;\n"
"}")
        self.loginbtn.setObjectName("loginbtn")
        self.forgotpass = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.forgotpass.setGeometry(QtCore.QRect(570, 310, 172, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.forgotpass.setFont(font)
        self.forgotpass.setStyleSheet("QCommandLinkButton#forgotpass{\n"
"color: white;\n"
"}")
        self.forgotpass.setDefault(False)
        self.forgotpass.setObjectName("forgotpass")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 80, 300, 300))
        self.logo.setStyleSheet("")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("logo_transparent.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.errorlbl = QtWidgets.QLabel(self.centralwidget)
        self.errorlbl.setGeometry(QtCore.QRect(340, 80, 450, 27))
        self.errorlbl.setStyleSheet("QLabel#errorlbl{\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"color: red;\n"
"}")
        self.errorlbl.setText("")
        self.errorlbl.setObjectName("errorlbl")
        
        self.addeventlistners(LoginWindow)
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "ForeveSafe"))
        self.userlbl.setText(_translate("LoginWindow", "User                        :"))
        self.passlbl.setText(_translate("LoginWindow", "Password              :"))
        self.resetbtn.setText(_translate("LoginWindow", "Reset"))
        self.loginbtn.setText(_translate("LoginWindow", "Unlock"))
        self.forgotpass.setText(_translate("LoginWindow", "Forgot Password"))
        
    def variablesinit(self):
        self.logincount = 0
    
    def addeventlistners(self, LoginWindow):
        self.loginbtn.clicked.connect(partial(self.unlockbtnclicked, LoginWindow))
        self.resetbtn.clicked.connect(self.resetbtnclicked)

    def unlockbtnclicked(self, LoginWindow):
        # 1->initialize keygen
        # 2->accept password
        # 3-> generate key
        # 4->try to decrypt userinfo
        # 5->if successful login
        #    else retrylogin
        # 6->after 5 incorrect tries wipe all data
        uinf = uinfdecrypt.UserInfoHandler(self.userin.text(), self.passin.text())
        userinfo = uinf.decryptUinfo()
        print(userinfo)
        if not type(userinfo) == bool:
            print(True)
            if (userinfo['username'].strip() == self.userin.text() and userinfo['password'] == self.passin.text()):
                self.mainwin = QtWidgets.QMainWindow()
                self.mainwinui = mainwindowblack.Ui_foreversafe(userinfo["username"], userinfo["password"])
                self.mainwinui.setupUi(self.mainwin)
                self.mainwin.show()
                LoginWindow.hide()
            else:
                self.logincount +=1
                self.errorlbl.setText("Invalid credentials! %s attempts remaining"%str(5 - self.logincount))
                return
        else:
            self.logincount +=1
            self.errorlbl.setText("Invalid credentials! %s attempts remaining"%str(5-self.logincount))
            return
                
        
    def resetbtnclicked(self):
        self.userin.setText("")
        self.passin.setText("")
        self.errorlbl.setText("")


"""def resource_path(relative_path):
     if hasattr(sys, '_MEIPASS'):
         return os.path.join(sys._MEIPASS, relative_path)
     return os.path.join(os.path.abspath("."), relative_path)

logo = resource_path("logo_transparent.png")"""
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())

