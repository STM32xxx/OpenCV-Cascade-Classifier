import cv2
import os


TestPicturePath = 'TestPicture' # 测试图片保存路径

recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer.read('model_save/Black_Chess.yml') # 加载黑色棋子分类模型
recognizer.read('model_save/Red_Chess.yml') # 加载红色棋子分类模型
font = cv2.FONT_HERSHEY_SIMPLEX

chess = ('No','Kin','Car','Hor','Can','Bis','Ele','Paw','Kin','Car','Hor','Can','Bis','Ele','Paw','Uk') # 用于标记的文本

for dirItem in os.listdir(TestPicturePath): # 遍历所有测试图片
    picPath = os.path.abspath(os.path.join(TestPicturePath, dirItem))
    print('-'*50)
    print(picPath)

    imgSource = cv2.imread(picPath) # 读入一幅图片
    gray = cv2.cvtColor(imgSource, cv2.COLOR_BGR2GRAY) # 转为灰度图
    fil  = cv2.medianBlur(gray, 3) # 中值滤波

    # 输入图像，方法（类型），dp(dp=1时表示霍夫空间与输入图像空间的大小一致，dp=2时霍夫空间是输入图像空间的一半，以此类推)，最短距离-可以分辨是两个圆否 则认为是同心圆 ,边缘检测时使用Canny算子的高阈值，中心点累加器阈值—候选圆心（霍夫空间内累加和大于该阈值的点就对应于圆心），检测到圆的最小半径，检测到圆的的最大半径
    circles = cv2.HoughCircles(fil, cv2.HOUGH_GRADIENT, 1, 40, param1=700, param2=20, minRadius=16, maxRadius=32)
    if not circles is None: # 检测到了圆
        for circle in circles[0]: # 遍历每一个圆
            x, y, r = int(circle[0]), int(circle[1]), 28 # 标记圆半径固定为28
            
            # if x<HoughRange[0] or y<HoughRange[1] or x>HoughRange[2] or y>HoughRange[3]:
            #     continue

            r2 = 15
            imgID, conf = recognizer.predict(gray[y-r2:y+r2, x-r2:x+r2]) # 对检测到的棋子灰度图进行分类

            if conf < 200: # 与样本中的数据置信度较高
                imgID = chess[imgID]
            else: # 置信度较低，标记为未知
                imgID = "Unknown"

            cv2.circle(imgSource, (x,y), r, (0,255,0), 2) # 标记检测到的棋子位置
            cv2.putText(imgSource, imgID, (x-20, y), font, 0.7, (255, 0, 0), 2) # 标记棋子ID

    cv2.imshow('res', imgSource)
    cv2.waitKey(0)

