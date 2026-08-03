from flask import Flask, jsonify
import serverless_wsgi  # Import the AWS Lambda adapter wrapper

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to my Serverless Flask App!</h1>"

@app.get('/api/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

# This handler function is what AWS Lambda calls whenever an HTTP request arrives.
def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)
