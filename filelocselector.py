# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filelocselector.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_filelocselector(object):
    def setupUi(self, filelocselector):
        filelocselector.setObjectName("filelocselector")
        filelocselector.resize(531, 431)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(filelocselector.sizePolicy().hasHeightForWidth())
        filelocselector.setSizePolicy(sizePolicy)
        filelocselector.setMinimumSize(QtCore.QSize(531, 431))
        filelocselector.setMaximumSize(QtCore.QSize(531, 431))
        filelocselector.setStyleSheet("QWidget#filelocselector{\n"
"background-color: #2a2a2a;\n"
"}")
        self.backbtn = QtWidgets.QPushButton(filelocselector)
        self.backbtn.setGeometry(QtCore.QRect(190, 250, 121, 41))
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
        self.finishbtn = QtWidgets.QPushButton(filelocselector)
        self.finishbtn.setGeometry(QtCore.QRect(320, 250, 121, 41))
        self.finishbtn.setStyleSheet("QPushButton#finishbtn{\n"
"background-color: #006ab6 ;\n"
"color: white;\n"
"border: none;\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#finishbtn:hover{\n"
"background-color: #008be8;\n"
"}")
        self.finishbtn.setObjectName("finishbtn")
        self.title = QtWidgets.QLabel(filelocselector)
        self.title.setGeometry(QtCore.QRect(100, 140, 338, 27))
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
        self.savelocin = QtWidgets.QLineEdit(filelocselector)
        self.savelocin.setGeometry(QtCore.QRect(100, 190, 281, 31))
        self.savelocin.setStyleSheet("QLineEdit#savelocin{\n"
"background-color: white;\n"
"color: black;\n"
"border-color: lightblue;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"}\n"
"QLineEdit#savelocin:focus{\n"
"border-color: blue;\n"
"}")
        self.savelocin.setPlaceholderText("")
        self.savelocin.setText(os.getcwd()+"\\userfiles")
        self.savelocin.setObjectName("savelocin")
        self.browsebtn = QtWidgets.QPushButton(filelocselector)
        self.browsebtn.setGeometry(QtCore.QRect(390, 190, 51, 31))
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/browse-icon-7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browsebtn.setIcon(icon)
        self.browsebtn.setObjectName("browsebtn")
        self.errorlbl = QtWidgets.QLabel(filelocselector)
        self.errorlbl.setGeometry(QtCore.QRect(140, 100, 261, 31))
        self.errorlbl.setStyleSheet("QLabel#errorlbl{\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"color: red;\n"
"}")
        self.errorlbl.setText("")
        self.errorlbl.setObjectName("errorlbl")

        self.retranslateUi(filelocselector)
        QtCore.QMetaObject.connectSlotsByName(filelocselector)

    def retranslateUi(self, filelocselector):
        _translate = QtCore.QCoreApplication.translate
        filelocselector.setWindowTitle(_translate("filelocselector", "Form"))
        self.backbtn.setText(_translate("filelocselector", "Back"))
        self.finishbtn.setText(_translate("filelocselector", "Finish"))
        self.title.setText(_translate("filelocselector", "Select location for encrypted files"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    filelocselector = QtWidgets.QWidget()
    ui = Ui_filelocselector()
    ui.setupUi(filelocselector)
    filelocselector.show()
    sys.exit(app.exec_())

