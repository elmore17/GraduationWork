from flask import Flask, render_template, request, url_for, flash, redirect, session, jsonify
from flask_cors import CORS
import psycopg2
from pathlib import Path
from wwdocx import read_docx, create_draft


app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'your secret key'

conn = psycopg2.connect(database="kisprod",  
                        user="postgres", 
                        password="",  
                        host="localhost", 
                        port="5432")

cursor = conn.cursor()

@app.route('/login', methods=['POST'])
def login_post():
    if request.method == 'POST':
        username = request.json.get('username')
        password = request.json.get('password')
        cursor.execute(('''select password from adminbd where user_name='{}';''').format(username))
        passwords = cursor.fetchall()
        if passwords[0][0] == password:
            return jsonify({'message': 'Successfully'})
        else:
            return jsonify({'message': 'Error'})
        
@app.route('/addusers', methods=['POST'])
def add_users():
    if request.method == 'POST':
        user_name = request.json.get('user_name')
        post = request.json.get('post')
        cursor.execute('SELECT * FROM users WHERE user_name = %s', (user_name,))
        existing_user = cursor.fetchone()
        if existing_user:
            return jsonify({'message': 'User already exists'}), 400
        cursor.execute('INSERT INTO users (user_name, post) VALUES (%s, %s)', (user_name, post))
        conn.commit()
        return jsonify({'message': 'Successfully'})
    
@app.route('/getusers', methods=['GET'])
def get_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    user_list = []
    for user in users:
        user_dict = {
            'id': user[0],
            'user_name': user[1],
            'post': user[2]
        }
        user_list.append(user_dict)
    return jsonify({'users': user_list})

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        uploaded_file = request.files['file']
        downloads_directory = Path.home() / 'Downloads'
        file_path = downloads_directory / uploaded_file.filename
        uploaded_file.save(file_path)
        output_json = 'output.json'
        read_docx(file_path, output_json)
        create_draft(output_json)
        return {'status': 'success', 'message': 'File uploaded successfully'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}
    

app.run(host='0.0.0.0', port=83)