# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verifyemail.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(419, 169)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{\n"
"background-color: #2a2a2a;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(140, 40, 145, 27))
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
        self.verifyotp = QtWidgets.QPushButton(self.centralwidget)
        self.verifyotp.setGeometry(QtCore.QRect(240, 90, 101, 31))
        self.verifyotp.setStyleSheet("QPushButton#verifyotp{\n"
"background-color: #006ab6 ;\n"
"color: white;\n"
"border: none;\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#verifyotp:hover{\n"
"background-color: #008be8;\n"
"}")
        self.verifyotp.setObjectName("verifyotp")
        self.otpin = QtWidgets.QLineEdit(self.centralwidget)
        self.otpin.setGeometry(QtCore.QRect(80, 90, 141, 31))
        self.otpin.setStyleSheet("QLineEdit#otpin{\n"
"background-color: white;\n"
"color: black;\n"
"border-color: lightblue;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"}\n"
"QLineEdit#otinp:focus{\n"
"border-color: blue;\n"
"}")
        self.otpin.setObjectName("otpin")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Verify Email Id"))
        self.verifyotp.setText(_translate("MainWindow", "Verify"))
        self.otpin.setPlaceholderText(_translate("MainWindow", "Enter OTP "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

