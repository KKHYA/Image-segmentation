# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 21:33:43 2021

@author: ZMY
"""

from PIL import Image
import os, sys

Img1 = Image.open('./FT/Example.jpg') #需要处理的原图路径
width, height = Img1.size
side = max(width, height)
Img2 = Image.new(Img1.mode, (side, side), color='white')

if width > height:
    Img2.paste(Img1, (0, int((side - height) / 2)))
else:
    Img2.paste(Img1, (int((side - width) / 2), 0))

one_third_side = int(side / 3)

box_list = []
for x in range(3):
    for y in range(3):
        lower_left = x * one_third_side
        upper_left = y * one_third_side
        lower_right = (x + 1) * one_third_side
        upper_right = (y + 1) * one_third_side
        box = (lower_left, upper_left, lower_right, upper_right)
        box_list.append(box)

path = './'	#需要存储到的文件夹路径
isExists = os.path.exists(path+'FT') #创建的文件夹名称（如果存储到已有文件夹则不需要此行）
if not isExists:
    os.makedirs(path+'FT') #需要存储到的文件夹名称
    print('%s 目录创建成功')
else:
    print('%s 目录已经存在')
    sys.exit(0)

for i in range(0,9):
    Img3 = Img2.crop(box_list[i]) 
    Img3.save('./FT/%d.png' %(i)) #图片存储路径