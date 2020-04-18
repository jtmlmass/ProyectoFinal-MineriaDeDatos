import flask
from flask import request, jsonify
import topic_modeling as tm

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
topics = tm.load_model()


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
            <p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/topics/all', methods=['GET'])
def api_all():
    return jsonify(topics)


app.run()
