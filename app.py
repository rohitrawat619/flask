from flask import Flask, jsonify, request,g, flash, redirect,url_for, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_wtf.csrf import CSRFProtect
from mysql.connector import Error
import mysql.connector
import jwt
import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'rohtirawat676'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['WTF_CSRF_ENABLED'] = True

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Cafe#676#',
    'database': 'flaskcurdapi'
}

db = SQLAlchemy(app)
api = Api(app)
csrf = CSRFProtect(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100),unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
class Employee(db.Model):
         id = db.Column(db.Integer, primary_key=True)
         name = db.Column(db.String(100),unique=True, nullable=False)
         email = db.Column(db.String(100), nullable=False)

from forms import EmployeeForm

with app.app_context():
    db.create_all()
    
    
def get_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None   

@app.route('/', methods=['GET', 'POST'])
def index():
    form = EmployeeForm()
    if form.validate_on_submit():
        from models import EmployeeDetails
        db.create_all()
        new_employee = EmployeeDetails(
            name=form.name.data,
            email=form.email.data,
            age=form.age.data
        )
        # Add to database
        db.session.add(new_employee)
        db.session.commit()

        flash('Employee data has been saved!', 'success')
        return redirect(url_for('index'))
    
    return render_template('form.html', form=form)

@app.route('/empregister', methods=['GET', 'POST'])
def empregister():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        
        if not name or not email:
                 return {'message': 'missing name or email or position'},400
        if Employee.query.filter_by(email=email).first():
            return {'message': 'Username already taken'},400
        
        employee = Employee(name=name, email=email)
        
        db.session.add(employee)
        db.session.commit()
        return {'message':f"Employee {name},{email} registered successfully!"},200

    return render_template('hacked.html')
    
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

@app.route('/items', methods=['GET'])
def get_items():
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM items')
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        items = [{'id': row[0], 'name': row[1], 'description': row[2]} for row in rows]
        return jsonify(items)
    else:
        return jsonify({"error": "Database connection failed"}), 500

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM items WHERE id = %s', (item_id,))
        row = cursor.fetchone()
        cursor.close()
        connection.close()
        if row:
            item = {'id': row[0], 'name': row[1], 'description': row[2]}
            return jsonify(item)
        return jsonify({"error": "Item not found"}), 404
    else:
        return jsonify({"error": "Database connection failed"}), 500

@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        abort(400)
    name = request.json['name']
    description = request.json.get('description', "")
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO items (name, description) VALUES (%s, %s)', (name, description))
        connection.commit()
        cursor.close()
        item_id = cursor.lastrowid
        connection.close()
        return jsonify({'id': item_id, 'name': name, 'description': description}), 201
    else:
        return jsonify({"error": "Database connection failed"}), 500

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if not request.json:
        abort(400)
    name = request.json.get('name')
    description = request.json.get('description')
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE items SET name = %s, description = %s WHERE id = %s', (name, description, item_id))
        connection.commit()
        cursor.close()
        connection.close()
        if cursor.rowcount:
            return jsonify({'id': item_id, 'name': name, 'description': description})
        return jsonify({"error": "Item not found"}), 404
    else:
        return jsonify({"error": "Database connection failed"}), 500

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM items WHERE id = %s', (item_id,))
        connection.commit()
        cursor.close()
        connection.close()
        if cursor.rowcount:
            return jsonify({"message": "Item deleted"}), 200
        return jsonify({"error": "Item not found"}), 404
    else:
        return jsonify({"error": "Database connection failed"}), 500

if __name__ == "__main__":
    app.run(debug=True)
