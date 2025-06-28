from flask import Flask, render_template, jsonify, request
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'container_id': os.environ.get('HOSTNAME', 'unknown')
    })

@app.route('/api/info')
def info():
    return jsonify({
        'app_name': 'Dockerized Flask App',
        'version': '1.0.0',
        'environment': os.environ.get('FLASK_ENV', 'production'),
        'hostname': os.environ.get('HOSTNAME', 'unknown')
    })

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({
        'message': 'Echo response',
        'received_data': data,
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 