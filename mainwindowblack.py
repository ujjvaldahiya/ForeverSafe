# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Python\SafeWare\mainwindowblack.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import shutil
import AES
import progress
import uinfdecrypt
import sys
import settings
import verify
import verifyemail
import SMS
import OTP
import EMail
import backup_restore

class Ui_foreversafe(object):
    
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd
    
    def setupUi(self, foreversafe):
        self.variablesinit()
        foreversafe.setObjectName("foreversafe")
        foreversafe.resize(1230, 692)
        foreversafe.setMinimumSize(QtCore.QSize(1230, 692))
        foreversafe.setMaximumSize(QtCore.QSize(1230, 692))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/logo_transparent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        foreversafe.setWindowIcon(icon)
        foreversafe.setStyleSheet("QMainWindow#MainWindow{\n"
"background-color: #2a2a2a;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(foreversafe)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{\n"
"background-color: #2a2a2a;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.topmenubar = QtWidgets.QWidget(self.centralwidget)
        self.topmenubar.setGeometry(QtCore.QRect(10, 10, 1211, 81))
        self.topmenubar.setObjectName("topmenubar")
        self.encryptbtn = QtWidgets.QPushButton(self.topmenubar)
        self.encryptbtn.setGeometry(QtCore.QRect(11, 10, 140, 61))
        self.encryptbtn.setStyleSheet("QPushButton#encryptbtn{\n"
"font: 57 14pt \"Montserrat Medium\";\n"
"background-color: #4a4a4a;\n"
"color: white;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton#encryptbtn:hover{\n"
"background-color: #787878;\n"
"}")
        self.encryptbtn.setObjectName("encryptbtn")
        self.decryptbtn = QtWidgets.QPushButton(self.topmenubar)
        self.decryptbtn.setGeometry(QtCore.QRect(160, 10, 141, 61))
        self.decryptbtn.setStyleSheet("QPushButton#decryptbtn{\n"
"background-color: #4a4a4a;\n"
"color: white;\n"
"border: none;\n"
"font: 57 14pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#decryptbtn:hover{\n"
"background-color: #787878;\n"
"}")
        self.decryptbtn.setObjectName("decryptbtn")
        self.deletebtn = QtWidgets.QPushButton(self.topmenubar)
        self.deletebtn.setGeometry(QtCore.QRect(310, 10, 141, 61))
        self.deletebtn.setStyleSheet("QPushButton#deletebtn{\n"
"background-color: #4a4a4a;\n"
"color: white;\n"
"border: none;\n"
"font: 57 14pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#deletebtn:hover{\n"
"background-color: #787878;\n"
"}")
        self.deletebtn.setObjectName("deletebtn")
        self.backupbtn = QtWidgets.QPushButton(self.topmenubar)
        self.backupbtn.setGeometry(QtCore.QRect(460, 10, 141, 61))
        self.backupbtn.setStyleSheet("QPushButton#backupbtn{\n"
"background-color: #4a4a4a;\n"
"color: white;\n"
"border: none;\n"
"font: 57 14pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#backupbtn:hover{\n"
"background-color: #787878;\n"
"}")
        self.backupbtn.setObjectName("backupbtn")
        self.restorebtn = QtWidgets.QPushButton(self.topmenubar)
        self.restorebtn.setGeometry(QtCore.QRect(610, 10, 141, 61))
        self.restorebtn.setStyleSheet("QPushButton#restorebtn{\n"
"background-color: #4a4a4a;\n"
"color: white;\n"
"font: 57 14pt \"Montserrat Medium\";\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton#restorebtn:hover{\n"
"background-color: #787878;\n"
"}")
        self.restorebtn.setObjectName("restorebtn")
        self.lockbtn = QtWidgets.QPushButton(self.topmenubar)
        self.lockbtn.setGeometry(QtCore.QRect(910, 10, 141, 61))
        self.lockbtn.setStyleSheet("QPushButton#lockbtn{\n"
"background-color: #4a4a4a;\n"
"color: white;\n"
"border: none;\n"
"font: 57 14pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#lockbtn:hover{\n"
"background-color: #787878;\n"
"}")
        self.lockbtn.setObjectName("lockbtn")
        self.settingsbtn = QtWidgets.QPushButton(self.topmenubar)
        self.settingsbtn.setGeometry(QtCore.QRect(1060, 10, 141, 61))
        self.settingsbtn.setStyleSheet("QPushButton#settingsbtn{\n"
"background-color: #006ab6 ;\n"
"color: white;\n"
"border: none;\n"
"font: 57 14pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#settingsbtn:hover{\n"
"background-color: #008be8;\n"
"}")
        self.settingsbtn.setObjectName("settingsbtn")
        self.reencryptbtn = QtWidgets.QPushButton(self.topmenubar)
        self.reencryptbtn.setGeometry(QtCore.QRect(760, 10, 141, 61))
        self.reencryptbtn.setStyleSheet("QPushButton#reencryptbtn{\n"
"background-color: #4a4a4a;\n"
"color: white;\n"
"border: none;\n"
"font: 57 14pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QPushButton#reencryptbtn:hover{\n"
"background-color: #787878;\n"
"}")
        self.reencryptbtn.setObjectName("reencryptbtn")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 100, 1191, 581))
        self.tabWidget.setStyleSheet("QTabBar::tab{\n"
"background-color: #006ab6;\n"
"border: 2px;\n"
"border-bottom-left-radius: 20px;\n"
"min-height: 125px;;\n"
"padding: 4px;\n"
"color:white;\n"
"font: 57 8pt \"Montserrat Medium\";\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover{\n"
"background-color: #008be8;\n"
"}\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"border: 2px solid #008be8;\n"
"}\n"
"\n"
"")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.imgtab = QtWidgets.QWidget()
        self.imgtab.setStyleSheet("QWidget#imgtab{\n"
"background-color: #4a4a4a;\n"
"}")
        self.imgtab.setObjectName("imgtab")
        self.imgtable = QtWidgets.QTableView(self.imgtab)
        self.imgtable.setGeometry(QtCore.QRect(0, 0, 1161, 571))
        self.imgtable.verticalHeader().setVisible(False)
        self.imgtable.setStyleSheet("QTableView#imgtable{\n"
                                    "background-color: #4a4a4a;\n"
                                    "border-style: none;"
                                        "}"
                                    "QTableView#imgtable::item{\n"
                                    "background-color: #4a4a4a;\n"
                                    "border: none;"
                                    "border-right: 0px solid;"
                                    "border-left: 0px solid;"
                                    "border-top: 0px solid;"
                                    "border-bottom: 1px solid #787878;"
                                    "color: white;"
                                        "}"
                                    "QHeaderView::section{"
                                    "background-color: #4a4a4a;"
                                    "border-style: none;"
                                    "color: white;"
                                    "}")
        self.imgtable.setObjectName("imgtable")
        self.tabWidget.addTab(self.imgtab, "")
        self.doctab = QtWidgets.QWidget()
        self.doctab.setStyleSheet("QWidget#doctab{\n"
                                  "background-color: #4a4a4a;\n"
                                  "}")
        self.doctab.setObjectName("doctab")
        self.doctable = QtWidgets.QTableView(self.doctab)
        self.doctable.setGeometry(QtCore.QRect(0, 0, 1161, 571))
        self.doctable.verticalHeader().setVisible(False)
        self.doctable.setStyleSheet("QTableView#doctable{\n"
                                    "background-color: #4a4a4a;\n"
                                    "border-style: none;"
                                        "}"
                                    "QTableView#doctable::item{\n"
                                    "background-color: #4a4a4a;\n"
                                    "border: none;"
                                    "border-right: 0px solid;"
                                    "border-left: 0px solid;"
                                    "border-top: 0px solid;"
                                    "border-bottom: 1px solid #787878;"
                                    "color: white;"
                                        "}"
                                    "QHeaderView::section{"
                                    "background-color: #4a4a4a;"
                                    "border-style: none;"
                                    "color: white;"
                                    "}")
        self.doctable.setObjectName("doctable")
        self.tabWidget.addTab(self.doctab, "")
        foreversafe.setCentralWidget(self.centralwidget)
        
        self.settingsmain = QtWidgets.QMainWindow()
        self.settingsui = settings.Ui_MainWindow()
        self.settingsui.setupUi(self.settingsmain)
        
        self.verifymain = QtWidgets.QMainWindow()
        self.verifyui = verify.Ui_MainWindow()
        self.verifyui.setupUi(self.verifymain)
        
        self.verifyemailmain = QtWidgets.QMainWindow()
        self.verifyemailui = verifyemail.Ui_MainWindow()
        self.verifyemailui.setupUi(self.verifyemailmain)
        
        self.otpmob = None
        self.otpemail = None
        
        self.loadencryptedfiles()
        self.retranslateUi(foreversafe)
        self.addeventlistners()
        QtCore.QMetaObject.connectSlotsByName(foreversafe)

    def retranslateUi(self, foreversafe):
        _translate = QtCore.QCoreApplication.translate
        foreversafe.setWindowTitle(_translate("foreversafe", "ForeverSafe"))
        self.encryptbtn.setText(_translate("foreversafe", "Encrypt"))
        self.decryptbtn.setText(_translate("foreversafe", "Decrypt"))
        self.deletebtn.setText(_translate("foreversafe", "Delete"))
        self.backupbtn.setText(_translate("foreversafe", "Backup"))
        self.restorebtn.setText(_translate("foreversafe", "Restore"))
        self.lockbtn.setText(_translate("foreversafe", "Lock"))
        self.settingsbtn.setText(_translate("foreversafe", "Settings"))
        self.reencryptbtn.setText(_translate("foreversafe", "Re-Encrypt"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.imgtab), _translate("foreversafe", "Images"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.doctab), _translate("foreversafe", "Documents"))

    def variablesinit(self):
        pass
    
    def addeventlistners(self):
        self.encryptbtn.clicked.connect(self.encryptbtnclicked)
        self.decryptbtn.clicked.connect(self.decryptbtnclicked)
        self.deletebtn.clicked.connect(self.deletebtnclicked)
        self.lockbtn.clicked.connect(self.lockbtnclicked)
        self.reencryptbtn.clicked.connect(self.reencryptbtnclicked)
        self.settingsbtn.clicked.connect(self.settingsbtnclicked)
        self.settingsui.saveuserbtn.clicked.connect(self.saveuserbtnclicked)
        self.settingsui.savepassbtn.clicked.connect(self.savepassbtnclicked)
        self.settingsui.saveemailbtn.clicked.connect(self.saveemailbtnclicked)
        self.settingsui.savephonebtn.clicked.connect(self.savephonebtnclicked)
        self.settingsui.savesavebtn.clicked.connect(self.savesavebtnclicked)
        self.verifyemailui.verifyotp.clicked.connect(self.verifyemailotpclicked)
        self.verifyui.verifyotp.clicked.connect(self.verifyotpbtnclicked)
        self.settingsui.browsebtn.clicked.connect(self.browsebtnclicked)
        self.restorebtn.clicked.connect(self.restorebtnclicked)
        self.backupbtn.clicked.connect(self.backupbtnclicked)
    
    def encryptbtnclicked(self):
        
        if self.tabWidget.currentIndex() == 0:
            filterr = "Image Files (*.png *.jpg *.jpeg *.bmp *.tif)"
            model =  self.imgtable.model()
        else:
            filterr = "Documents (*.txt *.html *.xml *.docx *.xlsx *.pptx)"
            model = self.doctable.model()
            
        files, _ = QtWidgets.QFileDialog.getOpenFileNames(filter = filterr) 
        print(files)
        
        if files == []:
            QtWidgets.QMessageBox.about(self.centralwidget, 'Invalid!', "No file selected")
            return
        
        encrypt = AES.EncryptDriver(files, self.tabWidget.currentIndex(), self.user, self.pwd, model)
        encrypt.start()
        

    def decryptbtnclicked(self): 
        
        if self.tabWidget.currentIndex():
            index = self.doctable.currentIndex()
            model = self.doctable.model()
        else :
            index = self.imgtable.currentIndex()
            model = self.imgtable.model()
        if index.row() == -1:
            QtWidgets.QMessageBox.about(self.centralwidget, 'Invalid!', "No file selected")
            return
            
        saveloc = QtWidgets.QFileDialog.getExistingDirectory() 
        print(saveloc)   
        print(index.row())
        print(model.item(index.row(), 0).text())
            #key = model.item(index).text()
        key  = model.item(index.row(), 0).text()
        decrypt = AES.DecryptDriver([key], self.tabWidget.currentIndex(), saveloc, self.user, self.pwd)  
        decrypt.start()                              
        
        

    def loadencryptedfiles(self):
        self.uinfd = uinfdecrypt.UserInfoHandler(self.user, self.pwd)
        self.imgfiles = self.uinfd.decryptFimg()
        imgmodel = QtGui.QStandardItemModel(self.imgtable)
        imgmodel.setHorizontalHeaderLabels(['Name', 'type'])
        
        self.docfiles = self.uinfd.decryptFdoc()
        docmodel = QtGui.QStandardItemModel(self.doctable)
        docmodel.setHorizontalHeaderLabels(['Name', 'type'])
        
        print(self.imgfiles)
        print(self.docfiles)  
        
        
        for file in self.imgfiles.keys():
            itemn = QtGui.QStandardItem()
            itemn.setFlags(QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled) 
            itemr = QtGui.QStandardItem()
            itemr.setFlags(QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled)
            itemn.setText(file.strip())
            itemr.setText(self.imgfiles[file.strip()][0][1:] + " file")
            imgmodel.appendRow([itemn, itemr])
    
        self.imgtable.setModel(imgmodel)
        self.imgtable.horizontalHeader().resizeSection(0, 800)
        self.imgtable.horizontalHeader().resizeSection(1, 359)
        
        for file in self.docfiles.keys():
            itemn = QtGui.QStandardItem()
            itemn.setFlags(QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled) 
            itemr = QtGui.QStandardItem()
            itemr.setFlags(QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled)
            itemn.setText(file.strip())
            itemr.setText(self.docfiles[file.strip()][0][1:] + " file")
            docmodel.appendRow([itemn, itemr])
            
        self.doctable.setModel(docmodel)
        self.doctable.horizontalHeader().resizeSection(0, 800)
        self.doctable.horizontalHeader().resizeSection(1, 359) 
        
    def deletebtnclicked(self):
        save = self.uinfd.decryptUinfo()['saveloc']
        if self.tabWidget.currentIndex():
            index = self.doctable.currentIndex()
            model = self.doctable.model()  
            self.docfiles = self.uinfd.decryptFdoc()
        else :
            index = self.imgtable.currentIndex()
            model = self.imgtable.model()
            self.imgfiles = self.uinfd.decryptFimg()
        
        if index.row() == -1:
            QtWidgets.QMessageBox.about(self.centralwidget, 'Invalid!', "No file selected")
            return
        
        if QtWidgets.QMessageBox.question(self.centralwidget, 'Delete', "Are you sure?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No) == QtWidgets.QMessageBox.Yes  :            
            if not self.tabWidget.currentIndex():
                os.remove(save + "\\" + self.imgfiles[model.item(index.row(), 0).text()][1] + '.fsef')
                self.imgfiles.pop(model.item(index.row(), 0).text())
                self.uinfd.encryptFimg(self.imgfiles)
            else:
                os.remove(save + "\\" + self.docfiles[model.item(index.row(), 0).text()][1] + '.fsef')
                self.docfiles.pop(model.item(index.row(), 0).text())
                self.uinfd.encryptFdoc(self.docfiles)
            model.removeRow(index.row())
        else:
            return
        
    def lockbtnclicked(self):
        if QtWidgets.QMessageBox.question(self.centralwidget, 'Lock', "Are you sure?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No) == QtWidgets.QMessageBox.Yes  :
            sys.exit(0)
        
    def reencryptbtnclicked(self):
        if self.tabWidget.currentIndex():
            index = self.doctable.currentIndex()
            model = self.doctable.model()    
        else :
            index = self.imgtable.currentIndex()
            model = self.imgtable.model()
            
        if index.row() == -1:
            QtWidgets.QMessageBox.about(self.centralwidget, 'Invalid!', "No file selected")
            return
        reencrypter = AES.re_encryptDriver([model.item(index.row(), 0).text()], self.tabWidget.currentIndex(), self.user, self.pwd)
        reencrypter.start()
        
    def settingsbtnclicked(self):
        self.settingsmain.show()

    def saveuserbtnclicked(self):
        newuser = self.settingsui.newuserin.text()
        uinfo = self.uinfd.decryptUinfo()
        uinfo['username'] = newuser
        self.uinfd.encryptUinfo(uinfo)
        self.user = newuser
        QtWidgets.QMessageBox.about(self.centralwidget, 'Success!', "Username changed successfully! :)")
        self.settingsui.newuserin.setText('')

    def savepassbtnclicked(self):
        newpass = self.settingsui.newpassin.text()
        cpass = self.settingsui.cpassin.text()
        
        if newpass == cpass:
            uinfo = self.uinfd.decryptUinfo()
            uinfo['password'] = cpass
            self.uinfd = uinfdecrypt.UserInfoHandler(uinfo['username'], cpass)
            self.uinfd.encryptUinfo(uinfo)
            self.pwd = cpass
            
            QtWidgets.QMessageBox.about(self.settingsui.centralwidget, 'Success!', "Password changed successfully! :)")
        else:
            QtWidgets.QMessageBox.about(self.settingsui.centralwidget, 'Failed!', "Passwords didn't match!")
        self.settingsui.newemailin.setText('')
        self.settingsui.cpassin.setText('')


    def saveemailbtnclicked(self):
        self.otpemail = OTP.generate()
        print(self.otpemail)
        message = "%s is your otp for verification on ForeverSafe"
        eservice = EMail.create_service()
        emessage = EMail.create_message(self.settingsui.newemailin.text(), self.user, 'Verify your email id', message%self.otpemail)
        emailresp = EMail.send_email(eservice, emessage)
        if emailresp['Messages'][0]['Status'] != 'success':
            QtWidgets.QMessageBox.about(self.settingsui.centralwidget, 'Failed!', "Couldn't send otp!")
            return      
        print(emailresp)
        self.verifyemailmain.show()

    def savephonebtnclicked(self):
        self.otpmob = OTP.generate()
        print(self.otpmob)
        message = "%s is your otp for verification on ForeverSafe"
        sms = SMS.SMS('9G0JTNRLKZPXDMJW66R6H91NJGGKNKJO', 'EI7ACDERVV8POE23', 'stage', 'FSAUTH')
        smsrespone = sms.sendSMS(self.settingsui.newphonein.text(), message%self.otpmob)
        if(smsrespone['status']!='success'):
            QtWidgets.QMessageBox.about(self.settingsui.centralwidget, 'Failed!', "Couldn't send otp!")
            return        
        print(smsrespone)
        self.verifymain.show()
        
    def verifyotpbtnclicked(self):
        uinfo = self.uinfd.decryptUinfo()
        if self.otpmob == int(self.verifyui.otpin.text()):
            uinfo['mobile'] = self.settingsui.newphonein.text()
            self.uinfd.encryptUinfo(uinfo)
            QtWidgets.QMessageBox.about(self.verifyui.centralwidget, 'Success!', "Mobile no. changed successfully! :)")
        else:
            QtWidgets.QMessageBox.about(self.verifyui.centralwidget, 'Failed!',"Invalid otp!")    
        self.otpmob = None
        self.verifymain.close()
        self.settingsui.newphonein.setText('')
        
    
    def verifyemailotpclicked(self):
        uinfo = self.uinfd.decryptUinfo()
        if self.otpemail == int(self.verifyemailui.otpin.text()):
            uinfo['email'] = self.settingsui.newemailin.text()
            self.uinfd.encryptUinfo(uinfo)
            QtWidgets.QMessageBox.about(self.verifyemailui.centralwidget, 'Success!', "Email Id changed successfully! :)")
        else:
            QtWidgets.QMessageBox.about(self.verifyemailui.centralwidget, 'Failed!',"Invalid otp!")
        self.otpemail = None
        self.verifyemailmain.close()
        self.settingsui.newemailin.setText('')

    def browsebtnclicked(self):
        newsaveloc = QtWidgets.QFileDialog.getExistingDirectory()
        self.settingsui.newsavein.setText(newsaveloc)

    def savesavebtnclicked(self):   
        if not os.path.exists(self.settingsui.newsavein.text()):
            try:
                os.makedirs(self.settingsui.newsavein.text())
            except:
                QtWidgets.QMessageBox.about(self.settingsui.centralwidget, 'Failed!', "ForeverSave can't save files to given directory :(")
                return
        uinfo = self.uinfd.decryptUinfo()
        uinfo['saveloc'] = self.settingsui.newsavein.text()
        self.uinfd.encryptUinfo(uinfo)
        QtWidgets.QMessageBox.about(self.settingsui.centralwidget, 'Success!', "Save Directory changed successfully! :)")
        self.settingsui.newsavein.setText('')
        
    def backupbtnclicked(self):
        uinf = backup_restore.take_backup(self.uinfd.decryptUinfo(), self.centralwidget)
        self.uinfd.encryptUinfo(uinf)
        
    def restorebtnclicked(self):
        backup_restore.restore_data(self.uinfd.decryptUinfo())
        
        docb = self.uinfd.decryptFdocb()
        print(docb)
        imgb = self.uinfd.decryptFimgb()
        print(imgb)
        img = self.uinfd.decryptFimg()
        doc = self.uinfd.decryptFdoc()
        
        imgmodel = self.imgtable.model()
        docmodel = self.doctable.model()
        
        for key in docb.keys():
            if key in doc.keys():
                flag = False
            else:
                flag = True
                
            doc[key] = docb[key]
            itemn = QtGui.QStandardItem()
            itemn.setFlags(QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled) 
            itemr = QtGui.QStandardItem()
            itemr.setFlags(QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled)
            itemn.setText(key)
            itemr.setText(docb[key][0][1:] + " file")
            if flag:
                docmodel.appendRow([itemn, itemr])
            
        for key in imgb.keys():
            if key in img.keys():
                flag = False
            else:
                flag = True
                
            img[key] = imgb[key]
            itemn = QtGui.QStandardItem()
            itemn.setFlags(QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled) 
            itemr = QtGui.QStandardItem()
            itemr.setFlags(QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled)
            itemn.setText(key)
            itemr.setText(imgb[key][0][1:] + " file")
            if flag:
                imgmodel.appendRow([itemn, itemr])
            
        self.uinfd.encryptFdoc(doc)
        self.uinfd.encryptFimg(img)
        os.remove(os.getenv('APPDATA')+'\\ForeverSafe\\temp\\backup.zip')
        shutil.rmtree(os.getenv('APPDATA')+'\\ForeverSafe\\temp\\backup')
        QtWidgets.QMessageBox.about(self.settingsui.centralwidget, 'Success!', "Restore successful! :)")            
                    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    foreversafe = QtWidgets.QMainWindow()
    ui = Ui_foreversafe()
    ui.setupUi(foreversafe)
    foreversafe.show()
    sys.exit(app.exec_())

