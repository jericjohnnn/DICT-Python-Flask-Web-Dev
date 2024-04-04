from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, World!<h1>"
@app.route('/animal')
def animal():
    return """
    <h1>Fun animal facts!</h1>
    <p>paragraph</p>"""
