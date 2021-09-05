import cv2

def colorp(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cBGR = image[y, x]
        cRGB=tuple(reversed(cBGR))

        print(f"RGB code: {cRGB} \n")


img = cv2.imread("barack.jpg")  #Change the picture to yours
image = cv2.resize(img, (800, 600))

cv2.namedWindow('Color Picker')
cv2.setMouseCallback('Color Picker', colorp)
cv2.imshow('Color Picker', image)
cv2.waitKey(0)
