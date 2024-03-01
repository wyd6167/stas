import pickle
import matplotlib.pyplot as plt
import numpy as np
with open("pr.pkl","rb") as f:
    re7=pickle.load(f)
    pr7 = pickle.load(f)
with open("/home/hansheng/wyd/stas_detection/yolov5-master/pr.pkl","rb") as f:
    re5=pickle.load(f)
    pr5 = pickle.load(f)
with open("/home/hansheng/wyd/stas_detection/ssd-pytorch-master/pr.pkl","rb") as f:
    re_sdd=pickle.load(f)
    pr_sdd= pickle.load(f)
fig, ax = plt.subplots(1, 1, figsize=(9, 6), tight_layout=True)
ax.plot(re7, pr7, linewidth=3, color='blue', label='Yolov7 ap=0.78')
ax.plot(re5, pr5, linewidth=3, color='red', label='Yolov5 ap=0.76')
ax.plot(re_sdd, pr_sdd, linewidth=3, color='yellow', label='SSD ap=0.74')

ax.set_xlabel('Recall')
ax.set_ylabel('Precision')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
fig.savefig("/home/hansheng/wyd/stas_detection/yolov7-main/1.png", dpi=250)