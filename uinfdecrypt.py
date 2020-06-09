import AES
import os
import json

#iv is generated fresh everytime so save iv in the encryption process

class UserInfoHandler:
    def __init__(self, user, pwd):
        self.user = user
        self.password = pwd
        
        self.uinfo = 'TsnWjtkdhKQmhoPqkVOY.fsi'
        self.fileinfo = {"images": "fQkndnISNWZuhxpzfiCw.fsi",
                         "documents": "ZIHeRisDReVajJeucWOa.fsi"}
        
        self.encryptor = AES.AESencrypt()
        self.key, _, self.bs = self.encryptor.keygen(pwd)
        self.iv = b'\x8d\xcc\x9e\xd4\x0ei\xf0\xdaG\xcc#\xb6\x15P_\x00'
        self.decryptor = AES.AESdecrypt(self.key, self.bs, self.iv)
        
        self.infoPath = os.getenv("APPDATA")+"\\ForeverSafe\\"
        
        if not os.path.exists(self.infoPath + self.uinfo):
            uinfofile = open(self.infoPath + self.uinfo, "wb+")
            uinfofile.close()
        
        if not os.path.exists(self.infoPath + self.fileinfo["images"]):
            fimginfofile = open(self.infoPath + self.fileinfo["images"], "wb+")
            fimginfofile.close()
            
        if not os.path.exists(self.infoPath + self.fileinfo["documents"]):
            fdocinfofile = open(self.infoPath + self.fileinfo["documents"], "wb+")
            fdocinfofile.close()
                
    def encryptUinfo(self, dtext):
        with open(self.infoPath + self.uinfo, "rb+") as f:
            dtext = json.dumps(dtext)
            etext = self.encryptor.encrypttext(dtext, self.iv)
            f.truncate(0)
            f.write(etext)
        return True
    
    def encryptFimg(self, dtext):
        with open(self.infoPath + self.fileinfo["images"], "rb+") as f:
            dtext = json.dumps(dtext)
            etext = self.encryptor.encrypttext(dtext, self.iv)
            f.truncate(0)
            f.write(etext)
        return True
    
    def encryptFdoc(self, dtext):
        with open(self.infoPath + self.fileinfo["documents"], "rb+") as f:
            dtext = json.dumps(dtext)
            etext = self.encryptor.encrypttext(dtext, self.iv)
            f.truncate(0)
            f.write(etext)
        return True
    
    def decryptUinfo(self):
        with open(self.infoPath + self.uinfo, "rb+") as f:
            etext = f.read()
            try:
                dtext = self.decryptor.decrypttext(etext, self.iv)
                return json.loads(dtext)
            except:
                return False
    
    def decryptFimg(self):
        if os.path.getsize(self.infoPath + self.fileinfo["images"]) == 0:
            return {}
        with open(self.infoPath + self.fileinfo["images"], "rb+") as f:
            etext = f.read()
            try:
                dtext = self.decryptor.decrypttext(etext, self.iv)
                return json.loads(dtext)
            except:
                return False
    
    def decryptFdoc(self):
        if os.path.getsize(self.infoPath + self.fileinfo["documents"]) == 0:
            return {}
        with open(self.infoPath + self.fileinfo["documents"], "rb+") as f:
            etext = f.read()
            try:
                dtext = self.decryptor.decrypttext(etext, self.iv)
                return json.loads(dtext)
            except:
                return False
    def decryptFimgb(self):
        if os.path.getsize(self.infoPath +"temp\\backup\\" + self.fileinfo["images"]) == 0:
            return {}
        with open(self.infoPath +"temp\\backup\\" + self.fileinfo["images"], "rb+") as f:
            etext = f.read()
            try:
                dtext = self.decryptor.decrypttext(etext, self.iv)
                return json.loads(dtext)
            except:
                return False
    
    def decryptFdocb(self):
        if os.path.getsize(self.infoPath +"temp\\backup\\" + self.fileinfo["documents"]) == 0:
            return {}
        with open(self.infoPath +"temp\\backup\\"+ self.fileinfo["documents"], "rb+") as f:
            etext = f.read()
            try:
                dtext = self.decryptor.decrypttext(etext, self.iv)
                return json.loads(dtext)
            except:
                return False
        
        
        