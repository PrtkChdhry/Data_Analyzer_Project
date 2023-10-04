from flask import Flask, render_template, request
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

if __name__ == '__main__':
    app.run(debug=True)
