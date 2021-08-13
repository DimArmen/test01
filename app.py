from flask import Flask
from datetime import datetime
import socket
app = Flask(__name__)

now = datetime.now().strftime("%y/%m/%d %H:%M:%S")
localhost = socket.gethostname()
@app.route("/")
def index():
    return f'The app started at {now} on {localhost}'
