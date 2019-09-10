from flask import Flask, render_template, request, redirect
import requests
import pandas as pd

"""
Given dataset
retrieve features
Specify two dates for timeline
return json object diet column from that period

"""



app = Flask(__name__)

# Diet
# Timeline

@app.route('/')
def index():
    """ Return JSON for sliced dataframe """

    diet = request.args.get('diet')
    timeline = request.args.get('timeline')

    return str('{}: {}'.format(diet, timeline))



def test_request():
    parser = argparse.ArgumentParser()
    parser.add_argument("diet")
    parser.add_argument("timeline", type=list)
    args = parser.parse_args()

    print(args.diet, args.timeline)


    data = requests.get('http://127.0.0.1:5000/')

    print('DATA RETRIVED: {}'.format(data))





if __name__ == "__main__":
    app.run(debug=True, port=5000)
