myVideo = document.getElementById("video");
var face_data = "";
function openCamera() {
  cons = {
    video: {
      width: 300,
      height: 300,
    },
  };
  video = navigator.mediaDevices.getUserMedia(cons);
  video.then(function (videoStream) {
    myVideo.srcObject = videoStream;
    myVideo.play();
  });
}

function takephone() {
  canvas = document.getElementById("canvas");
  ctx = canvas.getContext("2d");
  ctx.drawImage(myVideo, 0, 0, canvas.width, canvas.height);
  face_data = canvas.toDataURL();
  face_data = face_data.substring(22);
}

function toLLogin() {
  window.location.href = "http://127.0.0.1:5500/login.html";
}

function toRegister() {
  window.location.href = "http://127.0.0.1:5500/register.html";
}

function register() {
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;
  var confirmPwd = document.getElementById("confirmPwd").value;
  img = face_data;
  data = {
    username: username,
    password: password,
    confirmPwd: confirmPwd,
    img: img,
  };
  $.ajax({
    url: "http://127.0.0.1:5000/register",
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "*/*",
    },
    data: JSON.stringify(data),
  }).done(function (res) {
    if (res.code == "1") {
      alert(res.msg);
      toLLogin();
    } else {
      alert(res.msg);
      toRegister();
    }
  });
}
