from flask import Flask, jsonify, request, render_template, send_file
import json
# import os

app = Flask(__name__)

@app.route("/") 
def hello(): 
    message = "Hello, World"
    return render_template('index.html',  
                           message=message) 

@app.route('/favicon.ico')
def favicon():
    return send_file('favicon.ico', mimetype='image/vnd.microsoft.icon')

# This takes an html form post and prints it to the console returning success to the browser
@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    print(data)
    return render_template('response.html',
                           message="success")
    

if __name__ == '__main__':
    app.run(debug=True)

