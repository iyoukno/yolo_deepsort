'''
@Project ：DeepSORT_YOLOv5_Pytorch-master 
@File    ：sp_data.py
@Author  ：yuk
@Date    ：2023/11/7 15:19 
description：
'''
import os
import random
from shutil import copyfile

path = r'D:\datasets\car_reid\images'

train_path = path + '/train'
val_path = path + '/test'
if not os.path.isdir(train_path):
    os.mkdir(train_path)
    os.mkdir(val_path)

for root, dirs, files in os.walk(train_path, topdown=True):
    for dir in dirs:
        val_save_path = os.path.join(val_path, dir)
        if not os.path.exists(val_save_path):
            os.mkdir(val_save_path)
        name_list = os.listdir(root+'/'+dir)
        r_id = random.randint(0,len(name_list)-1)
        file_name = name_list[r_id]
        copyfile(root+'/'+dir+'/'+file_name, val_save_path+'/'+file_name)