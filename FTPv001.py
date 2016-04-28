import pysftp as sftp
import datetime
import os

#pen ftp connection
def sftpExample():
    try: 
        s = sftp.Connection(host='test.rebex.net', username='demo', password ='password')
       # s = sftp.Connection(host='ftp.ab-mgt.com', username='testUser01@ab-mgt.com', password ='Changeme105')

        remotepath='/Inbox/C715404_Principal_20160408.CSV'
        localpath='G:\Accounting\Accounting HR Collaboration\Principal\CostPoint Upload\C715404_Principal_20160408.CSV' 
        #uploading a file
        #s.put(localpath,remotepath)
        #downloading a file 
        s.get(remotepath,localpath)
        s.close()
        
        
        
    except Exception, e: 
        print str(e)  

sftpExample()
#List the files in the current directory
#print "File List:"
#files = ftp.dir()
#print files