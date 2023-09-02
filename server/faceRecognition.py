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

def train_model():
    listdirs,imgs,targets = load_data()
    if imgs != [] :
        face_recognizer=cv2.face.EigenFaceRecognizer_create() 
        face_recognizer.train(imgs,targets)
        face_recognizer.save('./face_recognition.xml')
        return "数据加载成功"
    else:
        return "数据加载成功"
    

def face_recognition(temp_img):
    #预测的数据处理
    temp_img = change_img(temp_img)
    face_recognizer=cv2.face.EigenFaceRecognizer_create() 
    face_recognizer.read('./face_recognition.xml')
    target,confidence = face_recognizer.predict(temp_img) 
    listdirs = os.listdir('./app/uploads')
    img_path = listdirs[target]
    name = img_path.split('.')[0]
    print(confidence)
    if confidence < 1000:
        return name
    else:
        return ' '
    
