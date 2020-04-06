import json


class file_reader:
    def __init__(self, self_path):
        with open(self_path) as file:
            content = json.load(file)
            self.title = content['metadata']['title']
            self.paper_id = content['paper_id']
            self.abstract = []
            self.body_text = []
            # Abstract
            for entry in content['abstract']:
                self.abstract.append(entry['text'])
            for entry in content['body_text']:
                self.body_text.append(entry['text'])
            self.abstract = '\n'.join(self.abstract)
            self.body_text = '\n'.join(self.body_text)

    def __repr__(self):
        return f'{self.paper_id}: {self.abstract[:50]}... {self.body_text[:50]}...'
