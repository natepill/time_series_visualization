from flask import Flask, render_template, request, redirect
import requests

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

    diet = request.args.get('')



def test_request():
    parser = argparse.ArgumentParser()
    parser.add_argument("diet")
    parser.add_argument("timeline", type =list)
    args = parser.parse_args()





if __name__ == "__main__":
    app.run(debug=True, port=5000)
