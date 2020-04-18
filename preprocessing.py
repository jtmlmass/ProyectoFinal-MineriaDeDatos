import data_prep as dp
import os
import json
from data_loading import DataLoader, save_file, delete_content
import config
import nltk
import re
import time

# # We need this dataset in order to use the tokenizer
nltk.download("punkt")

# # Also download the list of stopwords to filter out
nltk.download("stopwords")

print("Starting Preprocesing")
data_loader = DataLoader()

# Count to say which number of paper it"s being pre processed
count = 1
# Loading the papers from data set
files = data_loader.get_original_papers()
# Delete the contents from the folder which saves the pre processed papers
delete_content(config.root_results_prep)

start = time.time()
local_time_start = time.ctime(start)
print("Starting Preprocessing at " + str(local_time_start))
# Cicle for paper to paper
for paper_json in files:
    prep_paper = {}

    # Convert all the sentences in a list of STR sentences
    abstract = []
    for sentence in paper_json["abstract"]:
        abstract.append(dp.process_text(sentence["text"]))

    body_text = []
    for sentence in paper_json["body_text"]:
        body_text.append(dp.process_text(sentence["text"]))

    # Re asssign the values after formating
    prep_paper["paper_id"] = paper_json["paper_id"]
    prep_paper["title"] = " ".join(
        dp.process_text(paper_json["metadata"]["title"]))
    prep_paper["body_text"] = body_text
    prep_paper["abstract"] = abstract

    # Save the file with it"s ID as name in folder passed in config
    str_prep_paper = str(prep_paper)
    str_prep_paper = str_prep_paper.replace("\'", "\"")
    save_file(config.root_results_prep,
              paper_json["paper_id"]+".json", str_prep_paper)

    # Informing which paper it"s finished
    print(count)
    count += 1
end = time.time()
total_time = end - start
local_time_end = time.ctime(end)
print("Started Preprocessing at " + str(local_time_start))
print("Finished Preprocessing at " + str(end))
format_total_time = time.strftime('%H:%M:%S', time.gmtime(total_time))
print("Total Preprocessing time: " + str(format_total_time) + " seconds")
print("Preprocessing complete!")
