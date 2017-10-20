from flask import Flask, render_template
import urllib
import json

app = Flask(__name__)


@app.route('/')
def index():

    response        = urllib.request.urlopen('https://data.cityofchicago.org/resource/tt4n-kn4t.json?$where=starts_with(job_titles,%20%27CHIEF%27)')
    data  = json.load(response)


    records =[]

    for record in data:
        print (record)

        records.append(record)

    return render_template('index.html', records=records)


if __name__ == '__main__':
    # Starts the Flask application server
    app.run(debug=True)
