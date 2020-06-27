from . import db

class Employee(db.Model):
    __tablename__ = 'employees'
    
    id =  db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255),index = True)
    phoneno = db.Column(db.String(255),unique = True,index = True)
    birthdate = db.Column(db.String(255),index = True)
    position = db.Column(db.String(255),index = True)
    duties = db.Column(db.String(2000))
    earning = db.Column(db.String(255),index = True)
    
    def __repr__(self):
        return f'User {self.username}'