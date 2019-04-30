import urllib
import cv2
import numpy as np

url = "http://192.168.1.64:8080/shot.jpg"

while True:
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    cv2.imshow('test', img)
    cv2.waitKey(1)