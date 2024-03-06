'''
@Project ：DeepSORT_YOLOv5_Pytorch-master 
@File    ：reques_to_java.py
@Author  ：yuk
@Date    ：2023/10/27 9:53 
description：异步方式，将每5帧的车辆id与位置信息给java
'''
from threading import Thread
from time import sleep, ctime
import requests

class MyThread(Thread):
    def __init__(self, func, args):
        '''
        :param func: 可调用的对象
        :param args: 可调用对象的参数
        '''
        Thread.__init__(self)   # 不要忘记调用Thread的初始化方法
        self.func = func
        self.args = args

    def run(self):
        for i in self.args:
            self.func(i)


def to_java(info):
    requests.get('url', params=info)
    pass