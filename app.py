from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Vijay M J"
    username = os.getenv("USER") or os.getenv("USERNAME") or "unknown"

    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S.%f")

    try:
        top_output = subprocess.getoutput("top -b -n 1")
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"

    return f"""
    <h2>Name: {full_name}</h2>
    <h3>Username: {username}</h3>
    <h3>Server Time: {server_time}</h3>
    <pre>{top_output}</pre>
     """

if __name__ == '__main__':
    app.run(debug=True)
