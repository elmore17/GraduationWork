from flask import Flask, render_template, request, url_for, flash, redirect, session
import psycopg2


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

conn = psycopg2.connect(database="kisprod",  
                        user="postgres", 
                        password="",  
                        host="localhost", 
                        port="5432")

cursor = conn.cursor()

@app.route('/')
@app.route('/login')
def login():
    return render_template('formauth.html')

@app.route('/login', methods=['POST'])
def login_post():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        cursor.execute(('''select password from adminbd where user_name='{}';''').format(username))
        passwords = cursor.fetchall()
        if passwords[0][0] == password:
            return redirect(url_for('mainpage'))
        else:
            return redirect(url_for('login'))

@app.route('/mainpage')
def mainpage():
    return render_template('main_page.html')

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))
    

app.run(host='0.0.0.0', port=83)