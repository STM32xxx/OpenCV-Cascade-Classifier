import cv2
import os
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()

images = [] # 保存图片像素值数据
labels = [] # 保存图片标签

def read_path(path_name):
    for dir_item in os.listdir(path_name): # os.listdir()方法用于返回指定路径中包含的文件或文件夹的列表
        full_path = os.path.abspath(os.path.join(path_name, dir_item))

        if os.path.isdir(full_path): # 如果是文件夹，继续递归调用，去读取文件夹里的内容
            read_path(full_path)
        else:
            if dir_item.endswith('.jpg'): # 找到jpg文件
                image = cv2.imread(full_path,0) # 以灰度形式打开图片
                if image is None: # 遇到部分数据有点问题，报错'NoneType' object has no attribute 'shape'
                    pass
                else:
                    images.append(image)
                    labels.append(int(path_name.split('\\')[-1])) # 将数据集的文件夹名做标签

read_path('Dataset_Red_Black/red/') # 读取红色棋子文件，注意路径中不能有中文
# read_path('Dataset_Red_Black/black/')
print("recognizer training!")
recognizer.train(images, np.array(labels)) # 进行训练
recognizer.save('train/Red_Chess.yml') # 保存训练好的模型
# recognizer.save('train/Black_Chess.yml')
print("done!")


