from zipfile import ZipFile
import os
from datetime import date
import gdrive_handler
from PyQt5 import QtCore, QtGui, QtWidgets
import shutil
#include .fsi files
def get_all_file_paths(directory): 
    file_paths = [] 
  
    # crawling through directory and subdirectories 
    for root, directories, files in os.walk(directory): 
        for filename in files: 
            # join the two strings in order to form the full filepath. 
            filepath = os.path.join(root, filename) 
            file_paths.append(filepath) 
  
    # returning all file paths 
    return file_paths

def createbackup(directory): 
    # path to folder which needs to be zipped 
    #directory = 'userfiles'
    directory = os.path.split(directory)[-1]
    # calling function to get all file paths in the directory 
    file_paths = get_all_file_paths(directory)
    
    
    # printing the list of all files to be zipped 
    print('Following files will be zipped:') 
    for file_name in file_paths: 
        print(file_name) 
  
    # writing files to a zipfile 
    if not os.path.exists(os.getcwd() + '\\backup'):
        os.mkdir(os.getcwd() + '\\backup')
    
    today = date.today()
    # dd/mm/YY
    d = today.strftime("%d_%m_%Y")
    with ZipFile(os.getcwd() + '\\backup\\%s.zip'%d,'w') as zip: 
        # writing each file one by one

        zip.write(os.getenv('APPDATA')+'\\ForeverSafe\\ZIHeRisDReVajJeucWOa.fsi', 'ZIHeRisDReVajJeucWOa.fsi')
        zip.write(os.getenv('APPDATA')+'\\ForeverSafe\\fQkndnISNWZuhxpzfiCw.fsi', 'fQkndnISNWZuhxpzfiCw.fsi')
        for file in file_paths: 
            zip.write(file) 
  
    print('All files zipped successfully!')
    
def extract_backup(uinfo):
    file_name = os.getenv('APPDATA')+'\\ForeverSafe\\temp\\backup.zip'
      
    # opening the zip file in READ mode 
    with ZipFile(file_name, 'r') as zip: 
        # printing all the contents of the zip file 
        zip.printdir() 

        print('Extracting all the files now...') 
        if not os.path.exists(os.getenv('APPDATA')+'\\ForeverSafe\\temp\\backup'):
            os.makedirs(os.getenv('APPDATA')+'\\ForeverSafe\\temp\\backup')
        
        files = zip.namelist()
        
        if not os.path.exists(os.path.join(uinfo['saveloc'])):
            os.makedirs(os.path.join(uinfo['saveloc']))
        
        for file in files:
            if file.endswith('.fsi'):
                zip.extract(file, os.getenv('APPDATA')+'\\ForeverSafe\\temp\\backup')
            else:
                source = zip.open(file)
                target = open(os.path.join(uinfo['saveloc'], os.path.basename(file)), "wb+")
                with source, target:
                    shutil.copyfileobj(source, target)         
        print('Done!')
    


def take_backup(uinfo, widget):
    #zip all files with date as zip name
    #upload files to drive
    today = date.today()
    
    createbackup(uinfo['saveloc'])
    handler = gdrive_handler.GDrive_Handler()
    if uinfo['bf_id'] == '':
        uinfo['bf_id'] = handler.createFolder('ForeverSafe Backup')
    
    folder = handler.searchFile(10, "name = 'ForeverSafe Backup' and mimeType = 'application/vnd.google-apps.folder'")
    print(folder)
    if folder == []:
        uinfo['bf_id'] = handler.createFolder('ForeverSafe Backup')
    
    backupid = handler.uploadFile( today.strftime("%d_%m_%Y")+'.zip', 'backup\\%s.zip'%today.strftime("%d_%m_%Y"), 'application/zip', uinfo['bf_id'])
    
    if backupid != None:
        uinfo['lb_id'].append(backupid)
        QtWidgets.QMessageBox.about(widget, 'Success!', "Backup Successful! :)")
    else:
        QtWidgets.QMessageBox.about(widget, 'Failed!', "Backup Failed! Please Try again later :(")
    
    return uinfo
    
    
def restore_data(uinfo):
    #download backup files
    #extract files to the required folders
    handler = gdrive_handler.GDrive_Handler()
    if not os.path.exists(os.getenv('APPDATA')+'\\ForeverSafe\\temp\\'):
        os.makedirs(os.getenv('APPDATA')+'\\ForeverSafe\\temp\\')
    handler.downloadFile(uinfo['lb_id'][-1], os.getenv('APPDATA')+'\\ForeverSafe\\temp\\backup.zip')
    extract_backup(uinfo)
    

#if __name__ == "__main__":
 #   take_backup({})
#createbackup(os.getcwd()+'\\userfiles')