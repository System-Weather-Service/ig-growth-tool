from flask import Flask, render_template, request
from instagrapi import Client
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pw = request.form.get('password')
    
    try:
        # This is the "Brain" connecting to the account
        cl = Client()
        cl.login(user, pw)
        
        # Example of a "ManyChat" style Auto-DM to a specific target
        # In a real sale, you'd automate this for all new followers
        message = "Hi! This is an automated message from Akshay's Elite Tool. Thanks for connecting!"
        # cl.direct_send(message, [target_user_id]) 
        
        return f"<h1>Success!</h1><p>Bot is now linked to @{user} and monitoring for growth.</p>"
    
    except Exception as e:
        return f"<h1>Connection Error</h1><p>{str(e)}</p>"

if __name__ == '__main__':
    app.run()