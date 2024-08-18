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
    # print(request.form.getlist('media'))
    # print(request.form["replicates"])
    
    # <OptionsSection title="Select Media" name="media" options={["lb", "m9"]} selectFirst={true} />
    # <OptionsSection title="Select a strain" name="strain" options={["top10", "dh5a"]} />
    # <OptionsSection title="Select a supplement" name="supplement" options={["atc", "iptg"]} />
    # <OptionsSection title="Select a vector" name="vector" options={["repressilator", "toggleswitch"]} />

    # <OptionSlider title="Number of replicates" name="replicates" min="1" max="10" initialVal="1" />

    lists = [
        request.form.getlist('media'),
        request.form.getlist('strain'),
        request.form.getlist('supplement'),
        request.form.getlist('vector')
    ]
    
    replicates = int(request.form["replicates"])
    
    excel_sheet(lists, replicates)
    
    return render_template('response.html',
                           message="success")
    
port = 4269
# webbrowser.open('http://localhost:'+str(port))
if __name__ == '__main__':
    app.run(debug=False, port=port, host='0.0.0.0')
