import cv2
import numpy as np
from PIL import Image

def sort_area(areas):

    dict = {}
    k=0
    for area in areas:
        dict[k]=area
        k+=1
    #返回list
    a1 = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    # print(a1)
    return a1
def get_contour(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    data = np.array(img, dtype='uint8')
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    area = []
    for k in range(len(contours)):
        area.append(cv2.contourArea(contours[k]))
    res_contours = []
    area = sort_area(area)
    for aa in area:
        if aa[1] / area[0][1] > 0.5:
            res_contours.append(contours[aa[0]]//2)
    return res_contours
def union_image_mask(image_path, mask_path, num):
    image = cv2.imread(image_path)
    mask_2d = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    ret, thresh = cv2.threshold(mask_2d, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    area = []
    for k in range(len(contours)):
        area.append(cv2.contourArea(contours[k]))
    res_contours = []
    area = sort_area(area)
    for aa in area:
        if aa[1] / area[0][1] > 0.5:
            res_contours.append(contours[aa[0]])
    cv2.drawContours(image, res_contours, -1, (0, 0, 255),2)
    # print(y,x)
    # cv2.resize(image,(y*2,x*2),cv2.INTER_LINEAR)
    cv2.imwrite('res.png', image)

if __name__ == '__main__':
    # union_image_mask(r'F:\python\mypy1\stas_seg\1637527-H.png',r'F:\python\mypy1\stas_seg\1637527-H_mask.png',1)
    contour=get_contour(r'F:\python\mypy1\stas_system\stas_system\result\1637460-G.png')
    print(len(contour[0]))
    for c in contour[0]:
        print(c[0][0], c[0][1])
    # for i in len(contour[0]):
    #     contour[0][i][0][0]*=
    print(contour[0][4][0])
    print(type(contour))
    print(len(contour))