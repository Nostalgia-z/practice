import sys
import numpy as np
import cv2 as cv
import picture_fun
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit,QDesktopWidget,\
                            QFileDialog,QFrame,QVBoxLayout,QHBoxLayout,QGroupBox,QGridLayout,QLabel
from PyQt5.QtGui import QIcon,QImage,QPixmap,qRgb
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MyWindow(QWidget):
    def __init__(self):
        # 切记一定要调用父类的__int__方法，因为它里面有很多对UI空间的初始化操作
        super(MyWindow, self).__init__()
        self.init_UI()
    def init_UI(self):
        # 设置窗口大小
        self.resize(1280,720)
        # 设置窗口标题
        self.setWindowTitle("颂奇图像处理工具")
        # 设置左上角图标（logo）
        self.setWindowIcon(QIcon("./picture/logo2.png"))
        # 获取中心坐标
        center_pointer = QDesktopWidget().availableGeometry().center()
        # 输出屏幕中心坐标
        # print(center_pointer)
        x = center_pointer.x()
        y = center_pointer.y()
        # 拆包
        old_x, old_y, width, height = self.frameGeometry().getRect()
        # 自动移动窗口到屏幕中心
        self.move((int)(x-width/2),(int)(y-height/2))

        # 最外层的垂直布局，包含三部分：处理按钮、图像显示区、使用注意区
        container = QVBoxLayout()
        self.setStyleSheet("background-color:#333333;")
        A_Box = QHBoxLayout()
        # -----创建第1个组，添加多个组件-----
        # 操作组
        Actions_box = QGroupBox("处理")
        # 整体垂直布局
        v_layout = QVBoxLayout()
        # 设置上下左右边距
        v_layout.setContentsMargins(10,20,10,8)
        # 网格布局
        grid = QGridLayout()
        btn1 = QPushButton("选择图片")
        btn1.clicked.connect(self.getfile)
        btn1.setStyleSheet("border: 1px solid white;")
        btn1.pressed.connect(self.on_btn_pressed)
        btn1.released.connect(self.on_btn_released)
        btn1.setFixedSize(100,27)

        btn2 = QPushButton("显示原图")
        btn2.clicked.connect(self.btn2_clicked)
        btn2.setStyleSheet("border: 1px solid white;")
        btn2.pressed.connect(self.on_btn_pressed)
        btn2.released.connect(self.on_btn_released)
        btn2.setFixedSize(100,27)

        btn3 = QPushButton("灰度图")
        btn3.clicked.connect(self.btn3_clicked)
        btn3.setStyleSheet("border: 1px solid white;")
        btn3.pressed.connect(self.on_btn_pressed)
        btn3.released.connect(self.on_btn_released)
        btn3.setFixedSize(100,27)

        btn4 = QPushButton("二值化")
        btn4.clicked.connect(self.btn4_clicked)
        btn4.setStyleSheet("border: 1px solid white;")
        btn4.pressed.connect(self.on_btn_pressed)
        btn4.released.connect(self.on_btn_released)
        btn4.setFixedSize(100,27)

        btn5 = QPushButton("轮廓检测")
        btn5.clicked.connect(self.btn5_clicked)
        btn5.setStyleSheet("border: 1px solid white;")
        btn5.pressed.connect(self.on_btn_pressed)
        btn5.released.connect(self.on_btn_released)
        btn5.setFixedSize(100,27)

        btn6 = QPushButton("图像修复")
        btn6.clicked.connect(self.btn6_clicked)
        btn6.setStyleSheet("border: 1px solid white;")
        btn6.pressed.connect(self.on_btn_pressed)
        btn6.released.connect(self.on_btn_released)
        btn6.setFixedSize(100,27)

        btn7 = QPushButton("Sift特征检测")
        btn7.clicked.connect(self.btn7_clicked)
        btn7.setStyleSheet("border: 1px solid white;")
        btn7.pressed.connect(self.on_btn_pressed)
        btn7.released.connect(self.on_btn_released)
        btn7.setFixedSize(100,27)

        btn8 = QPushButton("直方图均衡化")
        btn8.clicked.connect(self.btn8_clicked)
        btn8.setStyleSheet("border: 1px solid white;")
        btn8.pressed.connect(self.on_btn_pressed)
        btn8.released.connect(self.on_btn_released)
        btn8.setFixedSize(100,27)

        btn9 = QPushButton("亮度增强")
        btn9.clicked.connect(self.btn9_clicked)
        btn9.setStyleSheet("border: 1px solid white;")
        btn9.pressed.connect(self.on_btn_pressed)
        btn9.released.connect(self.on_btn_released)
        btn9.setFixedSize(100,27)

        btn10 = QPushButton("保存图片")
        btn10.clicked.connect(self.savefile)
        btn10.setStyleSheet("border: 1px solid white;")
        btn10.pressed.connect(self.on_btn_pressed)
        btn10.released.connect(self.on_btn_released)
        btn10.setFixedSize(100,27)

        grid.addWidget(btn1,0,0)
        grid.addWidget(btn2,0,1)
        grid.addWidget(btn3,0,2)
        grid.addWidget(btn4,0,3)
        grid.addWidget(btn5,0,4)
        grid.addWidget(btn6,1,0)
        grid.addWidget(btn7,1,1)
        grid.addWidget(btn8,1,2)
        grid.addWidget(btn9,1,3)
        grid.addWidget(btn10,1,4)
        v_layout.addLayout(grid)

        lvbo_box = QGroupBox("滤波")
        # 设置边距
        lvbo_layout = QHBoxLayout()
        lvbo_layout.setContentsMargins(0,10,0,0)

        btn14 = QPushButton("均值滤波")
        btn14.setStyleSheet("border: 1px solid white;")
        btn14.clicked.connect(self.btn14_clicked)
        btn14.pressed.connect(self.on_btn_pressed)
        btn14.released.connect(self.on_btn_released)
        btn14.setFixedSize(100,27)

        btn15 = QPushButton("中值滤波")
        btn15.setStyleSheet("border: 1px solid white;")
        btn15.clicked.connect(self.btn15_clicked)
        btn15.pressed.connect(self.on_btn_pressed)
        btn15.released.connect(self.on_btn_released)
        btn15.setFixedSize(100,27)

        btn16 = QPushButton("双边滤波")
        btn16.setStyleSheet("border: 1px solid white;")
        btn16.clicked.connect(self.btn16_clicked)
        btn16.pressed.connect(self.on_btn_pressed)
        btn16.released.connect(self.on_btn_released)
        btn16.setFixedSize(100,27)

        btn17 = QPushButton("高斯滤波")
        btn17.setStyleSheet("border: 1px solid white;")
        btn17.clicked.connect(self.btn17_clicked)
        btn17.pressed.connect(self.on_btn_pressed)
        btn17.released.connect(self.on_btn_released)
        btn17.setFixedSize(100,27)

        btn18 = QPushButton("方框滤波")
        btn18.setStyleSheet("border: 1px solid white;")
        btn18.clicked.connect(self.btn18_clicked)
        btn18.pressed.connect(self.on_btn_pressed)
        btn18.released.connect(self.on_btn_released)
        btn18.setFixedSize(100,27)
        lvbo_layout.addWidget(btn14)
        lvbo_layout.addWidget(btn15)
        lvbo_layout.addWidget(btn16)
        lvbo_layout.addWidget(btn17)
        lvbo_layout.addWidget(btn18)
        v_layout.addWidget(lvbo_box)
        lvbo_box.setLayout(lvbo_layout)

        # 添加到 box中
        Actions_box.setLayout(v_layout)


        # -----创建第2个组，添加多个组件-----
        HSV_box = QGroupBox("图像翻转")
        HSV_box.setAlignment(Qt.AlignCenter)
        fanzhuan_layout = QVBoxLayout()
        fanzhuan_layout.setAlignment(Qt.AlignCenter)

        btn11 = QPushButton("水平翻转")
        btn11.clicked.connect(self.btn11_clicked)
        btn11.setStyleSheet("border: 1px solid white;")
        btn11.pressed.connect(self.on_btn_pressed)
        btn11.released.connect(self.on_btn_released)
        btn11.setFixedSize(150,27)

        btn12 = QPushButton("垂直翻转")
        btn12.clicked.connect(self.btn12_clicked)
        btn12.setStyleSheet("border: 1px solid white;")
        btn12.pressed.connect(self.on_btn_pressed)
        btn12.released.connect(self.on_btn_released)
        btn12.setFixedSize(150,27)

        btn13 = QPushButton("沿X轴Y轴翻转")
        btn13.clicked.connect(self.btn13_clicked)
        btn13.setStyleSheet("border: 1px solid white;")
        btn13.pressed.connect(self.on_btn_pressed)
        btn13.released.connect(self.on_btn_released)
        btn13.setFixedSize(150,27)

        fanzhuan_layout.addWidget(btn11)
        fanzhuan_layout.addWidget(btn12)
        fanzhuan_layout.addWidget(btn13)

        HSV_box.setLayout(fanzhuan_layout)



        # -----创建第3个组，添加多个组件-----
        RGB_box = QGroupBox("加噪")
        RGB_box.setAlignment(Qt.AlignCenter)
        RGB_layout = QVBoxLayout()
        RGB_layout.addStretch(1)
        # 椒盐噪声
        label_layout = QHBoxLayout()
        label = QLabel("N:",self)
        label.setGeometry(0,0,30,20)
        self.edit = QLineEdit()
        self.edit.setPlaceholderText(" 默认:10000")
        self.edit.setStyleSheet("border: 1px solid white; font-size: 11px;")
        self.edit.setGeometry(55,20,50,20)
        btn19 = QPushButton("椒盐噪声")
        btn19.setStyleSheet("border: 2px solid white;")
        btn19.clicked.connect(self.btn19_clicked)
        btn19.pressed.connect(self.on_btn_pressed)
        btn19.released.connect(self.on_btn_released)
        btn19.setFixedSize(100,25)
        label_layout.addWidget(label)
        label_layout.addWidget(self.edit)
        label_layout.addWidget(btn19)
        RGB_layout.addLayout(label_layout)
        RGB_layout.addWidget(btn19)
        # 缩短间距
        RGB_layout.addSpacing(-15)

        # 高斯噪声
        label_layout1 = QHBoxLayout()
        label1 = QLabel("Mean:",self)
        label1.setGeometry(0,0,30,20)
        label2 = QLabel("Sigma:",self)
        label2.setGeometry(0,0,30,20)

        self.edit1 = QLineEdit(self)
        self.edit1.setPlaceholderText(" 默认:0")
        self.edit1.setStyleSheet("border: 1px solid white;font-size: 11px;")
        self.edit1.setGeometry(55,20,50,20)
        self.edit2 = QLineEdit(self)
        self.edit2.setPlaceholderText(" 默认:0")
        self.edit2.setStyleSheet("border: 1px solid white;font-size: 11px;")
        self.edit2.setGeometry(55,20,50,20)
        label_layout1.addWidget(label1)
        label_layout1.addWidget(self.edit1)
        label_layout1.addWidget(label2)
        label_layout1.addWidget(self.edit2)
        RGB_layout.addLayout(label_layout1)

        btn20 = QPushButton("高斯噪声")
        btn20.setStyleSheet("border: 2px solid white;")
        btn20.clicked.connect(self.btn20_clicked)
        btn20.pressed.connect(self.on_btn_pressed)
        btn20.released.connect(self.on_btn_released)
        btn20.setFixedSize(260,25)
        RGB_layout.addWidget(btn20)
        RGB_layout.addStretch(1)

        RGB_box.setLayout(RGB_layout)
        # 把操作的内容添加到容器中

        A_Box.addWidget(Actions_box,5)

        # 添加分割线
        line1 = QFrame()
        line1.setFrameShape(QFrame.VLine)
        line1.setFrameShadow(QFrame.Raised)
        line1.setLineWidth(5);
        line1.setMidLineWidth(0);
        line1.setStyleSheet("background-color: white;")
        A_Box.addWidget(line1)

        A_Box.addWidget(HSV_box,2)

        # 添加分割线
        line2 = QFrame()
        line2.setFrameShape(QFrame.VLine)
        line2.setFrameShadow(QFrame.Raised)
        line2.setLineWidth(2);
        line2.setMidLineWidth(0);
        line2.setStyleSheet("background-color: white;")
        A_Box.addWidget(line2)

        A_Box.addWidget(RGB_box,2)

        # 设置窗口显示的内容是最外层容器x
        container.addLayout(A_Box,1)
        self.setLayout(A_Box)


        # ------------------------------------------------

        B_box = QHBoxLayout()

        # -----创建第4个组，添加多个组件-----
        picture_box = QGroupBox("原图")
        picture_labout = QHBoxLayout()
        # 设置边距
        picture_labout.setContentsMargins(10,20,10,10)

        self.label = QLabel('')
        self.label.setAlignment(Qt.AlignCenter)
        picture_labout.addWidget(self.label)
        self.label.setMaximumSize(600,460)

        picture_box.setLayout(picture_labout)

    # -----创建第5个组，添加多个组件-----
        picture_box2 = QGroupBox("处理后")
        picture_labout2 = QHBoxLayout()
        # 设置边距
        picture_labout2.setContentsMargins(10,20,10,10)
        self.label_2 = QLabel('')
        self.label_2.setAlignment(Qt.AlignCenter)
        picture_labout2.addWidget(self.label_2)
        self.label_2.setMaximumSize(600,460)
        picture_box2.setLayout(picture_labout2)

        B_box.addWidget(picture_box)
        B_box.addWidget(picture_box2)

        # 添加分割线
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Raised)
        line.setLineWidth(5);
        line.setMidLineWidth(0);
        container.addWidget(line)

        container.addLayout(B_box,3)
        self.setLayout(B_box)



    # -----添加保存注释-----
        attention_label = QLabel("注: 使用 滤波功能、加噪功能、图像翻转、亮度增强功能 时需要先处理图片。")
        container.addWidget(attention_label)
        attention_label.setStyleSheet("color:#FFFFFF;")

        RGB_box.setStyleSheet("color:#FFFFFF;" "border:None")
        HSV_box.setStyleSheet("color:#FFFFFF;" "border:None;")

        Actions_box.setStyleSheet("color:#FFFFFF;" "border:0px solid rgba(255, 255, 255,80);")
        picture_box.setStyleSheet("color:#FFFFFF;" "border:3px hidden rgba(255, 255, 255,80);")
        self.label.setStyleSheet("color:#FFFFFF;" "border:2px solid white;""background-image: url('picture/addpicture.png')")

        picture_box2.setStyleSheet("color:#FFFFFF;" "border:3px hodden rgba(255, 255, 255,80);")
        self.label_2.setStyleSheet("color:#FFFFFF;" "border:2px solid white;""background-image: url('picture/addpicture2.png')")



        self.setLayout(container)
    # 定义按钮鼠标按下事件的响应函数
    def on_btn_pressed(self):
        button = self.sender()
        button.setStyleSheet('QPushButton {background-color: #222222; border: 1px solid white;}')
    # 定义按钮鼠标松开事件的响应函数
    def on_btn_released(self):
        button = self.sender()
        button.setStyleSheet('QPushButton {border: 1px solid white;}')
    # 选择本地图片
    def getfile(self):
        fname ,_ = QFileDialog.getOpenFileName(None,'选择图片','./','Image (*.jpg *.png *.jpge *.bmp)')
        if fname:
            # 使用OpenCV的cv2.imdecode(buf,flags)方法读取图片，解决 cv2.imread(filename) 方法不能读取中文路径的问题。
            img =cv.imdecode(np.fromfile(fname,dtype=np.uint8),-1)
            self.label.setStyleSheet("color:#FFFFFF;" "border:2px solid white;")
            h,w = img.shape[0:2]
            while w > 550 or h > 450:
                w = int(w*0.98)
                h = int(h*0.98)
            self.label.setPixmap(QPixmap(fname).scaled(w,h))
    # 保存图片
    def savefile(self):
        pix = self.label_2.pixmap()
        if pix :
            nfname = QFileDialog.getSaveFileName(None, "保存图片", "./", "Images *.jpg *.png *.jpge *.bmp")
            self.label_2.pixmap().save(nfname[0])
    # 显示原图
    def btn2_clicked(self):
        pix = self.label.pixmap()
        if pix:
            self.label_2.setStyleSheet("color:#FFFFFF;" "border:3px solid white;")
            self.label_2.setPixmap(pix)

    # 灰度图
    def btn3_clicked(self):
        pix = self.label.pixmap()
        if pix :
            self.label_2.setStyleSheet("color:#FFFFFF;" "border:3px solid white;")
            img = qimage2mat(pix)
            newimg = picture_fun.gray_picture(img)
            pix = matqimage(newimg)
            self.label_2.setPixmap(pix)
    # 二值化
    def btn4_clicked(self):
        pix = self.label.pixmap()
        if pix :
            self.label_2.setStyleSheet("color:#FFFFFF;" "border:3px solid white;")
            img = qimage2mat(pix)
            newimg = picture_fun.erzhihua(img)
            pix = matqimage(newimg)
            self.label_2.setPixmap(pix)
    # 轮廓检测
    def btn5_clicked(self):
        pix = self.label.pixmap()
        if pix:
            self.label_2.setStyleSheet("color:#FFFFFF;" "border:3px solid white;")
            img = qimage2mat(pix)
            newimg = picture_fun.morphologyExfun(img)
            pix = matqimage(newimg)
            self.label_2.setPixmap(pix)
    # 图片修复
    def btn6_clicked(self):
        pix = self.label.pixmap()
        if pix :
            self.label_2.setStyleSheet("color:#FFFFFF;" "border:3px solid white;")
            img = qimage2mat(pix)
            newimg = picture_fun.xiufu(img)
            pix = matqimage(newimg)
            self.label_2.setPixmap(pix)
    # Sift特征检测
    def btn7_clicked(self):
        pix = self.label.pixmap()
        if pix :
            self.label_2.setStyleSheet("color:#FFFFFF;" "border:3px solid white;")
            img = qimage2mat(pix)
            newimg = picture_fun.sift_fun(img)
            pix = matqimage(newimg)
            self.label_2.setPixmap(pix)
    # 直方图均衡化
    def btn8_clicked(self):
        pix = self.label.pixmap()
        if pix :
            self.label_2.setStyleSheet("color:#FFFFFF;" "border:3px solid white;")
            img = qimage2mat(pix)
            newimg = picture_fun.cal_equalhist(img)
            pix = matqimage(newimg)
            self.label_2.setPixmap(pix)
    # 亮度增强
    def btn9_clicked(self):
        pix = self.label_2.pixmap()
        if pix :
            self.label_2.setStyleSheet("color:#FFFFFF;" "border:3px solid white;")
            img = qimage2mat(pix)
            newimg = picture_fun.checkColor(img,50)
            pix = matqimage(newimg)
            self.label_2.setPixmap(pix)

    # 水平翻转
    def btn11_clicked(self):
        pix = self.label_2.pixmap()
        if pix :
            img = qimage2mat(pix)
            newimg = picture_fun.flipfun(img,1)
            pix = matqimage(newimg)
            self.label_2.setPixmap(pix)
    # 垂直翻转
    def btn12_clicked(self):
        pix = self.label_2.pixmap()
        if pix :
            img = qimage2mat(pix)
            newimg = picture_fun.flipfun(img,0)
            pix = matqimage(newimg)
            self.label_2.setPixmap(pix)
    # 沿 x y轴翻转
    def btn13_clicked(self):
        pix = self.label_2.pixmap()
        if pix :
            img = qimage2mat(pix)
            newimg = picture_fun.flipfun(img,-1)
            pix = matqimage(newimg)
            self.label_2.setPixmap(pix)

    # 滤波
    # 均值滤波
    def btn14_clicked(self):
        pix = self.label_2.pixmap()
        if pix :
            img = qimage2mat(pix)
            newimg = picture_fun.blurfun(img)
            pix = matqimage(newimg)
            self.label_2.setPixmap(pix)
    # 中值滤波
    def btn15_clicked(self):
        pix = self.label_2.pixmap()
        if pix :
            img = qimage2mat(pix)
            newimg = picture_fun.medianBlurfun(img)
            pix = matqimage(newimg)
            self.label_2.setPixmap(pix)
    # 双边滤波
    def btn16_clicked(self):
        pix = self.label_2.pixmap()
        if pix :
            img = qimage2mat(pix)
            newimg = picture_fun.bilateralFilterfun(img)
            pix = matqimage(newimg)
            self.label_2.setPixmap(pix)
    # 高斯滤波
    def btn17_clicked(self):
        pix = self.label_2.pixmap()
        if pix :
            img = qimage2mat(pix)
            newimg = picture_fun.GaussianBlurfun(img)
            pix = matqimage(newimg)
            self.label_2.setPixmap(pix)
    # 方框滤波
    def btn18_clicked(self):
        pix = self.label_2.pixmap()
        if pix :
            img = qimage2mat(pix)
            newimg = picture_fun.boxFilterfun(img)
            pix = matqimage(newimg)
            self.label_2.setPixmap(pix)
    # 椒盐噪声
    def btn19_clicked(self):
        pix = self.label_2.pixmap()
        if pix :
            img = qimage2mat(pix)
            num = self.edit.text()
            if num:
                num = int(num)
            else:
                num = 10000
            newimg = picture_fun.add_noisy(img,num)
            pix = matqimage(newimg)
            self.label_2.setPixmap(pix)
    # 高斯噪声
    def btn20_clicked(self):
        pix = self.label_2.pixmap()
        if pix :
            img = qimage2mat(pix)
            mean = self.edit1.text()
            Sigma = self.edit2.text()
            if mean:
                mean = int(mean)
            else:
                mean = 0
            if Sigma:
                Sigma = float(Sigma)
            else:
                Sigma = 0
            newimg = picture_fun.add_noise(img,mean,Sigma)
            pix = matqimage(newimg)
            self.label_2.setPixmap(pix)
def qimage2mat(qtpixmap: object) :    #qtpixmap转opencv
    qimg = qtpixmap.toImage()
    temp_shape = (qimg.height(), qimg.bytesPerLine() * 8 // qimg.depth())
    temp_shape += (4,)
    ptr = qimg.bits()
    ptr.setsize(qimg.byteCount())
    result = np.array(ptr, dtype=np.uint8).reshape(temp_shape)
    result = result[..., :3]
    return result

def matqimage(cvimg):       #opencv转QImage
    if cvimg.ndim==2:              #单通道
        height, width= cvimg.shape
        cvimg = cv.cvtColor(cvimg, cv.COLOR_BGR2RGB)
        # 计算每行所占字节数
        bytesPerLine = 3 * width
        cvimg = QImage(cvimg.data, width, height,bytesPerLine,QImage.Format_RGB888)
        pix = QPixmap.fromImage(cvimg)
        return pix
    else:                          #多个通道
        width = cvimg.shape[1]
        height = cvimg.shape[0]
        pixmap = QPixmap(width, height)  # 根据已知的高度和宽度新建一个空的QPixmap,
        qimg = pixmap.toImage()         # 将pximap转换为QImage类型的qimg
        for row in range(0, height):
            for col in range(0, width):
                b = cvimg[row, col, 0]
                g = cvimg[row, col, 1]
                r = cvimg[row, col, 2]
                pix = qRgb(r, g, b)
                qimg.setPixel(col, row, pix)
                pix = QPixmap.fromImage(qimg)

        return pix
if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()

    # 展示窗口
    w.show()
    # 程序进行循环等待状态
    sys.exit(app.exec_())