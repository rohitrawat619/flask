from app import db

class EmployeeDetails(db.Model):
         
    __tablename__ = 'employee_details'
          
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)

