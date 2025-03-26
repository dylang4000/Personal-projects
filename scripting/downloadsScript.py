import sys
import os
import operator
import shutil

from getpass import getuser

userpath = fr"C:\Users\{getuser()}\Downloads"
DownloadsFiles=[]
DownloadsDirectories=[]

os.chdir(userpath)

for i in os.listdir():
    if "." in i:
        DownloadsFiles.append(i)
    elif ("." in i)==False:
        DownloadsDirectories.append(i)


for i in DownloadsFiles:
    if operator.contains(i,".png") or operator.contains(i,".jpg") or operator.contains(i,".ico") or operator.contains(i,".webp") :
            shutil.move(f"{userpath}\{i}",r"C:\Users\Dylan Davis\Pictures\downloaded images")
    elif operator.contains(i,".zip") or operator.contains(i,".7z"):
         shutil.move(f"{userpath}\{i}",r"C:\Users\Dylan Davis\Documents\Compressed files")
