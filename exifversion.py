from PIL import Image
from PIL.ExifTags import TAGS

FILE = "C:/Users/tren1/Desktop/pics/test01.jpg"
FIELD = "DateTimeOriginal"

def get_exif(FILE,field):
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
                dat += "-"
            return dat
date = get_exif(FILE,FIELD)
print(date)
