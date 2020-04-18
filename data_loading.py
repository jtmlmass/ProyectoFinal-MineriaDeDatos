import config
from os import makedirs, path, listdir, remove
import json


def save_file(ruta_directorio, nombre_archivo, string_a_guardar):
    if ruta_directorio[len(ruta_directorio)-1] != "/":
        ruta_directorio += "/"

    new_file = open(ruta_directorio+nombre_archivo, "w+", encoding="utf-8")
    new_file.write(string_a_guardar)
    return


def load_file(ruta_directorio, nombre_archivo):
    archivoCargado = open(ruta_directorio+nombre_archivo,
                          "r+", encoding="utf-8")
    return archivoCargado


def delete_content(ruta_directorio):
    print("Deleting content from: " + ruta_directorio)
    filelist = [f for f in listdir(ruta_directorio) if f.endswith(".json")]
    for f in filelist:
        remove(path.join(ruta_directorio, f))
    print("Deleted content from: " + ruta_directorio)


class DataLoader:
    def __init__(self):
        super().__init__()

        if not path.exists(config.root_results_prep):
            makedirs(config.root_results_prep)

        self.files = sorted(
            list(listdir(config.root_path[:len(config.root_path) - 1])))

    def get_original_papers(self):
        papers = []
        print("Loading original Papers...")
        for file in self.files:
            paper = load_file(config.root_path, file)
            papers.append(json.load(paper))
        print("Finished Loading")
        return papers

    def get_processed_papers(self):
        papers = []
        print("Loading processed Papers...")
        for file in self.files:
            paper = load_file(config.root_results_prep, file)
            papers.append(json.load(paper))
        print("Finished Loading")
        return papers
