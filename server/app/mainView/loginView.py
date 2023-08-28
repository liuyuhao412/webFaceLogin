from . import mainView
from flask import request,render_template,jsonify
from app.models.login import LoginModel
from app import db
from faceRecognition import face_recognition
import base64
from PIL import Image
from io import BytesIO
from hashlib import md5
import time

#将base64图片转换成jpg图片，并且返回图片的路径(注册)
def base64_to_image(username,base64String):
    decoded_image_data = base64.b64decode(base64String)
    image = Image.open(BytesIO(decoded_image_data))
    image = image.convert('RGB')
    path = 'app/uploads/'+username+'.jpg'
    image.save(path)
    return path
#登录
def base64_to_image_login(base64String):
    decoded_image_data = base64.b64decode(base64String)
    image = Image.open(BytesIO(decoded_image_data))
    image = image.convert('RGB')
    nowtime = time.time()
    path = 'app/temp/'+str(nowtime)+'.jpg'
    image.save(path)
    return path


#密码加密
def md5_password(pwd):
    m = md5()
    m.update(pwd.encode())
    pwd1 = m.hexdigest()
    return pwd1

@mainView.route('/register', methods=['post'])
def Register():
    data = request.get_json()
    username = data['username'].strip()
    password = data['password'].strip()
    confirmPwd = data['confirmPwd'].strip()
    img = data['img'].strip()
    if username == '':
        return jsonify({'code':'0', 'msg': '账号不能为空'})
    elif password =='':
        return jsonify({'code':'0', 'msg': '密码不能为空'})
    elif confirmPwd =='':
        return jsonify({'code':'0', 'msg': '再次输入密码不能为空'})
    elif img == '':
        return jsonify({'code':'0', 'msg': '请进行拍照'})
    else:
        loginUser = LoginModel.query.filter(LoginModel.username== username).first()
        if loginUser:
            return jsonify({'code':'0', 'msg': '该用户已经存在'})
        else:
            if(password == confirmPwd):
                registerUser=LoginModel()
                registerUser.username = username
                registerUser.password = md5_password(password)
                registerUser.imgPath = base64_to_image(username,img)
                db.session.add(registerUser)
                db.session.commit()
                return jsonify({'code':'1', 'msg': '注册成功'})
            else:
                return jsonify({'code':'0', 'msg': '两次密码不一致'})

@mainView.route('/login',methods=['POST'])
def login():
    data = request.get_json()
    username = data['username'].strip()
    password = data['password'].strip()
    if username == '':
        return jsonify({'code':'0', 'msg': '账号不能为空'})
    elif password =='':
        return jsonify({'code':'0', 'msg': '密码不能为空'})
    else:
        loginUser = LoginModel.query.filter(LoginModel.username==username).first()
        if loginUser:
            if loginUser.password == md5_password(password):
                return jsonify({'code':'1', 'msg': '登录成功'})
            else:
                return jsonify({'code':'0','msg':'密码错误'})
        else:
            return jsonify({'code':'0', 'msg': '账号不存在'})

@mainView.route('/faceLogin',methods=['POST'])
def faceLogin(): 
    data = request.get_json()
    img = data['img']
    img_path = base64_to_image_login(img)
    name = face_recognition(img_path)
    loginUser = LoginModel.query.filter(LoginModel.username==name).first()
    if loginUser:
        return jsonify({'code':'1', 'msg': '登录成功'})
    else:
        return jsonify({'code':'0', 'msg': '账号不存在'})
