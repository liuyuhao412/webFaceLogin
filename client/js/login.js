var video = document.getElementById("video");
var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");

function toRegister() {
  window.location.href = "http://127.0.0.1:5500/register.html";
}

function toLogin() {
  window.location.href = "http://127.0.0.1:5500/login.html";
}

function toIndex() {
  window.location.href = "http://127.0.0.1:5500/index.html";
}
//tab栏的切换
function tabChange() {
  var lis = document.querySelectorAll(".tab-list div");
  var items = document.querySelectorAll(".tab-items div");
  for (var i = 0; i < lis.length; i++) {
    lis[i].setAttribute("index", i);
    lis[i].onclick = function () {
      for (var j = 0; j < lis.length; j++) {
        lis[j].className = "";
      }
      this.className = "current";
      var index = this.getAttribute("index");
      for (var k = 0; k < items.length; k++) {
        items[k].style.display = "none";
      }
      items[index].style.display = "block";
      if (index == 1) {
        faceLogin();
        video.play();
      }
      if (index == 0) {
        toLogin();
      }
    };
  }
}

tabChange();
function login() {
  var username = document.getElementById("user").value;
  var password = document.getElementById("pwd").value;
  data = {
    username: username,
    password: password,
  };
  $.ajax({
    url: "http://127.0.0.1:5000/login",
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "*/*",
    },
    data: JSON.stringify(data),
  }).done(function (res) {
    if (res.code == "1") {
      alert(res.msg);
      toIndex();
    } else {
      alert(res.msg);
      toLogin();
    }
  });
}
//给后端发送人脸进行识别
function postFace() {
  setTimeout(() => {
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    img = canvas.toDataURL();
    img = img.substring(22);
    $.ajax({
      url: "http://127.0.0.1:5000/faceLogin",
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "*/*",
      },
      data: JSON.stringify({ img: img }),
      success: function (res) {
        if (res.code == 1) {
          alert(res.msg);
          toIndex();
        } else {
          postFace();
        }
      },
      error: function (callback) {
        postFace();
      },
    });
  }, 2000);
}

//获取摄像头
function getUserMediaToPhoto(constraints, success, error) {
  if (navigator.mediaDevices.getUserMedia) {
    //最新标准API
    navigator.mediaDevices.getUserMedia(constraints).then(success).catch(error);
  }
}

//成功的回调函数
function success(stream) {
  video.srcObject = stream;
  video.onloadedmetadata = function (e) {
    video.play();
  };
  postFace();
}

function error(error) {
  console.log("访问用户媒体失败：", error.name, error.message);
}

//人脸定时扫描登录
function faceLogin() {
  if (navigator.mediaDevices.getUserMedia) {
    getUserMediaToPhoto({ video: { width: 240, height: 180 } }, success, error);
  } else {
    alert("暂无媒体设备,请刷新试试");
  }
}
