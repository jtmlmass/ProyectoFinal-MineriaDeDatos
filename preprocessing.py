import data_prep as dp
import os
import json
from data_loading import DataLoader, save_file, delete_content
import config

print("Starting Preprocesing")
data_loader = DataLoader().get_instance()

count = 1
files = data_loader.get_original_papers()
delete_content(config.root_results_prep)

for paper_json in files:
    prep_paper = {}

    abstract = []
    for sentence in paper_json["abstract"]:
        abstract.append(" ".join(dp.process_text(sentence["text"])))

    body_text = []
    for sentence in paper_json["body_text"]:
        body_text.append(" ".join(dp.process_text(sentence["text"])))

    prep_paper['paper_id'] = paper_json['paper_id']
    prep_paper['title'] = " ".join(
        dp.process_text(paper_json['metadata']['title']))
    prep_paper['body_text'] = body_text
    prep_paper['abstract'] = abstract
    save_file(config.root_results_prep,
              paper_json["paper_id"]+".json", str(prep_paper))
    print(count)
    count += 1

print("Preprocessing complete!")
