import os
import datetime
import shutil
from PIL import Image
from PIL.ExifTags import TAGS
path = "C:/Users/tren1/Desktop/pics"
pathto="C:/Users/tren1/Desktop/picsto/"
print("Hello World.")

dirs=os.listdir(path=path)
print(dirs[0])
print(dirs[1])
for bufpath in dirs:
    #buffer = open(bufpath,mode='r')
    #os.chdir(path)
    buftmsp=datetime.datetime.fromtimestamp(os.stat(path+"/"+bufpath).st_mtime)
    bufdate=buftmsp.strftime('%Y-%m-%d')
    print(bufpath+":"+bufdate)
    if os.path.isdir(pathto+bufdate):
        print("already file exist.")
    else:
        os.mkdir(pathto+bufdate)
    
    shutil.copy(path+"/"+bufpath,pathto+"/"+bufdate+"/"+bufpath)