# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Python\SafeWare\verifycontact.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_verifycontact(object):
    def setupUi(self, verifycontact):
        verifycontact.setObjectName("verifycontact")
        verifycontact.resize(531, 431)
        verifycontact.setMinimumSize(QtCore.QSize(531, 431))
        verifycontact.setMaximumSize(QtCore.QSize(531, 431))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/resources/logo_transparent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        verifycontact.setWindowIcon(icon)
        verifycontact.setStyleSheet("QWidget#verifycontact{\n"
"background-color: #2a2a2a;\n"
"}")
        self.mobilelbl = QtWidgets.QLabel(verifycontact)
        self.mobilelbl.setGeometry(QtCore.QRect(20, 220, 159, 27))
        self.mobilelbl.setStyleSheet("QLabel#mobilelbl{\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"color: white;\n"
"}")
        self.mobilelbl.setObjectName("mobilelbl")
        self.title = QtWidgets.QLabel(verifycontact)
        self.title.setGeometry(QtCore.QRect(120, 80, 297, 27))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.title.setFont(font)
        self.title.setStyleSheet("QLabel#title{\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"color: white;\n"
"}")
        self.title.setObjectName("title")
        self.otpmobile = QtWidgets.QLineEdit(verifycontact)
        self.otpmobile.setGeometry(QtCore.QRect(200, 220, 141, 31))
        self.otpmobile.setStyleSheet("QLineEdit#otpmobile{\n"
"background-color: white;\n"
"color: black;\n"
"border-color: lightblue;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"}\n"
"QLineEdit#otpmobile:focus{\n"
"border-color: blue;\n"
"}")
        self.otpmobile.setObjectName("otpmobile")
        self.verifyemail = QtWidgets.QPushButton(verifycontact)
        self.verifyemail.setGeometry(QtCore.QRect(360, 170, 101, 31))
        self.verifyemail.setStyleSheet("QPushButton#verifyemail{\n"
"background-color: #006ab6 ;\n"
"color: white;\n"
"border: none;\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#verifyemail:hover{\n"
"background-color: #008be8;\n"
"}")
        self.verifyemail.setObjectName("verifyemail")
        self.verifymobile = QtWidgets.QPushButton(verifycontact)
        self.verifymobile.setGeometry(QtCore.QRect(360, 220, 101, 31))
        self.verifymobile.setStyleSheet("QPushButton#verifymobile{\n"
"background-color: #006ab6 ;\n"
"color: white;\n"
"border: none;\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#verifymobile:hover{\n"
"background-color: #008be8;\n"
"}")
        self.verifymobile.setObjectName("verifymobile")
        self.phone_t = QtWidgets.QLabel(verifycontact)
        self.phone_t.setGeometry(QtCore.QRect(480, 220, 30, 30))
        self.phone_t.setText("")
        self.phone_t.setScaledContents(True)
        self.phone_t.setObjectName("phone_t")
        self.emailotp = QtWidgets.QLineEdit(verifycontact)
        self.emailotp.setGeometry(QtCore.QRect(200, 170, 141, 31))
        self.emailotp.setStyleSheet("QLineEdit#emailotp{\n"
"background-color: white;\n"
"color: black;\n"
"border-color: lightblue;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"}\n"
"QLineEdit#emailotp:focus{\n"
"border-color: blue;\n"
"}")
        self.emailotp.setObjectName("emailotp")
        self.email_t = QtWidgets.QLabel(verifycontact)
        self.email_t.setGeometry(QtCore.QRect(480, 170, 30, 30))
        self.email_t.setText("")
        self.email_t.setScaledContents(True)
        self.email_t.setObjectName("email_t")
        self.continuebtn = QtWidgets.QPushButton(verifycontact)
        self.continuebtn.setGeometry(QtCore.QRect(340, 300, 121, 41))
        self.continuebtn.setStyleSheet("QPushButton#continuebtn{\n"
"background-color: #006ab6 ;\n"
"color: white;\n"
"border: none;\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#continuebtn:hover{\n"
"background-color: #008be8;\n"
"}")
        self.continuebtn.setObjectName("continuebtn")
        self.emaillbl = QtWidgets.QLabel(verifycontact)
        self.emaillbl.setGeometry(QtCore.QRect(20, 170, 158, 27))
        self.emaillbl.setStyleSheet("QLabel#emaillbl{\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"color: white;\n"
"}")
        self.emaillbl.setObjectName("emaillbl")
        self.backbtn = QtWidgets.QPushButton(verifycontact)
        self.backbtn.setGeometry(QtCore.QRect(200, 300, 121, 41))
        self.backbtn.setStyleSheet("QPushButton#backbtn{\n"
"background-color: #4a4a4a;\n"
"color: white;\n"
"border: none;\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#backbtn:hover{\n"
"background-color: #787878;\n"
"}")
        self.backbtn.setObjectName("backbtn")
        self.errorlbl = QtWidgets.QLabel(verifycontact)
        self.errorlbl.setGeometry(QtCore.QRect(200, 120, 261, 31))
        self.errorlbl.setStyleSheet("QLabel#errorlbl{\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"color: red;\n"
"}")
        self.errorlbl.setText("")
        self.errorlbl.setObjectName("errorlbl")

        self.retranslateUi(verifycontact)
        QtCore.QMetaObject.connectSlotsByName(verifycontact)

    def retranslateUi(self, verifycontact):
        _translate = QtCore.QCoreApplication.translate
        verifycontact.setWindowTitle(_translate("verifycontact", "verifycontact"))
        self.mobilelbl.setText(_translate("verifycontact", "Mobile No.         :"))
        self.title.setText(_translate("verifycontact", "Verify Mobile no and Email id"))
        self.otpmobile.setPlaceholderText(_translate("verifycontact", "Enter OTP "))
        self.verifyemail.setText(_translate("verifycontact", "Verify"))
        self.verifymobile.setText(_translate("verifycontact", "Verify"))
        self.emailotp.setPlaceholderText(_translate("verifycontact", "Enter OTP "))
        self.continuebtn.setText(_translate("verifycontact", "Continue"))
        self.emaillbl.setText(_translate("verifycontact", "Email                   :"))
        self.backbtn.setText(_translate("verifycontact", "Back"))

#import Logo

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    verifycontact = QtWidgets.QWidget()
    ui = Ui_verifycontact()
    ui.setupUi(verifycontact)
    verifycontact.show()
    sys.exit(app.exec_())

