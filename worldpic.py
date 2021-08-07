import os, sys, requests, re
from PIL import Image
from PIL.ExifTags import TAGS

def DMS_DD(DMS):
    D = float(DMS[0])
    M = float(DMS[1])
    S = float(DMS[2])
    DD = D + (M / 60) + (S / 3600)
    return "{0:.8f}".format(DD)

def MAP(lat, long):
    m = requests.get("https://geocode.xyz/{},{}?json=1".format(lat, long))
    script = m.json()
    print('Geocode')
    return print(script['stnumber'], script['staddress'], script['city'], script['country'], script['postal'])

def GMAP(dms_lat, dms_long):
    url = ("https://www.google.co.th/maps/place/{}%C2%B0{}'{}%22N+{}%C2%B0{}'{}%22E").format(int(dms_lat[0]), int(dms_lat[1]), dms_lat[2], int(dms_long[0]), int(dms_long[1]), dms_long[2])
    source = requests.get(url).text
    s1 = source.find('"E') + 5
    s2 = source[s1:].find("'") + s1
    print('Google Map')
    return print(source[s1:s2])
                  
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('worldpic.py [image]')
    else:
        FILE = sys.argv[1]
        try:
            image = Image.open(FILE)
            MetaData = {}
            try:
                for TAG, VALUE in image._getexif().items():   
                    MetaData[TAGS[TAG]] = VALUE
                GPS = MetaData['GPSInfo']
                print(GPS[1],GPS[2],GPS[3],GPS[4])
                print(DMS_DD(GPS[2]),DMS_DD(GPS[4]))
                MAP(DMS_DD(GPS[2]),DMS_DD(GPS[4]))
                GMAP(GPS[2],GPS[4])
            except AttributeError as Er:
                print(FILE,'does not has Location!')
        except FileNotFoundError as Er:
            print(FILE,'is not found!')
        except IOError as Er:
            print(FILE,'is not found!')
