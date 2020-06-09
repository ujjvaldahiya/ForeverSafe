import funcy
import base64
import Crypto.Protocol
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Protocol import KDF
import random
import string
from threading import Thread
import time
import progress
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import uinfdecrypt
import shutil

def randomString(stringLength = 10):   
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

def randomPassword():
    randomSource = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    for i in range(6):
        password += random.choice(randomSource)

    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)
    return password


class AESencrypt:
    
    def __init__(self):
        self.salt = b'\x9aX\x10\xa6^\x1fUVu\xc0\xa2\xc8\xff\xceOV'
        self.key = None
        self.bs = None
        self.iv = None
        
    def keygen(self, pwd):
        self.key = KDF.PBKDF2(password=pwd, salt=self.salt, dkLen=32, count=100000)
        self.iv = Random.new().read(AES.block_size)
        self.bs = AES.block_size
        return self.key, self.iv, self.bs
    
    def pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs).encode('utf-8')
    
    def encrypttext(self, raw, iv):
        raw = self.pad(raw.encode("utf-8"))
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(cipher.encrypt(raw))
    
    def encryptFile(self, fileIn, fileOut, chunksize=64*1024):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        with open(fileIn, "rb") as plain:
            with open(fileOut, "wb+") as outFile:                
                while True:
                    chunk = plain.read(chunksize)
                    if len(chunk) == 0:
                        break
                    chunk = self.pad(chunk)
                    outFile.write(base64.b64encode(cipher.encrypt(chunk)))
        return True
  
    
class AESdecrypt:
    
    def __init__(self, key, bs, iv):
        self.salt = b'\x9aX\x10\xa6^\x1fUVu\xc0\xa2\xc8\xff\xceOV'
        self.key = key
        self.bs = bs
        self.iv = iv
        
    def unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]
    
    def decrypttext(self, ency, iv):
        ency = base64.b64decode(ency)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return (self.unpad(cipher.decrypt(ency))).decode('utf-8')
    
    def decryptFile(self, fileIn, fileOut, chunksize=64*1024):
        with open(fileIn, "rb") as encryptedFile:
            cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
            with open(fileOut, "wb+") as decryptedFile:
                encrypted = base64.b64decode(encryptedFile.read())
                chunks = list(funcy.chunks(chunksize, encrypted))
                for chunk in chunks:
                    decrypted_chunk = self.unpad(cipher.decrypt(chunk))
                    decryptedFile.write(decrypted_chunk)
        return True

#create driver functions using threads (make batches or do single threads)
class EncryptDriver(Thread):
    
    def __init__(self, files, ftype, user, pwd, model):
        self.files = files
        self.encryptor = AESencrypt()
        self.ftype = ftype 
        self.uinf = uinfdecrypt.UserInfoHandler(user, pwd)
        self.userinfo =  self.uinf.decryptUinfo()
        self.saveloc = self.userinfo["saveloc"].strip()
        self.encrypted = None
        self.model = model
        #self.widget = widget
        print(self.files,
            self.ftype,
            self.saveloc,
            self.encrypted)
        super(EncryptDriver, self).__init__(daemon = True)
        '''self.progwin = QtWidgets.QMainWindow()
        self.progui = progress.Ui_progresswindow()
        self.progui.setupUi(self.progwin)
        self.progwin.show()'''
        
    def run(self):

        totalfiles = len(self.files)
        print(totalfiles)
        currentfile = 0
        #self.progui.progressBar.setMaximum(totalfiles)
        #self.progui.progressBar.setMinimum(0)
        
        if self.ftype == 0:
            self.encrypted = self.uinf.decryptFimg()
        else:
            self.encrypted = self.uinf.decryptFdoc()
        
        for fin in self.files:
            currentfile +=1
            #self.progui.filelbl.setText("File %s/%s"%(str(currentfile), str(totalfiles)))
            #self.progui.currentfilelbl.setText(fin)
            
            fname, fext = os.path.splitext(fin)
            fname = fname.split('/')[-1]
            foutname = randomString()
            fout = self.saveloc + "\\" + foutname + ".fsef"
            fpass = randomPassword()
            key, iv, bs = self.encryptor.keygen(fpass)
            print(type(key), type(iv), type(bs))
            print(key)
            print(iv)
            key = base64.encodebytes(key)
            key = key.decode('ascii')
            iv = base64.encodebytes(iv)
            iv = iv.decode('ascii')
            self.encryptor.encryptFile(fin, fout)
            
            self.encrypted[fname] = [fext, foutname, str(key) , str(iv), bs]
            itemn = QtGui.QStandardItem()
            itemn.setFlags(QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled) 
            itemr = QtGui.QStandardItem()
            itemr.setFlags(QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled)
            itemn.setText(fname)
            itemr.setText(fext[1:] + " file")
            self.model.appendRow([itemn, itemr])
            
            #self.progui.progressBar.setValue(currentfile)
        
        if self.ftype == 0:
            self.uinf.encryptFimg(self.encrypted)
        else:
            self.uinf.encryptFdoc(self.encrypted)
        #QtWidgets.QMessageBox.about(self.widget, "Success!", "Files encrypted successfully :)")
        print("encryption successfull")
        

class DecryptDriver(Thread):
    
    def __init__(self, files, ftype, saveloc, user, pwd):
        self.files = files
        self.ftype = ftype 
        self.uinf = uinfdecrypt.UserInfoHandler(user, pwd)
        self.saveloc = saveloc
        self.encryptloc = self.uinf.decryptUinfo()['saveloc']
        #self.widget = widget
        if ftype == 0:
            self.decryptinfo = self.uinf.decryptFimg()
        else:
            self.decryptinfo = self.uinf.decryptFdoc()
        super(DecryptDriver, self).__init__(daemon = True)
        '''self.progwin = QtWidgets.QMainWindow()
        self.progui = progress.Ui_progresswindow()
        self.progui.setupUi(self.progwin)
        self.progwin.show()'''
        
        
    def run(self):
        #self.progui.title.setText("File decryption progress")
        totalfiles = len(self.files)
        print(totalfiles)
        currentfile = 0
        #self.progui.progressBar.setMaximum(totalfiles)
        #self.progui.progressBar.setMinimum(0)
        
        for fin in self.files:
            currentfile +=1
            #self.progui.filelbl.setText("File %s/%s"%(str(currentfile), str(totalfiles)))
           # self.progui.currentfilelbl.setText(fin)
            
            fext = self.decryptinfo[fin][0]
            efname = self.encryptloc + "\\" + self.decryptinfo[fin][1] + ".fsef"
            print(self.decryptinfo[fin][2].encode('ascii'))
            key = base64.decodebytes(self.decryptinfo[fin][2].encode('ascii'))
            print(key)
            print(self.decryptinfo[fin][3].encode('ascii'))
            iv = base64.decodebytes(self.decryptinfo[fin][3].encode('ascii'))
            print(iv)
            bs = self.decryptinfo[fin][4]
            
            fout = self.saveloc + "\\" + fin + fext
            decryptor = AESdecrypt(key, bs, iv)
            decryptor.decryptFile(efname, fout)

            #self.progui.progressBar.setValue(currentfile)
        #QtWidgets.QMessageBox.about(self.widget, "Success!", "Files decrypted successfully :)")
        print('decryption successfull!')
        
class re_encryptDriver(Thread):
    
    def __init__(self, files, ftype, user, pwd):
        self.files = files
        self.ftype = ftype 
        self.encryptor = AESencrypt()
        self.uinf = uinfdecrypt.UserInfoHandler(user, pwd)
        self.encryptloc = self.uinf.decryptUinfo()['saveloc']
        self.temploc = os.getenv('APPDATA') + '\\ForeverSafe\\temp'
        #self.widget = widget
        if ftype == 0:
            self.decryptinfo = self.uinf.decryptFimg()
        else:
            self.decryptinfo = self.uinf.decryptFdoc()
        super(re_encryptDriver, self).__init__(daemon = True)
        '''self.progwin = QtWidgets.QMainWindow()
        self.progui = progress.Ui_progresswindow()
        self.progui.setupUi(self.progwin)
        self.progwin.show()'''
        
        
    def run(self):
        #self.progui.title.setText("File decryption progress")
        totalfiles = len(self.files)
        print(totalfiles)
        currentfile = 0
        '''self.progui.progressBar.setMaximum(totalfiles)
        self.progui.progressBar.setMinimum(0)'''
        
        for fin in self.files:
            currentfile +=1
            '''self.progui.filelbl.setText("File %s/%s"%(str(currentfile), str(totalfiles)))
            self.progui.currentfilelbl.setText(fin)'''
            
            fext = self.decryptinfo[fin][0]
            efname = self.encryptloc + "\\" + self.decryptinfo[fin][1] + ".fsef"
            print(self.decryptinfo[fin][2].encode('ascii'))
            key = base64.decodebytes(self.decryptinfo[fin][2].encode('ascii'))
            print(key)
            print(self.decryptinfo[fin][3].encode('ascii'))
            iv = base64.decodebytes(self.decryptinfo[fin][3].encode('ascii'))
            print(iv)
            bs = self.decryptinfo[fin][4]
            
            fout = self.temploc + "\\" + fin + fext
            decryptor = AESdecrypt(key, bs, iv)
            decryptor.decryptFile(efname, fout)
            os.remove(efname)
            print('file decrypted')
            fname = fin
            fin = fout
            
            foutname = randomString()
            fout = self.encryptloc + "\\" + foutname + ".fsef"
            fpass = randomPassword()
            key, iv, bs = self.encryptor.keygen(fpass)
            print(type(key), type(iv), type(bs))
            print(key)
            print(iv)
            key = base64.encodebytes(key)
            key = key.decode('ascii')
            iv = base64.encodebytes(iv)
            iv = iv.decode('ascii')
            
            self.encryptor.encryptFile(fin, fout)
            os.remove(fin)
            print('file re enctypted file name:', foutname)
            self.decryptinfo[fname] = [fext, foutname, str(key) , str(iv), bs]
            
            '''self.progui.progressBar.setValue(currentfile)'''
        if self.ftype == 0:
            self.uinf.encryptFimg(self.decryptinfo)
        else:
            self.uinf.encryptFdoc(self.decryptinfo)
        #QtWidgets.QMessageBox.about(self.widget, "Success!", "Files Re-encrypted successfully :)")
        print('re-ecryption successfull!')
