# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Python\SafeWare\progress.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_progresswindow(object):
    def setupUi(self, progresswindow):
        progresswindow.setObjectName("progresswindow")
        progresswindow.resize(531, 275)
        progresswindow.setMinimumSize(QtCore.QSize(531, 275))
        progresswindow.setMaximumSize(QtCore.QSize(531, 275))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/logo_transparent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        progresswindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(progresswindow)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{\n"
"background-color: #2a2a2a;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 160, 491, 23))
        self.progressBar.setStyleSheet("QProgressBar:horizontal {\n"
"border: 1px solid #006ab6;\n"
"background: white;\n"
"padding: 1px;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"background: #006ab6;\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.filelbl = QtWidgets.QLabel(self.centralwidget)
        self.filelbl.setGeometry(QtCore.QRect(20, 90, 70, 24))
        self.filelbl.setStyleSheet("QLabel#filelbl{\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"color: white;\n"
"}")
        self.filelbl.setObjectName("filelbl")
        self.currentfilelbl = QtWidgets.QLabel(self.centralwidget)
        self.currentfilelbl.setGeometry(QtCore.QRect(20, 120, 211, 24))
        self.currentfilelbl.setStyleSheet("QLabel#currentfilelbl{\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"color: white;\n"
"}")
        self.currentfilelbl.setObjectName("currentfilelbl")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(140, 30, 248, 27))
        self.title.setStyleSheet("QLabel#title{\n"
"font: 57 12pt \"Montserrat Medium\";\n"
"color: white;\n"
"}")
        self.title.setObjectName("title")
        self.bgbtn = QtWidgets.QPushButton(self.centralwidget)
        self.bgbtn.setGeometry(QtCore.QRect(390, 210, 121, 35))
        self.bgbtn.setStyleSheet("QPushButton#bgbtn{\n"
"background-color: #006ab6 ;\n"
"color: white;\n"
"border: none;\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#bgbtn:hover{\n"
"background-color: #008be8;\n"
"}")
        self.bgbtn.setObjectName("bgbtn")
        self.cancelbtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelbtn.setGeometry(QtCore.QRect(130, 210, 121, 35))
        self.cancelbtn.setStyleSheet("QPushButton#cancelbtn{\n"
"background-color: #4a4a4a;\n"
"color: white;\n"
"border: none;\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#cancelbtn:hover{\n"
"background-color: #787878;\n"
"}")
        self.cancelbtn.setObjectName("cancelbtn")
        self.pausebtn = QtWidgets.QPushButton(self.centralwidget)
        self.pausebtn.setGeometry(QtCore.QRect(260, 210, 121, 35))
        self.pausebtn.setStyleSheet("QPushButton#pausebtn{\n"
"background-color: #4a4a4a;\n"
"color: white;\n"
"border: none;\n"
"font: 57 10pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#pausebtn:hover{\n"
"background-color: #787878;\n"
"}")
        self.pausebtn.setObjectName("pausebtn")
        progresswindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(progresswindow)
        QtCore.QMetaObject.connectSlotsByName(progresswindow)

    def retranslateUi(self, progresswindow):
        _translate = QtCore.QCoreApplication.translate
        progresswindow.setWindowTitle(_translate("progresswindow", "Progress"))
        self.filelbl.setText(_translate("progresswindow", ""))
        self.currentfilelbl.setText(_translate("progresswindow", ""))
        self.title.setText(_translate("progresswindow", "File Encryption Progress"))
        self.bgbtn.setText(_translate("progresswindow", "Background"))
        self.cancelbtn.setText(_translate("progresswindow", "Cancel"))
        self.pausebtn.setText(_translate("progresswindow", "Pause"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    progresswindow = QtWidgets.QMainWindow()
    ui = Ui_progresswindow()
    ui.setupUi(progresswindow)
    progresswindow.show()
    sys.exit(app.exec_())

