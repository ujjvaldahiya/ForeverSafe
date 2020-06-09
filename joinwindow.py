# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'joinwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from regwidget import Ui_regwidget
from verifycontact import Ui_verifycontact
from filelocselector import Ui_filelocselector
import SMS
import OTP
import EMail
import logging
import os
import json
from functools import partial
import mainwindowblack
import uinfdecrypt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.variableinit()
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 450)
        MainWindow.setMaximumSize(QtCore.QSize(800,450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/logo_transparent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{\n"
"background-color: #2a2a2a;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 90, 225, 225))
        self.logo.setStyleSheet("")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("resources/logo_transparent.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.mdi = QtWidgets.QMdiArea(self.centralwidget)
        self.mdi.setGeometry(QtCore.QRect(260, 10, 531, 431))
        self.mdi.setMaximumSize(QtCore.QSize(531, 431))
        self.mdi.setObjectName("mdi")
        self.subwin = QtWidgets.QMdiSubWindow(self.mdi)
        self.subwin.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint))
        self.regui = Ui_regwidget()
        self.regwid = QtWidgets.QWidget()
        self.regui.setupUi(self.regwid)
        self.verifyui = Ui_verifycontact()
        self.verifywid = QtWidgets.QWidget()
        self.verifyui.setupUi(self.verifywid)
        self.filelocselui = Ui_filelocselector()
        self.filelocselwid = QtWidgets.QWidget()
        self.filelocselui.setupUi(self.filelocselwid)
        
        self.setregwid()
        #self.setfilelocselectorwid()
        self.addeventlistners(MainWindow)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ForeverSafe"))
        
    def variableinit(self):
        self.passcopy = None
        self.password = None
        self.email = None
        self.username = None
        self.mobile = None
        self.otpemail = None
        self.otpmob = None
        self.message = "%s is your otp for verification on ForeverSafe"
        self.mobileverified = False
        self.emailverified = False
        self.saveloc = None
        self.userinfo = None
        
    def setregwid(self):
        self.subwin.setWidget(self.regwid)

    def setverifywid(self):
        self.subwin.setWidget(self.verifywid)
        
    def setfilelocselectorwid(self):
        self.subwin.setWidget(self.filelocselwid)
    
    def addeventlistners(self, MainWindow):
        self.regui.joinbtn.clicked.connect(self.joinclicked)
        self.verifyui.verifymobile.clicked.connect(self.verifymobileclicked)
        self.verifyui.verifyemail.clicked.connect(self.verifyemailclicked)
        self.regui.resetbtn.clicked.connect(self.regresetclicked)
        self.verifyui.backbtn.clicked.connect(self.verbackclicked)
        self.verifyui.continuebtn.clicked.connect(self.vercontinueclicked)
        self.filelocselui.browsebtn.clicked.connect(self.browsebtnclicked)
        self.filelocselui.finishbtn.clicked.connect(partial(self.filefinishbtnclicked, MainWindow))
        
    def joinclicked(self):
        if self.regui.passin.text()!= self.regui.passconf.text():
            self.regui.errorlbl.setText("Passwords didn't match!")
            self.regui.passconf.setText("")
            self.regui.passin.setText("")
            return
        
        if not self.regui.emailin.hasAcceptableInput():
            self.regui.errorlbl.setText("Invalid Email Id!")
            self.regui.emailin.setText("")
            return

        if not self.regui.mobilein.hasAcceptableInput():
            self.regui.errorlbl.setText("Invalid Mobile no.!")
            self.regui.mobilein.setText("")
            return
        
        self.username = self.regui.userin.text()
        self.password = self.regui.passin.text()
        self.email = self.regui.emailin.text()
        self.mobile = self.regui.mobilein.text()
        self.passcopy = self.regui.passconf.text()
        print(self.username, self.password, self.passcopy, self.email, self.mobile)
        
        self.otpmob = OTP.generate()
        print(self.otpmob)
        
        sms = SMS.SMS('9G0JTNRLKZPXDMJW66R6H91NJGGKNKJO', 'EI7ACDERVV8POE23', 'stage', 'FSAUTH')
        smsrespone = sms.sendSMS(self.mobile, self.message%self.otpmob)
        if(smsrespone['status']!='success'):
            self.regui.errorlbl.setText(smsrespone['message'])
            return
        
        print(smsrespone)
        
        self.otpemail = OTP.generate()
        print(self.otpemail)
        
        eservice = EMail.create_service()
        emessage = EMail.create_message(self.email, self.username, 'Verify your email id', self.message%self.otpemail)
        emailresp = EMail.send_email(eservice, emessage)
        if emailresp['Messages'][0]['Status'] != 'success':
            self.regui.errorlbl.setText(emailresp['Messages'][0]['Status'])
            return
        
        print(emailresp)
        
        self.setverifywid()

    def verifymobileclicked(self):
        print(self.verifyui.otpmobile.text())
        
        if self.otpmob == int(self.verifyui.otpmobile.text()):
            self.mobileverified = True
            print(self.mobileverified)
            self.verifyui.phone_t.setPixmap(QtGui.QPixmap("resources/verified.png"))
            self.verifyui.errorlbl.setText("")
        else:
            self.verifyui.errorlbl.setText("Invalid otp!")
            
            
    def verifyemailclicked(self):
        print(self.verifyui.emailotp.text())
         
        if self.otpemail == int(self.verifyui.emailotp.text()):
            self.emailverified = True
            print(self.emailverified)
            self.verifyui.email_t.setPixmap(QtGui.QPixmap("resources/verified.png"))
            self.verifyui.errorlbl.setText("")
        else:
            self.verifyui.errorlbl.setText("Invalid otp!")
            
    def regresetclicked(self):
        self.regui.emailin.setText("")
        self.regui.userin.setText("")
        self.regui.passconf.setText("")
        self.regui.passin.setText("")
        self.regui.mobilein.setText("")
        self.email = None
        self.passcopy = None
        self.password = None
        self.username = None
        self.mobile = None
        
    def verbackclicked(self):
        self.verifyui.emailotp.setText("")
        self.verifyui.otpmobile.setText("")
        self.verifyui.email_t.clear()
        self.verifyui.phone_t.clear()
        self.regresetclicked()
        self.setregwid()
        
    def vercontinueclicked(self):
        self.userinfo = dict([('username', self.username),
                         ('password', self.password), 
                         ('mobile', self.mobile), 
                         ('email', self.email),
                         ("saveloc", os.getcwd() + "\\userfiles"),
                         ("bf_id", ''),
                         ("lb_id", [])])
        if self.emailverified == True and self.mobileverified == True :
            appdata = os.getenv('APPDATA')
            if(not os.path.exists('%s\\ForeverSafe'%appdata)):
                os.makedirs('%s\\ForeverSafe'%appdata)
                os.makedirs('%s\\ForeverSafe\\temp'%appdata)
            uinf = uinfdecrypt.UserInfoHandler(self.userinfo["username"], self.userinfo["password"])
            uinf.encryptUinfo(self.userinfo)
        else: 
            self.verifyui.errorlbl.setText("Please verify your contact information!")
            
        self.setfilelocselectorwid()
            
    def browsebtnclicked(self):
        self.saveloc = QtWidgets.QFileDialog.getExistingDirectory()
        self.filelocselui.savelocin.setText(self.saveloc)
        print(self.saveloc)
        
    def filefinishbtnclicked(self, MainWindow):
        self.saveloc = self.filelocselui.savelocin.text()
        if self.saveloc == "" or self.saveloc == None:
            self.filelocselui.errorlbl.setText("Please select a folder!")
            return
        if not os.path.exists(self.saveloc):
            try:
                os.makedirs(self.saveloc)
                print(self.saveloc, " directory created successfully")
            except OSError as e:
                self.filelocselui.errorlbl.setText("Directory Creation failed")
                print(e)
                return
                
        self.userinfo["saveloc"] = self.saveloc
        uinf = uinfdecrypt.UserInfoHandler(self.userinfo["username"], self.userinfo["password"])
        uinf.encryptUinfo(self.userinfo)
        
        self.mainwin = QtWidgets.QMainWindow()
        self.mainwinui = mainwindowblack.Ui_foreversafe(self.userinfo["username"], self.userinfo["password"])
        self.mainwinui.setupUi(self.mainwin)
        self.mainwin.show()
        MainWindow.hide()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

