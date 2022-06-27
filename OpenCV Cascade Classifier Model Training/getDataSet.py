import cv2

cap = cv2.VideoCapture(1) # 打开USB摄像头

# chess = ('B_king','BR_car','BR_horse','B_elephant','BR_bishop','BR_cannon','B_pawn','R_king','R_elephant','R_pawn') # 1,2,3,4,5,6,7.8.9.10

chessBoardXY = (43,30) # 棋盘方格左上角坐标，(x,y)，→为x正方向，↓为y正方向
chessBoardWH = (400,430) # 棋盘方格宽和高，(width,height)

while True:
    ret, img = cap.read() # 读取一帧图像
    # img = img[5:470,150:590] # 感兴趣区域，去掉多余部分画面
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 转为灰度图
    fil  = cv2.medianBlur(gray, 3) # 中值滤波

    # 输入图像，方法（类型），dp(dp=1时表示霍夫空间与输入图像空间的大小一致，dp=2时霍夫空间是输入图像空间的一半，以此类推)，最短距离-可以分辨是两个圆否 则认为是同心圆 ,边缘检测时使用Canny算子的高阈值，中心点累加器阈值—候选圆心（霍夫空间内累加和大于该阈值的点就对应于圆心），检测到圆的最小半径，检测到圆的的最大半径
    circles = cv2.HoughCircles(fil,cv2.HOUGH_GRADIENT,1,32,param1=300,param2=20,minRadius=10,maxRadius=22)

    if not circles is None: # 检测到了圆
        for circle in circles[0]: # 遍历每一个圆
            x, y, r = int(circle[0]), int(circle[1]), 16 # 标记圆的半径为16

            if x<chessBoardXY[0] or y<chessBoardXY[1] or x>chessBoardWH[0] or y>chessBoardWH[1]: # 靠近边缘的棋子忽略
                continue

            sampleNum = sampleNum + 1
            r2 = 15
            cv2.imwrite("DataSet/" + '10' + '.' + str(sampleNum) + ".jpg", gray[y-r2:y+r2, x-r2:x+r2]) # 将检测到的棋子裁剪为30*30像素，保存图片

            cv2.circle(img, (x,y), r, (0,255,0), 2)

    cv2.rectangle(img, chessBoardXY, chessBoardWH, (255,255,0), 1, 4) # 标记棋盘方格最外圈轮廓

    cv2.imshow('HoughCircles', img)

    if cv2.waitKey(200) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


