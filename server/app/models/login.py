from app import db
class LoginModel(db.Model):
    __tablename__ = 'login' 
    id = db.Column(db.Integer, primary_key=True,index=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(200))
    imgPath = db.Column(db.String(100))