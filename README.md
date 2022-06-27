# OpenCV-Cascade-Classifier
使用OpenCV的级联分类器识别中国象棋棋子

OpenCV级联分类器模型训练


#### 文件夹内容：

Dataset_Red_Black文件夹保存了采集的棋子图片，是经过灰度化及中值滤波后的图片，红色棋子和黑色棋子图片分开保存，每种颜色7类棋子，每类棋子经筛选后保留200张各种角度的图片。

model_save文件夹保存了使用上述数据集训练好的级联分类器模型，包括红色棋子分类模型Red_Chess.yml和黑色棋子分类模型Black_Chess.yml，该模型可在recognize.py中直接使用。

TestPicture文件夹保留了4张用于测试的图片，检测模型分类的准确率。


#### 各py文件功能：

##### getDataSet.py:

运行该程序，手动转动棋子，采集棋子各角度图片用于训练模型。

##### train.py:

使用级联分类器训练分类模型。

##### recognize.py:

测试模型效果，TestPicture文件夹中有几张测试图片，也可直接处理摄像头实时画面。



使用级联分类器时，如果类别数量过多识别速度会很低，所以对棋子分类的解决方法是先使用其他方法（如判断R通道阈值）判断出棋子颜色（红色或黑色），再将该棋子送入对应颜色的棋子分类模型，这样棋子类别由14降为7，识别速度能加快，实测同时识别32个棋子帧率在0.7-0.8帧，约5帧内可以识别出全部棋子。



下面的测试结果中并没有先判断棋子颜色再将其送入到对应模型内，因此每种颜色的模型会对所有颜色的棋子进行识别，自行忽略其它颜色棋子的识别结果。

#### 红色棋子识别结果（请忽略黑色棋子）：

**Test1图片红色棋子识别结果：**

<div align=left><img width=500 src="image\Test1红色棋子分类结果.jpg">

**Test2图片红色棋子识别结果：**

<div align=left><img width=500 src="image\Test2红色棋子分类结果.jpg">

**Test3图片红色棋子识别结果：**

<div align=left><img width=500 src="image\Test3红色棋子分类结果.jpg">

**Test4图片红色棋子识别结果：**

<div align=left><img width=500 src="image\Test4红色棋子分类结果.jpg">



#### 黑色棋子识别结果（请忽略红色棋子）：

**Test1图片黑色棋子识别结果：**

<div align=left><img width=500 src="image\Test1黑色棋子分类结果.jpg">

**Test2图片黑色棋子识别结果：**

<div align=left><img width=500 src="image\Test2黑色棋子分类结果.jpg">

**Test3图片黑色棋子识别结果：**

<div align=left><img width=500 src="image\Test3黑色棋子分类结果.jpg">

**Test4图片黑色棋子识别结果：**

<div align=left><img width=500 src="image\Test4黑色棋子分类结果.jpg">
