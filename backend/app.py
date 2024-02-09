from flask import Flask, render_template, request, url_for, flash, redirect, session, jsonify
from flask_cors import CORS
import psycopg2
from pathlib import Path
from wwdocx import read_docx, create_draft, create_json
import json
from flask_bcrypt import Bcrypt


app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)
app.config['SECRET_KEY'] = 'your secret key'

def get_db_connection():
    return psycopg2.connect(database="kisprod", user="postgres", password="", host="localhost", port="5432")

@app.route('/')
@app.route('/authorization')
def authorization():
    return render_template('Authorization.html')

@app.route('/registration')
def registration():
    return render_template('Registration.html')

@app.route('/gecpage')
def gecpage():
    return render_template('GecPage.html')

@app.route('/commissionpage')
def commissionpage():
    return render_template('CommissionPage.html')

@app.route('/login', methods=['POST'])
def login_post():
    if request.method == 'POST':
        username = request.form.get('login')
        password = request.form.get('password')
        
        #Получение информации о пользователе по логину
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("select password from adminbd where user_name= %s", (username,))
            user_data = cursor.fetchone()
            if user_data:
                hashed_password = user_data[0]
                if bcrypt.check_password_hash(hashed_password, password):
                    return redirect(url_for('gecpage'))
                else:
                    flash('Неверный логин или пароль', "info")
                    return redirect(url_for('authorization'))
            else:
                flash('Этот пользователь не найден', "info")
                return redirect(url_for('authorization'))
        

@app.route('/addadmin', methods=['POST'])
def add_admin():
    if request.method == 'POST':
        username = request.form.get('login')
        password = request.form.get('password1')
        password2 = request.form.get('password2')
        if password == password2:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            
            #Проверка наличия пользователя
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM adminbd WHERE user_name = %s", (username,))
                existing_user = cursor.fetchone()

                #Обработка ошибки о наличии пользователя
                if existing_user:
                    flash('Такой пользователь уже существует', "info")
                    return redirect(url_for('registration'))
            
            #Создание нового пользователя
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO adminbd (user_name, password) VALUES (%s, %s)", (username, hashed_password))
                conn.commit()
                return redirect(url_for('authorization'))
        else:
            flash('Пароли не совпадают', "info")
            return redirect(url_for('registration'))
        
@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        uploaded_file = request.files['file']
        downloads_directory = Path.home() / 'Downloads'
        file_path = downloads_directory / uploaded_file.filename
        uploaded_file.save(file_path)
        output_json = 'output.json'
        data_text = read_docx(file_path)
        create_json(data_text, output_json)
        return {'status': 'success', 'message': 'File uploaded successfully', 'filePath': str(file_path)}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

   
@app.route('/getjsoninfo', methods=['GET', 'POST'])
def get_json_info():
    json_file_path = 'output.json'
    if request.method == 'GET':
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            all_data = json.load(json_file)

            # Создаем список студентов
            students = []
            for entry in all_data:
                student_name = entry['student']
                score = entry['score']
                scoredip = entry['scoredip']

                # Создаем объект для каждого студента
                student = {'name': student_name, 'score': score, 'scoredip': scoredip}
                students.append(student)

        # Возвращаем список студентов в формате JSON
        return jsonify({'students': students})
    if request.method == 'POST':
        student = request.form.get('student')
        score = request.form.get('score')
        scoredip = request.form.get('scoredip')
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            all_data = json.load(json_file)
            for entry in all_data:
                if entry['student'] == student:
                    entry['score'] = score
                    entry['scoredip'] = scoredip
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(all_data, json_file, ensure_ascii=False, indent=4)
        return jsonify({'status': 'success'})

@app.route('/getusers', methods=['GET'])
def get_users():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users_commission')
        users = cursor.fetchall()
        user_list = []
        for user in users:
            user_dict = {
                'id': user[0],
                'user_name': user[1],
                'post': user[2],
                'data_start': user[3],
                'data_end': user[4]
            }
            user_list.append(user_dict)
        return jsonify({'users': user_list})
        
# @app.route('/addusers', methods=['POST'])
# def add_users():
#     if request.method == 'POST':
#         user_name = request.json.get('user_name')
#         post = request.json.get('post')
#         cursor.execute('SELECT * FROM users WHERE user_name = %s', (user_name,))
#         existing_user = cursor.fetchone()
#         if existing_user:
#             return jsonify({'message': 'User already exists'}), 400
#         cursor.execute('INSERT INTO users (user_name, post) VALUES (%s, %s)', (user_name, post))
#         conn.commit()
#         return jsonify({'message': 'Successfully'})
    

    

app.run(host='0.0.0.0', port=83)