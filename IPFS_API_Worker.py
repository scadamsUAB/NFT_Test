#import ipfsapi  ### note this is depricated
import ipfshttpclient
import subprocess
import json
import os
import time
from pathlib import Path

# TODO: PIN DATA
# TODO: Configure options for Cache

class IPFSWorker:

    def __init__(self):
        self.api=None
        if not os.path.exists('Cache'):
            os.makedirs('Cache')
       
        self.tryconnect()

    def addFileByPath(self,filePath):
        CID=self.api.add(filePath)
        self.api.add(filePath)
        return CID["Hash"]
        

    def getCID(self, fileName):
        CID=self.api.add(fileName,only_hash=True)
        print("CID: ::", CID["Hash"])
        return CID["Hash"]

    def getCIDAndAdd(self, fileName):
        CID=self.api.add(fileName,only_hash=True)
        self.api.add(fileName)
        return CID["Hash"]
   
    def getContent(self,CID):
        try:
            content=self.api.cat(CID)
            return self.api.cat(CID)
        except ipfshttpclient.exceptions.TimeoutError:
            return ""  ### Return empty if no value found 

    def close(self):  # Call this when you're done
        self.api.close()

    def tryconnect(self):
        # Connect to local node
        try:
            print("ESTABLISHING CONNECTION TO IPFS DAEMON")
            api = ipfshttpclient.connect(timeout=5)
            print("CONNECTION SUCCESSFUL")
            self.api=api
            
        except ipfshttpclient.exceptions.ConnectionError as ce:
            print("***** ERROR ******")
            print(str(ce))
            print()
            f=open("Config.json","r")
            jsonContent=f.read()
            jsonConfig=json.loads(jsonContent)
            f.close()    
            print(jsonConfig)
            print(jsonConfig["IPFSPath"])
         
            cmd =str(jsonConfig["IPFSPath"])+" daemon &"
            print("COMMAND: ", cmd)
            os.system(cmd) # returns the exit status
            #subprocess.Popen(cmd,close_fds=True)
           
          #  os.spawnl(os.P_NOWAIT, [cmd,'daemon'])
            time.sleep(5)
            self.tryconnect()
            


if __name__ == '__main__':
    ipfsworker = IPFSWorker()
    res = ipfsworker.api.add("Images/1.png")
    print(res)
    print("HASH:",res['Hash'])
    print(ipfsworker.getContent(res["Hash"]))