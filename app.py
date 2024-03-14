from flask import Flask, send_from_directory
import os



app = Flask(__name__,static_folder='frontend/build/static')

@app.route('/')
def index():
    return send_from_directory(os.path.join(os.getcwd(), 'frontend', 'build'), 'index.html')

if __name__ == '__main__':
    app.run()
