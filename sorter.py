# imports random
import random
import os
import shutil
random.seed(1234)
from IPFS_API_Worker import IPFSWorker

dirListing = os.listdir("./Images")
#initial_image_list = []
#for item in dirListing:
#if ".txt" in item:
#    editFiles.append(path+'\\'+item)
#print editFiles
ipfs_worker :IPFSWorker = IPFSWorker()
new_list = []
amount_i_want = input("How many files? ")
amount_i_want = int(amount_i_want)
print(len(dirListing))
print(dirListing)


for i in range(1,amount_i_want+1):
    index = random.randint(0,len(dirListing))
    print(index, dirListing[index])
    new_list.append(dirListing[index])
'''If we pass string or character literals as
parameters in the randint() function'''

print(new_list)

#for f in new_list:
#    shutil.move("Images/"+f, "FInal_Images/"+f)

CID = ipfs_worker.addFileByPath("Images/1.png")
print(CID)