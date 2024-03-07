import math

import numpy as np
import cv2

palette = (2 ** 11 - 1, 2 ** 15 - 1, 2 ** 20 - 1)
# 车辆统计
car_count = 0
car_count_list = []
temp = 0


def compute_color_for_labels(label):
    """
    Simple function that adds fixed color depending on the class
    """
    color = [int((p * (label ** 2 - label + 1)) % 255) for p in palette]
    return tuple(color)


def draw_boxes(img, bbox, identities=None, offset=(0, 0), car_count='', line=None):
    if line is not None:
        cv2.line(img, (line[0], line[1]), (line[2], line[3]), (0,0,255), 1, 8)

    for i, box in enumerate(bbox):
        x1, y1, x2, y2 = [int(i) for i in box]
        x1 += offset[0]
        x2 += offset[0]
        y1 += offset[1]
        y2 += offset[1]
        # box text and bar
        id = int(identities[i]) if identities is not None else 0
        color = compute_color_for_labels(id)
        label = '{}{:d}'.format("", id)
        t_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_PLAIN, 2, 2)[0]
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
        cv2.rectangle(img, (x1, y1), (x1 + t_size[0] + 3, y1 + t_size[1] + 4), color, -1)
        cv2.putText(img, label, (x1, y1 + t_size[1] + 4), cv2.FONT_HERSHEY_PLAIN, 2, [255, 255, 255], 2)
        cv2.putText(img, car_count, (20, 20), cv2.FONT_HERSHEY_PLAIN, 2, [255, 255, 255], 2)
    return img


# todo 计算车辆到划线的距离并判断是否过线
def calculate_distance(bbox, identities=None, line=None):
    # 关于line，第一个点始终是x坐标小的
    if line is None:
        return
    # 划线的一般方程
    A = line[3] - line[1]
    B = line[0] - line[2]
    C = line[2] * line[1] - line[0] * line[3]


    global car_count
    global temp
    for idx, box in enumerate(bbox):
        x1, y1, x2, y2 = [int(i) for i in box]
        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)

        id = int(identities[idx]) if identities is not None else 0
        # 先考虑划线为平行与坐标轴的情况,直接判断位置
        # if line[0] < cx < line[2] and cy > line[1]:
        #     # 判断这个id是否加过
        #     if car_count_list.__contains__(id):
        #         car_count_list.append(id)
        # 任意划线，算物体中心点到划线的直线距离
        d = (A * cx + B * cy + C) / math.sqrt(math.pow(A,2) + math.pow(B,2))
        if d < 0 and (max(line[1],line[3]) > cy > min(line[1],line[3]) or max(line[0],line[2]) > cx > min(line[0],line[2])):
            if not car_count_list.__contains__(id):
                car_count_list.append(id)
    car_count = temp + len(car_count_list)
    if len(car_count_list) > 1000:
        temp += len(car_count_list)
        car_count_list.clear()
    return car_count


if __name__ == '__main__':
    for i in range(82):
        print(compute_color_for_labels(i))
