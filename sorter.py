# imports random
import random
import os
import shutil
random.seed(1234)
from IPFS_API_Worker import IPFSWorker
import json

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

def choose_files(amount_i_want):
    print("IN CHOOSE FILES: ", amount_i_want)
    for i in range(1,amount_i_want+1):
        index = random.randint(0,len(dirListing))
        print(index, dirListing[index])
        new_list.append(dirListing[index])
   
    print("NEW LIST " , new_list)
    return new_list

def create_json_file(index, filename):
    json_file = {}
    CID = ipfs_worker.addFileByPath("FInal_Images/" + filename)
    json_file["image"] = "https://gateway.ipfs.io/ipfs/"+str(CID)
    json_file["tokenId"] = index
    json_file["name"] = "Pixel Plants " + str(index)
    json_file["description"] = "Pixelart plants celebrating key Songbird references"
    content = json.dumps(json_file)
    f = open("Temp/temp.json","w")
    f.write(content)
    f.close()

    f = open("JSON_Files/"+str(index)+".json","w")
    f.write(content)
    f.close()


def move_files(new_list):
    for f in new_list:
        shutil.move("Images/"+f, "FInal_Images/"+f)


def add_file_list_to_ipfs():
    dirListing = os.listdir("./FInal_Images") 
    size = len(dirListing)
    for i in range(0, size):
        create_json_file(i,dirListing[i])


file_list = choose_files(amount_i_want)
move_files(file_list)
add_file_list_to_ipfs()
    
