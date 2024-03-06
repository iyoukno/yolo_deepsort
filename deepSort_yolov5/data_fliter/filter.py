'''
@Project ：DeepSORT_YOLOv5_Pytorch-master 
@File    ：filter.py
@Author  ：yuk
@Date    ：2023/10/27 9:19 
description：
'''
new_l = []
with open(r'res.txt','r') as f:
    l = f.readlines()
    for i in l:
        new_l.append(i.strip().split(','))
    print(new_l)

