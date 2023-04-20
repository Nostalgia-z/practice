import math
import cv2
import numpy as np
####################灰度图########################################
def gray_picture(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return img_gray

####################二值化########################################
def erzhihua(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rst = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    return rst[1]

##################加噪###########################################################
def add_noisy(image,n):    #椒盐彩色
    result = image.copy()
    w, h = image.shape[:2]
    for i in range(n):
        # 宽和高的范围内生成一个随机值，模拟表x,y坐标
        x = np.random.randint(1, w)
        y = np.random.randint(1, h)
        if np.random.randint(0, 2) == 0:
            # 生成白色噪声（盐噪声）
            result[x, y] = 0
        else:
            # 生成黑色噪声（椒噪声）
            result[x, y] = 255
    return result

####################添加高斯噪声#######################################
def add_noise(image,mean,var):
    img = np.array(image / 255, dtype=float)
    gauss = np.random.normal(mean, var/255, img.shape)
    noisy_img = img + gauss
    resultImg = np.clip(noisy_img, 0.0, 1.0)
    resultImg = np.uint8(resultImg * 255.0)
    return resultImg
################################直方图均衡化#####################################
def cal_equalhist(img):
    # 判断图像是否为三通道；
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.CV_8U)
    h , w = img.shape[0:2]
    # 无 Mask，256个bins,取值范围为[0,255]
    grathist = cv2.calcHist([img], [0], None, [256], [0, 255])

    zerosumMoment = np.zeros([256], np.uint32)
    for p in range(256):
        if p == 0:
            zerosumMoment[p] = grathist[0]
        else:
            zerosumMoment[p] = zerosumMoment[p - 1] + grathist[p]

    output_q = np.zeros([256], np.uint8)
    cofficient = 256.0 / (h * w)
    for p in range(256):
        q = cofficient * float(zerosumMoment[p]) - 1
        if q >= 0:
            output_q[p] = math.floor(q)
        else:
            output_q[p] = 0

    equalhistimage = np.zeros(img.shape, np.uint8)
    for i in range(h):
        for j in range(w):
            equalhistimage[i][j] = output_q[img[i][j]]

    return equalhistimage
###############亮度增强####################################################

def checkColor(img,count):
    height,width=img.shape[0:2]
    # 遍历每一个像素点
    for row in range(height):
        for col in range(width):
            #获取每个像素点的颜色值
            b,g,r=img[row,col]
            #增大当前颜色值
            newb=b+count
            newg=g+count
            newr=r+count
            #校验每个像素值不能越界
            newb=newb if newb<256 else 255
            newb=newb if newb>0 else 0
            newg=newg if newg<256 else 255
            newg=newg if newg>0 else 0
            newr=newr if newr<256 else 255
            newr=newr if newr>0 else 0
            img[row,col]=(newb,newg,newr)
    return img

################图像去噪####################################################
def boxFilterfun(image):       #方框滤波
    image=cv2.boxFilter(image,-1,(2,2),normalize=0)
    return image

def medianBlurfun(image):      #中值滤波
    image=cv2.medianBlur(image,3)
    return image

def bilateralFilterfun(image):   #双边滤波
    image=cv2.bilateralFilter(image,25,100,100)
    return image

def GaussianBlurfun(image):      #高斯滤波
    image=cv2.GaussianBlur(image,(5,5),0,0)
    return image

def blurfun(image):              #均值滤波
    image=cv2.blur(image,(5,5))
    return image

###############图像翻转####################################################
def flipfun(image,x):    #图像  水平翻转:1   垂直翻转:0  沿xy轴翻转:-1
    image = cv2.flip(image,x)
    return image

##############轮廓检测####################################################
def morphologyExfun(image):
    kernel = np.ones((3, 3), dtype=np.uint8)
    image_gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
    return image_gradient

#############sift检测#######################################################
def sift_fun(image):
    sift = cv2.SIFT_create()
    kps = sift.detect(image)
    image_sift = cv2.drawKeypoints(image, kps, None, -1, cv2.DrawMatchesFlags_DEFAULT)
    return image_sift
##################################图片修复##############################
def xiufu(image):
    # 图像进行二值化处理（将输入图像中的像素值大于245的像素设为255，将其余像素设为0，生成一个二值掩模mask1）
    _, mask1 = cv2.threshold(image, 245, 255, cv2.THRESH_BINARY)
    # 生成一个形状为矩形的结构元素k，大小为(3, 3)
    k = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # 膨胀操作，将掩模中的白色区域扩张，生成一个更大的掩模mask2
    mask1 = cv2.dilate(mask1, k)
    # 修复处理(cv2.INPAINT_NS 基于Navier-Stokes方程的修复算法,速度较慢，但需要较少的内存)
    result1 = cv2.inpaint(image, mask1[:, :, -1],5, cv2.INPAINT_NS)
    return result1

