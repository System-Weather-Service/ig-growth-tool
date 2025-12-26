from flask import Flask, request, render_template, redirect, url_for, flash
from instagrapi import Client
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_123')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # This is where the login and growth logic happens
        flash('Campaign started! (Testing Mode)', 'success')
        return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run()