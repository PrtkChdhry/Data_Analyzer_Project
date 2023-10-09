from flask import Flask, render_template, request, send_file
import pandas as pd
from pandas_profiling import ProfileReport

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded CSV file
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            df = pd.read_csv(uploaded_file)
            profile = ProfileReport(df, explorative=True)

            return render_template('result.html', report=profile)
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

from flask import request

@app.route('/static/forms/contact.php', methods=['GET','POST'])
def contact_form():
    if request.method == 'POST':
        # Access form data
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        Message = request.form.get('Message')
        # Process the data as needed
        # Return a response, render a template, or redirect
        return "Form submitted successfully"


if __name__ == '__main__':
    app.run(debug=True)
