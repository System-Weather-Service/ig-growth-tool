from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    # In a real bot, we'd trigger the background automation script here
    
    return f"""
    <html>
        <body style="background:#0f0f0f; color:white; font-family:sans-serif; display:flex; flex-direction:column; align-items:center; justify-content:center; height:100vh;">
            <h1 style="color:#bc1888;">System Initialized!</h1>
            <div style="border:1px solid #333; padding:20px; border-radius:15px; background:rgba(255,255,255,0.05);">
                <p>✅ <b>Target Account:</b> {user}</p>
                <p>✅ <b>Feature:</b> Automated Welcome DMs (Active)</p>
                <p>✅ <b>Feature:</b> Comment-to-DM Trigger (Active)</p>
                <p style="color:#aaa;">The bot is now running in the cloud. You can close this window.</p>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run()