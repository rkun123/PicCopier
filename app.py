import os
import sys
import datetime
import shutil
from PIL import Image
from PIL.ExifTags import TAGS

import configLoader

#from folder path
path = ""
#to folder path
pathto = ""
print(len(sys.argv))
if len(sys.argv) > 1:
    path = sys.argv[1]
    pathto = sys.argv[2] + "/"
else:
    configs = configLoader.loader()
    path = configs["frompath"]
    pathto = configs["topath"] + "/"

FIELD = "DateTimeOriginal"

print("Hello World.")

def get_exif(FILE,field):
    print(FILE+":"+field)
    try:
        img = Image.open(FILE)
        exif = img._getexif()
        exif_data = []
        for id,value in exif.items():
            if TAGS.get(id) == field:
                tag = TAGS.get(id,id),value
                exif_data.extend(tag)
                temp = []
                temp = exif_data[1].split(" ")
                dates = []
                dates = temp[0].split(":")
                dat = ""
                for txt in dates:
                    dat += txt
                return dat
    except:
        print("Exif isn't. So,use timestamp of OS")
        buftmsp=datetime.datetime.fromtimestamp(os.stat(FILE).st_mtime)
        return buftmsp.strftime('%Y%m%d')



dirs=os.listdir(path=path)

for bufpath in dirs:
    print(bufpath)
    res_before_path = path+"/"+bufpath
    bufdate = get_exif(path+"/"+bufpath,FIELD)
    if os.path.isdir(pathto+bufdate):
        print(pathto + bufdate + " already file exist.")
    else:
        os.mkdir(pathto+bufdate)
        print("make file "+bufdate)
    
    res_path = pathto+bufdate+"/"+bufpath
    
    shutil.copy(res_before_path,res_path)
    print("Copied to :"+res_before_path+" to "+res_path)

print("All tasks are completed :)")

