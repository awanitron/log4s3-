import requests
import pdb
from awsauth import S3Auth
import logging
import os
from logging.handlers import RotatingFileHandler

class FooBar(RotatingFileHandler)  : 
    def __init__(self,  filename, mode='a', maxBytes=0,backupCount=0, encoding=None, delay=0) :
        RotatingFileHandler.__init__(self, filename, mode, maxBytes, backupCount, encoding, delay)
    
 
class S3RotatingFileHandler(RotatingFileHandler) :
    def __init__(self, filename, mode='a', maxBytes=0,   
                       backupCount=0, encoding=None, delay=0,
                       aws_key = None, aws_secret = None,
                       aws_urlbase = None):

        RotatingFileHandler.__init__(self, filename, mode, maxBytes, backupCount, encoding, delay)
        self.aws_key = aws_key
        self.aws_secret = aws_secret
        self.aws_urlbase = aws_urlbase


    def doRollover(self):
        """
        Do a rollover, as described in __init__().
        """
        if self.stream:
            self.stream.close()
            self.stream = None

        url =  self.aws_urlbase + r'/' + os.path.basename(self.baseFilename)
        r = requests.put(url, data=self.baseFilename, auth=S3Auth(self.aws_key, self.aws_secret))

        if self.backupCount > 0:
            
            for i in range(self.backupCount - 1, 0, -1):
                sfn = "%s.%d" % (self.baseFilename, i)
                dfn = "%s.%d" % (self.baseFilename, i + 1)
                if os.path.exists(sfn):
                    if os.path.exists(dfn):
                        os.remove(dfn)
                    os.rename(sfn, dfn)
                    url =  self.aws_urlbase + r'/' + os.path.basename(dfn)
                    r = requests.put(url, data=dfn, auth=S3Auth(self.aws_key, self.aws_secret))

            dfn = self.baseFilename + ".1"
            if os.path.exists(dfn):
                os.remove(dfn)
            # Issue 18940: A file may not have been created if delay is True.
            if os.path.exists(self.baseFilename):
                os.rename(self.baseFilename, dfn)
            

        if not self.delay:
            self.stream = self._open()
