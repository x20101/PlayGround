import pysftp as sftp
import datetime
import os
from ftplib import FTP
import re



#pen ftp connection
def listFiles(files, patern='re_.+.txt'):
    matchedFiles = []
 
    for filename in files:
        if re.match(patern, filename):
            matchedFiles.append(filename)
    return matchedFiles
 
 
user='demo'
password = 'password'
f = FTP('test.rebex.net', user, password)
#return list of files in the current directory
files = f.nlst()
print listFiles(files)