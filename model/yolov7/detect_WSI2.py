import argparse
import time
from pathlib import Path
import numpy as np
import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random

from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized, TracedModel
from preprocess.Slide.openslide_func import openSlide as opensvs
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
def get_res_contours(path):
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
    # print(area)
    for aa in area:
        res_contours.append(contours[aa[0]])
        # if aa[1] / area[0][1] > 0.5:
        #     res_contours.append(contours[aa[0]])
    return res_contours
def judge_box_in_contour_1(res_contours,dot_list):
    for con in res_contours:
        # print('patchcenter:',(dot_list[0]+dot_list[2])/2, (dot_list[1]+dot_list[3])/2)
        # print(cv2.pointPolygonTest(con, ((dot_list[0]+dot_list[2])/2, (dot_list[1]+dot_list[3])/2), False))
        if cv2.pointPolygonTest(con, ((dot_list[0]+dot_list[2])/2, (dot_list[1]+dot_list[3])/2), False)==1 or cv2.pointPolygonTest(con, (dot_list[0] , dot_list[1]), False) == 1 or cv2.pointPolygonTest(con, (dot_list[0], dot_list[3]), False) == 1 or cv2.pointPolygonTest(con, (dot_list[2], dot_list[1]), False) == 1 or cv2.pointPolygonTest(con, (dot_list[2], dot_list[3]), False) == 1 :
            return False

    return True
def judge_box_in_contour(path,dot_list):

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
    res_contours=[]
    area=sort_area(area)
    # print(area)
    for aa in area:
        # res_contours.append(contours[aa[0]])
        if aa[1]/area[0][1]>0.5:
            res_contours.append(contours[aa[0]])

    for con in res_contours:
        # print('patchcenter:',(dot_list[0]+dot_list[2])/2, (dot_list[1]+dot_list[3])/2)
        # print(cv2.pointPolygonTest(con, ((dot_list[0]+dot_list[2])/2, (dot_list[1]+dot_list[3])/2), False))
        if cv2.pointPolygonTest(con, ((dot_list[0]+dot_list[2])/2, (dot_list[1]+dot_list[3])/2), False)==1 or cv2.pointPolygonTest(con, (dot_list[0] , dot_list[1]), False) == 1 or cv2.pointPolygonTest(con, (dot_list[0], dot_list[3]), False) == 1 or cv2.pointPolygonTest(con, (dot_list[2], dot_list[1]), False) == 1 or cv2.pointPolygonTest(con, (dot_list[2], dot_list[3]), False) == 1 :
            return False

    return True

def letterbox(img, new_shape=(640, 640), color=(114, 114, 114), auto=True, scaleFill=False, scaleup=True, stride=32):
    # Resize and pad image while meeting stride-multiple constraints
    shape = img.shape[:2]  # current shape [height, width]
    if isinstance(new_shape, int):
        new_shape = (new_shape, new_shape)

    # Scale ratio (new / old)
    r = min(new_shape[0] / shape[0], new_shape[1] / shape[1])
    if not scaleup:  # only scale down, do not scale up (for better test mAP)
        r = min(r, 1.0)

    # Compute padding
    ratio = r, r  # width, height ratios
    new_unpad = int(round(shape[1] * r)), int(round(shape[0] * r))
    dw, dh = new_shape[1] - new_unpad[0], new_shape[0] - new_unpad[1]  # wh padding
    if auto:  # minimum rectangle
        dw, dh = np.mod(dw, stride), np.mod(dh, stride)  # wh padding
    elif scaleFill:  # stretch
        dw, dh = 0.0, 0.0
        new_unpad = (new_shape[1], new_shape[0])
        ratio = new_shape[1] / shape[1], new_shape[0] / shape[0]  # width, height ratios

    dw /= 2  # divide padding into 2 sides
    dh /= 2

    if shape[::-1] != new_unpad:  # resize
        img = cv2.resize(img, new_unpad, interpolation=cv2.INTER_LINEAR)
    top, bottom = int(round(dh - 0.1)), int(round(dh + 0.1))
    left, right = int(round(dw - 0.1)), int(round(dw + 0.1))
    img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)  # add border
    return img, ratio, (dw, dh)
def detect(save_img=False):





    source, weights, view_img, save_txt, imgsz, trace = opt.source, opt.weights, opt.view_img, opt.save_txt, opt.img_size, not opt.no_trace
    save_txt=True

    save_img = not opt.nosave and not source.endswith('.txt')  # save inference images
    webcam = source.isnumeric() or source.endswith('.txt') or source.lower().startswith(
        ('rtsp://', 'rtmp://', 'http://', 'https://'))

    # Directories
    save_dir = Path(increment_path(Path(opt.project) / opt.name, exist_ok=opt.exist_ok))  # increment run
    (save_dir / 'labels' if save_txt else save_dir).mkdir(parents=True, exist_ok=True)  # make dir

    # Initialize
    set_logging()
    device = select_device(opt.device)
    half = device.type != 'cpu'  # half precision only supported on CUDA

    # Load model
    model = attempt_load(weights, map_location=device)  # load FP32 model
    stride = int(model.stride.max())  # model stride
    imgsz = check_img_size(imgsz, s=stride)  # check img_size

    if trace:
        model = TracedModel(model, device, opt.img_size)

    if half:
        model.half()  # to FP16



    # # Set Dataloader
    # vid_path, vid_writer = None, None
    # if webcam:
    #     view_img = check_imshow()
    #     cudnn.benchmark = True  # set True to speed up constant image size inference
    #     dataset = LoadStreams(source, img_size=imgsz, stride=stride)
    # else:
    #     dataset = LoadImages(source, img_size=imgsz, stride=stride)

    # Get names and colors
    names = model.module.names if hasattr(model, 'module') else model.names
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in names]

    # Run inference
    if device.type != 'cpu':
        model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))  # run once
    old_img_w = old_img_h = imgsz
    old_img_b = 1

    t0 = time.time()
    import os
    # list_slide=os.listdir(source)
    # list_slide = os.listdir('/home/hansheng/wyd/stas_detection/data/yinxing/')
    list_slide = os.listdir('/home/hansheng/wyd/stas_detection/pytorch-deeplab-xception-master/data_new/11/')
    #
    contour_path='/home/hansheng/wyd/stas_detection/data/split_result_yang/1/'
    # contour_path='/home/hansheng/wyd/stas_detection/data/split_result/'

    svs_pa='/home/hansheng/wyd/stas_detection/data/data/'
    yinxing_pa='/home/hansheng/wyd/stas_detection/data/yinxing/'
    for i in range(len(list_slide)):
        list_slide[i]=list_slide[i].replace('_res1','').replace('png','svs')
    # list_slide=['1638522-I.svs','1641013-A.svs','1705746-H.svs','1709582-N.svs','1715182-D.svs','1717112-F.svs','1717112-H.svs','1642544-G.svs']
    count = 0
    for ss in list_slide:

        flag=0
        s = opensvs(svs_pa+ss)
        patch_size = 512
        step = 512
        name=ss.replace('.svs','')
        res_contours=get_res_contours(contour_path + name + '_res1.png')
        cur_slide = s.read(location=[0, 0], scale=1)
        print(cur_slide.shape)
        # resize_ratio = s.level_downsamples[level] / 8
        whole_size_i = cur_slide.shape[0]  # y
        whole_size_j = cur_slide.shape[1]  # x

        patch_size_i = patch_size
        patch_size_j = patch_size
        for i in range(0, whole_size_i, step):
            for j in range(0, whole_size_j, step):
                if judge_box_in_contour_1(res_contours,
                                        [i,j , i + patch_size, j + patch_size]) == False:

                    continue
                # print(1)
                if i + patch_size_i > whole_size_i:
                    i = whole_size_i - patch_size_i
                if j + patch_size_j > whole_size_j:
                    j = whole_size_j - patch_size_j
                img = cur_slide[i:i + patch_size, j:j + patch_size, :]
                img0 = img.copy()
                # img0 = img0[:, :, ::-1]


                img = letterbox(img, 512, stride=32)[0]

                img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416

                img = np.ascontiguousarray(img)
                # img = img[0:3, :, :].unsqueeze(0)
                img = torch.from_numpy(img).to(device)

                img = img.half() if half else img.float()  # uint8 to fp16/32

                # img = img[0:3, :, :].unsqueeze(0).cuda()
                img /= 255.0  # 0 - 255 to 0.0 - 1.0
                if img.ndimension() == 3:
                    img = img.unsqueeze(0)
                if device.type != 'cpu' and (
                        old_img_b != img.shape[0] or old_img_h != img.shape[2] or old_img_w != img.shape[3]):
                    old_img_b = img.shape[0]
                    old_img_h = img.shape[2]
                    old_img_w = img.shape[3]
                    for i in range(3):
                        model(img, augment=opt.augment)[0]
                    # Inference
                t1 = time_synchronized()
                with torch.no_grad():  # Calculating gradients would cause a GPU memory leak
                    pred = model(img, augment=opt.augment)[0]
                t2 = time_synchronized()

                # Apply NMS
                pred = non_max_suppression(pred, opt.conf_thres, opt.iou_thres, classes=opt.classes,
                                           agnostic=opt.agnostic_nms)
                t3 = time_synchronized()

                path=name+'_'+str(i)+'_'+str(j)+'.png'
                # Process detections
                for j, det in enumerate(pred):  # detections per image
                    p, s, im0, frame = path, '', img0, 0

                    p = Path(p)  # to Path
                    save_path = str(save_dir / p.name)  # img.jpg
                    # print(p.name,save_path)
                    # sava_path=save_dir/p
                    gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
                    if len(det):
                        # Rescale boxes from img_size to im0 size
                        det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                        # Print results
                        for c in det[:, -1].unique():
                            n = (det[:, -1] == c).sum()  # detections per class
                            s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

                        # Write results
                        for *xyxy, conf, cls in reversed(det):
                            if save_txt:  # Write to file
                                xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(
                                    -1).tolist()  # normalized xywh
                                line = (cls, *xywh, conf) if opt.save_conf else (cls, *xywh)  # label format
                                with open(save_dir / 'labels' / (path.replace('.png','') + '.txt'), 'a') as f:
                                    f.write(('%g ' * len(line)).rstrip() % line + '\n')

                            if save_img or view_img:  # Add bbox to image
                                label = f'{names[int(cls)]} {conf:.2f}'
                                plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=1)

                    # Print time (inference + NMS)
                    # print(f'{s}Done. ({(1E3 * (t2 - t1)):.1f}ms) Inference, ({(1E3 * (t3 - t2)):.1f}ms) NMS')


                    # Save results (image with detections)
                    if save_img and len(det)>0:
                    # if save_img:
                        im0 = im0[:, :, ::-1]
                        cv2.imwrite(save_path, im0)
                        print(f" The image with the result is saved in: {save_path}")
                        flag=1
                    if save_txt or save_img:
                        s = f"\n{len(list(save_dir.glob('labels/*.txt')))} labels saved to {save_dir / 'labels'}" if save_txt else ''
                        # print(f"Results saved to {save_dir}{s}")
        if flag==1:
            count+=1
            # flag=0

        print(str(count) + '/' + str(len(list_slide)))
        print(f'Done. ({time.time() - t0:.3f}s)')
        # exit()







if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default='/home/hansheng/wyd/stas_detection/yolov7-main/runs/train/exp26/weights/best.pt', help='model.pt path(s)')
    parser.add_argument('--source', type=str, default='/home/hansheng/wyd/stas_detection/pytorch-deeplab-xception-master/data_new/test_whole_new', help='source')  # file/folder, 0 for webcam
    parser.add_argument('--img-size', type=int, default=512, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.8, help='object confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.5, help='IOU threshold for NMS')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--view-img', action='store_true', help='display results')
    parser.add_argument('--save-txt', action='store_true', help='save results to *.txt')
    parser.add_argument('--save-conf', action='store_true', help='save confidences in --save-txt labels')
    parser.add_argument('--nosave', action='store_true', help='do not save images/videos')
    parser.add_argument('--classes', nargs='+', type=int, help='filter by class: --class 0, or --class 0 2 3')
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--update', action='store_true', help='update all models')
    parser.add_argument('--project', default='runs/detect', help='save results to project/name')
    parser.add_argument('--name', default='exp', help='save results to project/name')
    parser.add_argument('--exist-ok', action='store_true', help='existing project/name ok, do not increment')
    parser.add_argument('--no-trace', action='store_true', help='don`t trace model')
    opt = parser.parse_args()
    print(opt)
    #check_requirements(exclude=('pycocotools', 'thop'))

    with torch.no_grad():
        if opt.update:  # update all models (to fix SourceChangeWarning)
            for opt.weights in ['yolov7.pt']:
                detect()
                strip_optimizer(opt.weights)
        else:
            detect()
