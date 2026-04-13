# keep_alive.py
from flask import Flask
from threading import Thread
import requests
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
    
    # Self-ping every 10 minutes
    while True:
        try:
            requests.get('https://your-app.onrender.com')
        except:
            pass
        time.sleep(600)
