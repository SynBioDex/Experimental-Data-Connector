import argparse
from flask import Flask, request, render_template, send_file
import webbrowser
from gensheet import excel_sheet

app = Flask(__name__)

@app.route("/") 
@app.route('/index.html')
def index():
    return send_file('templates/index.html', mimetype='text/html')

@app.route('/options.json')
def options():
    return send_file('options.json', mimetype='application/json')

@app.route('/favicon.ico')
def favicon():
    return send_file('favicon.ico', mimetype='image/vnd.microsoft.icon')

# This takes an html form post and prints it to the console returning success to the browser
@app.route('/submit', methods=['POST'])
def submit():
    # get the lists from the form
    lists = [
        request.form.getlist('media'),
        request.form.getlist('strain'),
        request.form.getlist('supplement'),
        request.form.getlist('vector')
    ]
    
    #check that all lists have at least one item
    for l in lists:
        if len(l) == 0:
            return render_template('response.html',
                                   message="Error, at least one item must be selected from each list, please go back.",
                                   color="red"
                                   )
    
    # get the number of replicates from the form
    replicates = int(request.form["replicates"])
    
    # generate the excel sheet
    excel_sheet(lists, replicates)
    
    # return success to the browser
    return render_template('response.html',
                           message="Success",
                           color="green"
                           )
    
port = 4269
# webbrowser.open('http://localhost:'+str(port))
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run Flask app with optional debug mode.')
    parser.add_argument('--debug', action='store_true', help='Run the Flask app in debug mode')
    args = parser.parse_args()

    app.run(debug=args.debug, port=port, host='0.0.0.0')
