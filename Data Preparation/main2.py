import data_prep as dp
import os
import json


def save_file(rutaDirectorio, nombreArchivo, stringAGuardar):
    if rutaDirectorio[len(rutaDirectorio)-1] != "/":
        rutaDirectorio += "/"

    newFile = open(rutaDirectorio+nombreArchivo, "w+", encoding="utf-8")
    newFile.write(stringAGuardar)
    return


def load_file(rutaDirectorio, nombreArchivo):
    archivoCargado = open(rutaDirectorio+nombreArchivo, "r+", encoding="utf-8")
    return archivoCargado


root_path = '/home/tomas/Desktop/Mineria de Datos/ProyectoFinal-MineriaDeDatos/noncomm_use_subset/'
root_results_prep = '/home/tomas/Desktop/Mineria de Datos/ProyectoFinal-MineriaDeDatos/preprocessed_papers/'

if not os.path.exists(root_results_prep):
    os.makedirs(root_results_prep)

files = sorted(
    list(os.listdir(root_path[:len(root_path) - 1])))
count = 1
for file in files:
    print(count)
    paper = load_file(root_path, file)
    paper_json = json.load(paper)

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
    prep_paper['body_text'] = abstract
    prep_paper['abstract'] = body_text
    save_file(root_results_prep, file, str(prep_paper))
    count += 1
