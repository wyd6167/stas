import cv2
import numpy as np

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

def judge(path,dot_list):

    # for i in range(len(dot_list)):
    #     dot_list[i]=dot_list[i]/8
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    data = np.array(img, dtype='uint8')
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for i in range(len(contours)):
        contours[i]=contours[i]*8
    area=[]
    for k in range(len(contours)):
        area.append(cv2.contourArea(contours[k]))
        # max_idx = np.argmax(np.array(area))
    res_contours=[]
    area=sort_area(area)
    # print(area)
    # max_idx=area[0][0]
    # print(max_idx)
    # res_contours.append(contours[max_idx])
    for aa in area:
        # res_contours.append(contours[aa[0]])
        if aa[1]/area[0][1]>0.5:
            res_contours.append(contours[aa[0]])
    # print(len(res_contours))
    # mask=np.zeros(img.shape,dtype=np.uint8)
    # img=cv2.drawContours(img, res_contours, -1, (0, 0, 255), cv2.FILLED)
    #
    # cv2.imwrite('01.png', img)
    for con in res_contours:
        print('patchcenter:',(dot_list[0]+dot_list[2])/2, (dot_list[1]+dot_list[3])/2)
        print(cv2.pointPolygonTest(con, ((dot_list[0]+dot_list[2])/2, (dot_list[1]+dot_list[3])/2), False))
        if cv2.pointPolygonTest(con, ((dot_list[0]+dot_list[2])/2, (dot_list[1]+dot_list[3])/2), False)==1 and data[(dot_list[1]//8+dot_list[3]//8)//2,(dot_list[0]//8+dot_list[2]//8)//2,:].all()==255:
        # if cv2.pointPolygonTest(con, ((dot_list[0]+dot_list[2])/2, (dot_list[1]+dot_list[3])/2), False)==1:
            return False
        # if cv2.pointPolygonTest(con, (dot_list[0], dot_list[1]), False)==-1 or cv2.pointPolygonTest(con, (dot_list[2], dot_list[1]), False)==-1 or cv2.pointPolygonTest(con, (dot_list[0], dot_list[3]), False)==-1 or cv2.pointPolygonTest(con, (dot_list[2], dot_list[3]), False)==-1 :
        #     return False
    return True
    # print(res_contours)
    # cv2.drawContours(img,res_contours,-1,(0, 0, 255),cv2.FILLED)
    # # print(contours)
    # # print(len(contours))
    # # print(dist1)
    # cv2.imshow("img", img)
    # cv2.waitKey(0)
    # cv2.imwrite('01.png',img)

def judge_rectangle(path,dot_list):

    img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    data = np.array(img, dtype='uint8')

    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for i in range(len(contours)):
        contours[i] = contours[i] * 8
    area = []
    for k in range(len(contours)):
        area.append(cv2.contourArea(contours[k]))
    res_contours = []
    area = sort_area(area)

    for aa in area:

        if aa[1] / area[0][1] > 0.5:
            res_contours.append(contours[aa[0]])
    left_top=[dot_list[0],dot_list[1]]
    left_bottom=[dot_list[0],dot_list[3]]
    right_top=[dot_list[2],dot_list[1]]
    right_botttom=[dot_list[2],dot_list[3]]
    for con in res_contours:
        for i in range(dot_list[1],dot_list[3]):

            if cv2.pointPolygonTest(con, (dot_list[0], i),
                                    False) == 1 and data[i//8,
                                                    dot_list[0]//8, 0] == 255:


                return False
        for i in range(dot_list[1],dot_list[3]):
            if cv2.pointPolygonTest(con, (dot_list[2], i),
                                    False) == 1 and data[i//8,
                                                    dot_list[2]//8, 0] == 255:
                return False
        for i in range(dot_list[0],dot_list[2]):
            if cv2.pointPolygonTest(con, (i, dot_list[1]),
                                    False) == 1 and data[dot_list[1]//8,
                                                    i//8, 0] == 255:
                return False
        for i in range(dot_list[0],dot_list[2]):
            if cv2.pointPolygonTest(con, (i, dot_list[3]),
                                    False) == 1 and data[dot_list[3]//8,
                                                    i//8, 0] == 255:
                return False



    return True
def compute_distance(path,dot_list):

    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    data = np.array(img, dtype='uint8')
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for i in range(len(contours)):
        contours[i] = contours[i] * 8
    area = []
    for k in range(len(contours)):
        area.append(cv2.contourArea(contours[k]))
    res_contours = []
    area = sort_area(area)

    for aa in area:

        # if aa[1] / area[0][1] > 0.5:
        res_contours.append(contours[aa[0]])
    dis=99999999
    for con in res_contours:
        print('patchcenter:', (dot_list[0] + dot_list[2]) / 2, (dot_list[1] + dot_list[3]) / 2)
        print(-cv2.pointPolygonTest(con, ((dot_list[0] + dot_list[2]) / 2, (dot_list[1] + dot_list[3]) / 2), True))
        dis=min(dis,-cv2.pointPolygonTest(con, ((dot_list[0] + dot_list[2]) / 2, (dot_list[1] + dot_list[3]) / 2), True))



    return dis
def compute_area(path,mpp):

    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    data = np.array(img, dtype='uint8')
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for i in range(len(contours)):
        contours[i] = contours[i] * 8
    area = []
    sum=0
    sum_main=0
    for k in range(len(contours)):
        area.append(cv2.contourArea(contours[k])*mpp**2)
        sum+=(cv2.contourArea(contours[k])*mpp**2)
        sum_main+=cv2.contourArea(contours[k])
    # print(img.shape[0]*img.shape[1]*64,sum)
    # exit()

    return sum_main,img.shape[0]*img.shape[1]*64*mpp**2-sum



if __name__=='__main__':
    judge('/home/hansheng/wyd/stas_detection/pytorch-deeplab-xception-master/data_new/test_whole_reult_t/modify/1722405-F_res1.png',[0, 0, 0, 0])