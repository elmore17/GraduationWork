from flask import Flask, render_template, request, url_for, flash, redirect
import psycopg2


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

conn = psycopg2.connect(database="kisprod",  
                        user="postgres", 
                        password="",  
                        host="localhost", 
                        port="5432")

@app.route('/')
@app.route('/authorization', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = conn.cursor()
        cur.execute('SELECT * FROM adminBD') 
        user = cur.fetchone()
        if user[1]==username and user[2]==password:
            return "SO good`s"
    return render_template('formauth.html')
    

app.run(host='0.0.0.0', port=83)