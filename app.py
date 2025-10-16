from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Get environment variable defined in the Dockerfile
    version = os.environ.get("APP_VERSION", "v1.0") 
    return f'Hello from the Dockerized CI/CD Pipeline! App Version: {version}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)