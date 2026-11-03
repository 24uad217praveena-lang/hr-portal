from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to HR Portal</h1>
    <h2>PaaS Cloud Deployment</h2>
    <p>HR Portal Successfully Deployed!</p>
    """

@app.route('/employee')
def employee():
    return """
    <h2>Employee Details</h2>
    <p>Employee ID: 101</p>
    <p>Name: Arun</p>
    <p>Department: IT</p>
    """

@app.route('/leave')
def leave():
    return """
    <h2>Leave Management</h2>
    <p>Leave Management Service Active</p>
    """

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000))
    )
