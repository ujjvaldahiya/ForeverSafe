# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 460)
        MainWindow.setMinimumSize(QtCore.QSize(730, 460))
        MainWindow.setMaximumSize(QtCore.QSize(730, 460))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/logo_transparent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{\n"
"background-color: #2a2a2a;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.cpassin = QtWidgets.QLineEdit(self.centralwidget)
        self.cpassin.setGeometry(QtCore.QRect(260, 180, 281, 41))
        self.cpassin.setStyleSheet("QLineEdit#cpassin{\n"
"background-color: white;\n"
"color: black;\n"
"border-color: lightblue;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"}\n"
"QLineEdit#cpassin:focus{\n"
"border-color: blue;\n"
"}")
        self.cpassin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cpassin.setObjectName("cpassin")
        self.newphonein = QtWidgets.QLineEdit(self.centralwidget)
        self.newphonein.setGeometry(QtCore.QRect(260, 250, 281, 41))
        self.newphonein.setStyleSheet("QLineEdit#newphonein{\n"
"background-color: white;\n"
"color: black;\n"
"border-color: lightblue;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"}\n"
"QLineEdit#newphonein:focus{\n"
"border-color: blue;\n"
"}")
        self.newphonein.setObjectName("newphonein")
        self.savesavebtn = QtWidgets.QPushButton(self.centralwidget)
        self.savesavebtn.setGeometry(QtCore.QRect(550, 390, 111, 41))
        self.savesavebtn.setStyleSheet("QPushButton#savesavebtn{\n"
"background-color: #006ab6 ;\n"
"color: white;\n"
"border: none;\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#savesavebtn:hover{\n"
"background-color: #008be8;\n"
"}")
        self.savesavebtn.setObjectName("savesavebtn")
        self.saveuserbtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveuserbtn.setGeometry(QtCore.QRect(556, 40, 111, 41))
        self.saveuserbtn.setStyleSheet("QPushButton#saveuserbtn{\n"
"background-color: #006ab6 ;\n"
"color: white;\n"
"border: none;\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#saveuserbtn:hover{\n"
"background-color: #008be8;\n"
"}")
        self.saveuserbtn.setObjectName("saveuserbtn")
        self.newsavelbl = QtWidgets.QLabel(self.centralwidget)
        self.newsavelbl.setGeometry(QtCore.QRect(32, 390, 221, 41))
        self.newsavelbl.setStyleSheet("QLabel#newsavelbl{\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"color: white;\n"
"}")
        self.newsavelbl.setObjectName("newsavelbl")
        self.newemaillbl = QtWidgets.QLabel(self.centralwidget)
        self.newemaillbl.setGeometry(QtCore.QRect(30, 320, 221, 41))
        self.newemaillbl.setStyleSheet("QLabel#newemaillbl{\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"color: white;\n"
"}")
        self.newemaillbl.setObjectName("newemaillbl")
        self.saveemailbtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveemailbtn.setGeometry(QtCore.QRect(552, 320, 111, 41))
        self.saveemailbtn.setStyleSheet("QPushButton#saveemailbtn{\n"
"background-color: #006ab6 ;\n"
"color: white;\n"
"border: none;\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#saveemailbtn:hover{\n"
"background-color: #008be8;\n"
"}")
        self.saveemailbtn.setObjectName("saveemailbtn")
        self.newsavein = QtWidgets.QLineEdit(self.centralwidget)
        self.newsavein.setGeometry(QtCore.QRect(262, 390, 231, 41))
        self.newsavein.setStyleSheet("QLineEdit#newsavein{\n"
"background-color: white;\n"
"color: black;\n"
"border-color: lightblue;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"}\n"
"QLineEdit#newsavein:focus{\n"
"border-color: blue;\n"
"}")
        self.newsavein.setObjectName("newsavein")
        self.newuserin = QtWidgets.QLineEdit(self.centralwidget)
        self.newuserin.setGeometry(QtCore.QRect(264, 40, 281, 41))
        self.newuserin.setStyleSheet("QLineEdit#newuserin{\n"
"background-color: white;\n"
"color: black;\n"
"border-color: lightblue;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"}\n"
"QLineEdit#newuserin:focus{\n"
"border-color: blue;\n"
"}")
        self.newuserin.setObjectName("newuserin")
        self.cpasslbl = QtWidgets.QLabel(self.centralwidget)
        self.cpasslbl.setGeometry(QtCore.QRect(30, 180, 221, 41))
        self.cpasslbl.setStyleSheet("QLabel#cpasslbl{\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"color: white;\n"
"}")
        self.cpasslbl.setObjectName("cpasslbl")
        self.savephonebtn = QtWidgets.QPushButton(self.centralwidget)
        self.savephonebtn.setGeometry(QtCore.QRect(552, 250, 111, 41))
        self.savephonebtn.setStyleSheet("QPushButton#savephonebtn{\n"
"background-color: #006ab6 ;\n"
"color: white;\n"
"border: none;\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#savephonebtn:hover{\n"
"background-color: #008be8;\n"
"}")
        self.savephonebtn.setObjectName("savephonebtn")
        self.newuserlbl = QtWidgets.QLabel(self.centralwidget)
        self.newuserlbl.setGeometry(QtCore.QRect(34, 40, 221, 41))
        self.newuserlbl.setStyleSheet("QLabel#newuserlbl{\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"color: white;\n"
"}")
        self.newuserlbl.setObjectName("newuserlbl")
        self.newpasslbl = QtWidgets.QLabel(self.centralwidget)
        self.newpasslbl.setGeometry(QtCore.QRect(32, 110, 221, 41))
        self.newpasslbl.setStyleSheet("QLabel#newpasslbl{\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"color: white;\n"
"}")
        self.newpasslbl.setObjectName("newpasslbl")
        self.newemailin = QtWidgets.QLineEdit(self.centralwidget)
        self.newemailin.setGeometry(QtCore.QRect(260, 320, 281, 41))
        self.newemailin.setStyleSheet("QLineEdit#newemailin{\n"
"background-color: white;\n"
"color: black;\n"
"border-color: lightblue;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"}\n"
"QLineEdit#newemailin:focus{\n"
"border-color: blue;\n"
"}")
        self.newemailin.setObjectName("newemailin")
        self.newpassin = QtWidgets.QLineEdit(self.centralwidget)
        self.newpassin.setGeometry(QtCore.QRect(262, 110, 281, 41))
        self.newpassin.setStyleSheet("QLineEdit#newpassin{\n"
"background-color: white;\n"
"color: black;\n"
"border-color: lightblue;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"}\n"
"QLineEdit#newpassin:focus{\n"
"border-color: blue;\n"
"}")
        self.newpassin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newpassin.setObjectName("newpassin")
        self.savepassbtn = QtWidgets.QPushButton(self.centralwidget)
        self.savepassbtn.setGeometry(QtCore.QRect(552, 180, 111, 41))
        self.savepassbtn.setStyleSheet("QPushButton#savepassbtn{\n"
"background-color: #006ab6 ;\n"
"color: white;\n"
"border: none;\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#savepassbtn:hover{\n"
"background-color: #008be8;\n"
"}")
        self.savepassbtn.setObjectName("savepassbtn")
        self.newphonelbl = QtWidgets.QLabel(self.centralwidget)
        self.newphonelbl.setGeometry(QtCore.QRect(30, 250, 221, 41))
        self.newphonelbl.setStyleSheet("QLabel#newphonelbl{\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"color: white;\n"
"}")
        self.newphonelbl.setObjectName("newphonelbl")
        self.browsebtn = QtWidgets.QPushButton(self.centralwidget)
        self.browsebtn.setGeometry(QtCore.QRect(500, 390, 41, 41))
        self.browsebtn.setStyleSheet("QPushButton#browsebtn{\n"
"background-color: #006ab6 ;\n"
"color: white;\n"
"border: none;\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#browsebtn:hover{\n"
"background-color: #008be8;\n"
"}")
        self.browsebtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/browse-icon-7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browsebtn.setIcon(icon1)
        self.browsebtn.setObjectName("browsebtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Settings"))
        self.savesavebtn.setText(_translate("MainWindow", "Save"))
        self.saveuserbtn.setText(_translate("MainWindow", "Save"))
        self.newsavelbl.setText(_translate("MainWindow", "New save Directory  :"))
        self.newemaillbl.setText(_translate("MainWindow", "New Email                    :"))
        self.saveemailbtn.setText(_translate("MainWindow", "Save"))
        self.cpasslbl.setText(_translate("MainWindow", "Confirm Password    :"))
        self.savephonebtn.setText(_translate("MainWindow", "Save"))
        self.newuserlbl.setText(_translate("MainWindow", "New Username          :"))
        self.newpasslbl.setText(_translate("MainWindow", "New Password           :"))
        self.savepassbtn.setText(_translate("MainWindow", "Save"))
        self.newphonelbl.setText(_translate("MainWindow", "New Phone No.          :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

