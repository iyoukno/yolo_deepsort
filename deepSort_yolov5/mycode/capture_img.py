'''
@Project ：DeepSORT_YOLOv5_Pytorch-master 
@File    ：capture_img.py
@Author  ：yuk
@Date    ：2023/11/1 11:43 
description：
'''
import cv2


input_path = r'D:\project\car_count\DeepSORT_YOLOv5_Pytorch-master\testDir\cir2.MP4'
save_path = r'D:\datasets\car_reid\imgs'
cap = cv2.VideoCapture(input_path)

i = 0
while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        cv2.imwrite(save_path+f'/{i}.jpg',frame)
        i += 1
    else:
        cap.release()
cap.release()