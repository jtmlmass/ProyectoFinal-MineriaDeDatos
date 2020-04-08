import data_prep as dp
import os
import json
from data_loading import DataLoader, save_file, delete_content
import config

print("Starting Preprocesing")
data_loader = DataLoader().get_instance()

# Count to say which number of paper it's being pre processed
count = 1
# Loading the papers from data set
files = data_loader.get_original_papers()
# Delete the contents from the folder which saves the pre processed papers
delete_content(config.root_results_prep)

# Cicle for paper to paper
for paper_json in files:
    prep_paper = {}

    # Convert all the sentences in a list of STR sentences
    abstract = []
    for sentence in paper_json["abstract"]:
        abstract.append(" ".join(dp.process_text(sentence["text"])))

    body_text = []
    for sentence in paper_json["body_text"]:
        body_text.append(" ".join(dp.process_text(sentence["text"])))

    # Re asssign the values after formating
    prep_paper['paper_id'] = paper_json['paper_id']
    prep_paper['title'] = " ".join(
        dp.process_text(paper_json['metadata']['title']))
    prep_paper['body_text'] = body_text
    prep_paper['abstract'] = abstract

    # Save the file with it's ID as name in folder passed in config
    save_file(config.root_results_prep,
              paper_json["paper_id"]+".json", str(prep_paper))

    # Informing which paper it's finished
    print(count)
    count += 1

print("Preprocessing complete!")