# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Python\SafeWare\regwidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_regwidget(object):
    def setupUi(self, regwidget):
        regwidget.setObjectName("regwidget")
        regwidget.resize(531, 431)
        regwidget.setMinimumSize(QtCore.QSize(531, 431))
        regwidget.setMaximumSize(QtCore.QSize(531, 431))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/resources/logo_transparent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        regwidget.setWindowIcon(icon)
        regwidget.setStyleSheet("QWidget#regwidget{\n"
"background-color: #2a2a2a;\n"
"}")
        self.emailin = QtWidgets.QLineEdit(regwidget)
        self.emailin.setGeometry(QtCore.QRect(250, 220, 261, 31))
        self.emailin.setStyleSheet("QLineEdit#emailin{\n"
"background-color: white;\n"
"color: black;\n"
"border-color: lightblue;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"}\n"
"QLineEdit#emailin:focus{\n"
"border-color: blue;\n"
"}")
        self.emailin.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.emailin.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'), self.emailin))
        self.emailin.setObjectName("emailin")
        self.passlbl = QtWidgets.QLabel(regwidget)
        self.passlbl.setGeometry(QtCore.QRect(20, 120, 211, 26))
        self.passlbl.setStyleSheet("QLabel#passlbl{\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"color: white;\n"
"}")
        self.passlbl.setObjectName("passlbl")
        self.userlbl = QtWidgets.QLabel(regwidget)
        self.userlbl.setGeometry(QtCore.QRect(21, 70, 211, 26))
        self.userlbl.setStyleSheet("QLabel#userlbl{\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"color: white;\n"
"}")
        self.userlbl.setObjectName("userlbl")
        self.mobilein = QtWidgets.QLineEdit(regwidget)
        self.mobilein.setGeometry(QtCore.QRect(250, 270, 261, 31))
        self.mobilein.setStyleSheet("QLineEdit#mobilein{\n"
"background-color: white;\n"
"color: black;\n"
"border-color: lightblue;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"}\n"
"QLineEdit#mobilein:focus{\n"
"border-color: blue;\n"
"}")
        self.mobilein.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.mobilein.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp('^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'), self.mobilein))
        self.mobilein.setObjectName("mobilein")
        self.joinbtn = QtWidgets.QPushButton(regwidget)
        self.joinbtn.setGeometry(QtCore.QRect(390, 320, 121, 41))
        self.joinbtn.setStyleSheet("QPushButton#joinbtn{\n"
"background-color: #006ab6 ;\n"
"color: white;\n"
"border: none;\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#joinbtn:hover{\n"
"background-color: #008be8;\n"
"}")
        self.joinbtn.setObjectName("joinbtn")
        self.passin = QtWidgets.QLineEdit(regwidget)
        self.passin.setGeometry(QtCore.QRect(250, 120, 261, 31))
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
        self.passconf = QtWidgets.QLineEdit(regwidget)
        self.passconf.setGeometry(QtCore.QRect(250, 170, 261, 31))
        self.passconf.setStyleSheet("QLineEdit#passconf{\n"
"background-color: white;\n"
"color: black;\n"
"border-color: lightblue;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"}\n"
"QLineEdit#passconf:focus{\n"
"border-color: blue;\n"
"}")
        self.passconf.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passconf.setObjectName("passconf")
        self.emaillbl = QtWidgets.QLabel(regwidget)
        self.emaillbl.setGeometry(QtCore.QRect(20, 220, 211, 26))
        self.emaillbl.setStyleSheet("QLabel#emaillbl{\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"color: white;\n"
"}")
        self.emaillbl.setObjectName("emaillbl")
        self.userin = QtWidgets.QLineEdit(regwidget)
        self.userin.setGeometry(QtCore.QRect(250, 70, 261, 31))
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
        self.resetbtn = QtWidgets.QPushButton(regwidget)
        self.resetbtn.setGeometry(QtCore.QRect(250, 320, 121, 41))
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
        self.mobilelbl = QtWidgets.QLabel(regwidget)
        self.mobilelbl.setGeometry(QtCore.QRect(20, 270, 211, 26))
        self.mobilelbl.setStyleSheet("QLabel#mobilelbl{\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"color: white;\n"
"}")
        self.mobilelbl.setObjectName("mobilelbl")
        self.passconfirmlbl = QtWidgets.QLabel(regwidget)
        self.passconfirmlbl.setGeometry(QtCore.QRect(20, 170, 211, 26))
        self.passconfirmlbl.setStyleSheet("QLabel#passconfirmlbl{\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"color: white;\n"
"}")
        self.passconfirmlbl.setObjectName("passconfirmlbl")
        self.errorlbl = QtWidgets.QLabel(regwidget)
        self.errorlbl.setGeometry(QtCore.QRect(244, 30, 271, 20))
        self.errorlbl.setStyleSheet("QLabel#errorlbl{\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"color: red;\n"
"}")
        self.errorlbl.setText("")
        self.errorlbl.setObjectName("errorlbl")

        self.retranslateUi(regwidget)
        QtCore.QMetaObject.connectSlotsByName(regwidget)

    def retranslateUi(self, regwidget):
        _translate = QtCore.QCoreApplication.translate
        regwidget.setWindowTitle(_translate("regwidget", "Register"))
        self.passlbl.setText(_translate("regwidget", "Master Password     :"))
        self.userlbl.setText(_translate("regwidget", "User                              :"))
        self.joinbtn.setText(_translate("regwidget", "Join"))
        self.emaillbl.setText(_translate("regwidget", "Email                            :"))
        self.resetbtn.setText(_translate("regwidget", "Reset"))
        self.mobilelbl.setText(_translate("regwidget", "Mobile No.                  :"))
        self.passconfirmlbl.setText(_translate("regwidget", "Confirm Password  :"))

#import Logo

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    regwidget = QtWidgets.QWidget()
    ui = Ui_regwidget()
    ui.setupUi(regwidget)
    regwidget.show()
    sys.exit(app.exec_())

