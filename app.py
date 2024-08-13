from flask import Flask, jsonify, request,g
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_jwt_extended import create_access_token, JWTManager, get_jwt_identity, jwt_required
import jwt
import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'rohtirawat676'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'

db = SQLAlchemy(app)
api = Api(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100),unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
with app.app_context():
    db.create_all()
    
    
def token_required(f):
    def decorator(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].replace('Bearer ', '')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            g.data = data
        except:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(*args, **kwargs)
    return decorator

@app.route('/register', methods=['POST'])
def register():
# class UserRegistration(Resource):
#     def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']
        
        if not username or not password:
            return {'message': 'missing username or password'},400
        if User.query.filter_by(username=username).first():
            return {'message': 'Username already taken'},400
        
        new_user = User(username=username, password=password)
        
        db.session.add(new_user)
        db.session.commit()
        return {'message':'User created successfully'},200

@app.route('/login', methods=['POST'])
def login():
# class UserLogin(Resource):
#     def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']

        user =  User.query.filter_by(username=username).first()
            
        if user and user.password == password:
            # access_token = create_access_token(identity=user.id)  
            access_token = jwt.encode({'id': user.id, 'sub': user.username, 'exp': datetime.datetime.now() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'],algorithm='HS256')
            return jsonify({'token': access_token},200)
    
        return {'message':'Invalid Credentials'},401

@app.route('/secure', methods=['GET'])
@token_required
def secure():
# class ProtectedResource(Resource):
    # def get(self):
    # current_user_id = get_jwt_identity()
    # return {'message': f"hellow user {current_user_id}, you accessed the protected resuorce"},200
    user_data = g.data
    return jsonify({'message': 'This is a protected route', 'user_data': user_data})
    
# api.add_resource(UserRegistration,'/register')
# api.add_resource(UserLogin,'/login')
# api.add_resource(ProtectedResource,'/secure')

if __name__ == "__main__":
    app.run(debug=True)
