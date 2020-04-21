import flask
from flask import request, jsonify
import topic_modeling as tm
from data_loading import DataLoader
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

# Load needed data
topics = tm.load_model()
print("Starting data loading")
data_loader = DataLoader()
print("Finishied data loading")
original_papers = data_loader.get_original_papers_dic()


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
            <p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/topics/all', methods=['GET'])
def api_topics_all():
    return jsonify({'data': topics})


@app.route('/api/papers/all', methods=['GET'])
def api_papers_all():
    return jsonify(original_papers)


@app.route('/api/papers/<paper_id>', methods=['GET'])
def api_paper_id(paper_id):

    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    # For trial: /api/papers/00a00d0edc750db4a0c299dd1ec0c6871f5a4f24
    try:
        paper = original_papers[paper_id]
    except KeyError:
        return "Error: Paper not found. "
    return jsonify(paper)


# host='0.0.0.0', port=80
app.run()
