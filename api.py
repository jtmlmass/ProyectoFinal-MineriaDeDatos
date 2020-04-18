import flask
from flask import request, jsonify
import topic_modeling as tm
from data_loading import DataLoader

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# Load needed data
topics = tm.load_model()
print("Starting data loading")
data_loader = DataLoader()
print("Finishied data loading")
processed_papers = data_loader.get_original_papers()


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
    return jsonify(processed_papers)


app.run()
