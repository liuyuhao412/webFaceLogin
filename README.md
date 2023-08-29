# 项目介绍
此项目是HTML5 + flask构建的web客户端人脸登录系统，可以实现用户注册，用户登录以及人脸登录等功能。

## 说明

> 如果您对此项目感兴趣，可以点 ”star“支持一下 谢谢！    

>开发环境 python3.8 

>如果有问题直接在issue中提出，或者您发现问题并有更好的解决方案，欢迎交流。

## 环境依赖

首先确保您的电脑上安装python3.8及以上版本的python。

再根据server文件夹里的requirements文件来安装项目所需要的依赖。



## 项目结构

│  README.md      //帮助文档       
  
├─client     //前端文件夹       
  │  index.html        //首页        
  │  login.html             //登录页面        
  │  register.html          //注册页面        
  │        
  ├─css               //页面的样式文件夹        
  │      login.css         
  │      register.css          
  │      reset.css         
  │         
  ├─images         //前端页面所需要的图片文件夹        
  │        bk.jpg        
  │      
  └─js     //页面所需要的js文件夹        
             face-min.js        
             jquery-3.2.1.min.js        
             login.js        
             register.js        
             tracking-min.js        
      
└─server         //后端文件夹        
    │  config.py            //后端数据库的配置文件夹     
    │  faceRecognition.py      //人脸识别的算法      
    │  manage.py         //主程序入口      
    │  requirements.txt      //后端环境依赖文件夹       
    │        
    └─app                 //项目文件夹        
        │  __init__.py        
        │       
        ├─mainView       //登录页面的api接口        
        │      loginView.py        
        │      __init__.py        
        │         
        ├─models       //创建数据库的文件夹       
        │      login.py         
        │      __init__.py        
        │         
        ├─temp                   //用于存放前端实时传来的登录人脸图像       
        └─uploads            //用于存放数据库里的人脸图像        

## 项目运行

* 在config.py文件夹里配置数据库的相关信息。
* 首先可以使用manage.py来创建数据库
  * 需要用*drop_db(app)*、*create_db(app)*，注释app.run()。
  * 运行manage.py文件。
* 用manage.py来运行后端文件
  * 需要用app.run()，注释*drop_db(app)*、*create_db(app)*。
  * 运行manage.py文件。
* 运行前端login.html文件。

## 注意

* 在进行人脸登录之前首先要确保数据库里有用户信息才能进行用户登录。



## 版本内容更新

v1.0.0：

>实现了用户注册功能

>实现了用户登录功能

>实现了人脸登录功能

