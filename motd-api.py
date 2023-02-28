import os
from flask import Flask, jsonify

app = Flask(__name__)

message = os.environ.get('MESSAGE', 'Salutation')
app_port = os.environ.get('APP_PORT', 8080)

@app.route('/motd')
def motd():
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(port=app_port)
