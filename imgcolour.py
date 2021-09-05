import cv2
import json
import requests

def colorp(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cBGR = image[y, x]
        cRGB=tuple(reversed(cBGR))

        r = requests.get(f'https://www.thecolorapi.com/id?rgb=rgb{cRGB}').json()
        colour_rex = r['hex']['value']
        colour_name = r['name']['value']

        print(f'Colour name: {colour_name}')
        print(f'HEX: {colour_rex}')
        print(f'RGB code: {cRGB} \n')


img = cv2.imread('family.jpg')
image = cv2.resize(img, (800, 600))  #Change the picture to yours


cv2.namedWindow('imgcolour')
cv2.setMouseCallback('imgcolour', colorp)
cv2.imshow('imgcolour', image)
cv2.waitKey(0)
