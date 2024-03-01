
import os
def write():
    files = os.listdir("/home/hansheng/wyd/stas_detection/yolov7-main/runs/detect/exp24_best_0.75/1")
    print(files)
    for f in files:
        name=f
        if f.endswith("png"):
            with open(
                    '/home/hansheng/wyd/stas_detection/yolov7-main/data/data_512_to_512_all_129_addEmptyYin/dataSet/train.txt',
                    'a') as f:
                f.write("{}\n".format("/home/hansheng/wyd/stas_detection/yolov7-main/data/data_512_to_512_all_129_addEmptyYin/image/"+name))
def empty():
    path="/home/hansheng/wyd/stas_detection/yolov7-main/runs/detect/exp33/labels"
    files = os.listdir(path)
    print(files)
    for f in files:
        name=f
        if f.endswith("txt"):
            with open(
                    "/home/hansheng/wyd/stas_detection/yolov7-main/runs/detect/exp33/labels/"+f,
                    'r+') as f:
                f.seek(0)
                f.truncate()

                # f.write("{}\n".format("/home/hansheng/wyd/stas_detection/yolov7-main/data/data_512_to_512_all_129_addEmptyYin/image/"+name))
write()
# empty()