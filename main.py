from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def health_check():
    return 'Bot is online!', 200

def run_flask():
    app.run(host='0.0.0.0', port=10000)

if __name__ == "__main__":
    # Run Flask in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    
    # Run Discord bot
    bot.run(os.getenv('DISCORD_TOKEN'))
