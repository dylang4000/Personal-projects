import sys
import os
import operator
import shutil

from getpass import getuser

userpath = fr"C:\Users\{getuser()}\Downloads"
documentsPath = fr"C:\Users\{getuser()}\Documents\Compressed files"
imagesPath = fr'C:\Users\{getuser()}\Pictures\downloaded images'
imageFileEXT = [".png",".jpg",".webp",".ico"]
DownloadsFiles=[]
DownloadsDirectories=[]

os.chdir(userpath)
try:
    os.mkdir(documentsPath) 
    os.mkdir(imagesPath)
   
except FileExistsError:
        print("Directories have been made")

for i in os.listdir():
    if "." in i:
        DownloadsFiles.append(i)
    elif ("." in i)==False:
        DownloadsDirectories.append(i)

#try:
    for i in DownloadsFiles:
        for ext in imageFileEXT:
             if(operator.contains(i,ext)) == True:
                  print(i)
                  break
                  
        #if operator.contains(i,".png") or operator.contains(i,".jpg") or operator.contains(i,".ico") or operator.contains(i,".webp") :
         #       shutil.move(f"{userpath}\{i}",imagesPath)
        #elif operator.contains(i,".zip") or operator.contains(i,".7z"):
        #     shutil.move(f"{userpath}\{i}",documentsPath)
