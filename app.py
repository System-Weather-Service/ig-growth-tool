from flask import Flask, render_template, request, redirect
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    # We will simulate the connection to avoid the IP block for now 
    # while we build the client-facing side
    
    return render_template('dashboard.html', username=user)

if __name__ == '__main__':
    app.run()