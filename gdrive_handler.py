
from __future__ import print_function
import httplib2
import os, io

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaFileUpload, MediaIoBaseDownload
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
import auth
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json

class GDrive_Handler():
    
    def __init__(self):
        self.SCOPES = 'https://www.googleapis.com/auth/drive'
        self.CLIENT_SECRET_FILE = 'client_secret.json'
        self.APPLICATION_NAME = 'ForeverSafe'
        self.authInst = auth.auth(self.SCOPES,self.CLIENT_SECRET_FILE,self.APPLICATION_NAME)
        self.credentials = self.authInst.getCredentials()
        
        self.http = self.credentials.authorize(httplib2.Http())
        self.drive_service = discovery.build('drive', 'v3', http=self.http)
    
    '''def listFiles(self, size):
        results = self.drive_service.files().list(
            pageSize=size,fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print('{0} ({1})'.format(item['name'], item['id']))'''
    
    def uploadFile(self, filename,filepath,mimetype, folder_id):
        try:
            file_metadata = {'name': filename, "parents": [folder_id]}
            media = MediaFileUpload(filepath,
                                    mimetype=mimetype)
            file = self.drive_service.files().create(body=file_metadata,
                                                media_body=media,
                                                fields='id').execute()
            return file.get('id')
        except:
            return None
    
    def downloadFile(self, file_id,filepath):
        try:
            request = self.drive_service.files().get_media(fileId=file_id)
            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print("Download %d%%." % int(status.progress() * 100))
            with io.open(filepath,'wb+') as f:
                fh.seek(0)
                f.write(fh.read())
            return True
        except:
            return False
    
    def createFolder(self, name):
        file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder'
        }
        file = self.drive_service.files().create(body=file_metadata,
                                            fields='id').execute()
        return file.get('id')
    
    def searchFile(self, size,query):
        results = self.drive_service.files().list(
        pageSize=size,fields="nextPageToken, files(id, name, kind, mimeType)",q=query).execute()
        items = results.get('files', [])
        return items
    
#uploadFile('unnamed.jpg','unnamed.jpg','image/jpeg')
#downloadFile('1Knxs5kRAMnoH5fivGeNsdrj_SIgLiqzV','google.jpg')
#createFolder('Google')
#searchFile(10,"name = 'hello' and mimeType = 'application/vnd.google-apps.folder'")
#handler = gdrive_handler()
#handler.searchFile(10, "name = 'kasaui' and mimeType = 'application/vnd.google-apps.folder'")