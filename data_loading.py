import config
from os import makedirs, path, listdir
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


class data_loader:
    __instance = None

    def get_instance(self):
        if data_loader.__instance == None:
            data_loader()
        return data_loader.__instance

    def __init__(self):
        super().__init__()

        if data_loader.__instance != None:
            raise Exception("This class has already been accessed")
        else:
            data_loader.__instance = self

        if not path.exists(config.root_results_prep):
            makedirs(config.root_results_prep)

        files = sorted(
            list(listdir(config.root_path[:len(config.root_path) - 1])))

    def get_crude_papers(self):
        papers = []
        count = 1
        for file in self.files:
            print(count)
            paper = load_file(config.root_path, file)
            papers.append(json.load(paper))
        return papers

    def get_processed_papers(self):
        papers = []
        count = 1
        for file in self.files:
            print(count)
            paper = load_file(config.root_results_prep, file)
            papers.append(json.load(paper))
        return papers
