import cv2
import numpy as np
import os

def load_data():
    listdirs = os.listdir('./app/uploads')
    imgs = []
    targets = []
    # print(listdirs)
    for index,dir in enumerate(listdirs): 
        # print(index,dir)
        img = cv2.imread('./app/uploads/%s'%dir)
        #读取的图片是三维数据
        # print(imgs.shape)
        img = img[:,:,0]
        img = cv2.resize(img,(128,128))
        #转换为二维数据  
        # print(imgs_two.shape)
        imgs.append(img)
        targets.append(index)

    imgs = np.asarray(imgs)
    targets = np.asarray(targets)
    return listdirs,imgs,targets


def change_img(temp_img):
    img = cv2.imread(temp_img)
    img = img[:,:,0]
    img = cv2.resize(img,(128,128))
    return img


def face_recognition(temp_img):
    #预测的数据处理
    temp_img = change_img(temp_img)
    #加载数据
    listdirs,imgs,targets = load_data()
    # print(listdirs,imgs,targets)
    
    #加载人脸识别的算法
    face_recognizer=cv2.face.EigenFaceRecognizer_create()     #特征脸(EigenFaces)人脸识别
    #算法训练
    face_recognizer.train(imgs,targets)
    #进行预测
    target,confidence = face_recognizer.predict(temp_img) 
    img_path = listdirs[target]
    name = img_path.split('.')[0]
    print(name,confidence)
    if confidence < 500:
        return name
    else:
        name=''
        return name
    