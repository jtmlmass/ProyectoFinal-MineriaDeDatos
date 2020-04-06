
from file_reader import file_reader
import glob


class processing:
    def __init__(self, params):
        self.dict_ = {'title': [], 'paper_id': [],
                      'abstract': [], 'body_text': []}
        self.root_path = params['root_path']
        self.all_json = self.get_all_json()
        for idx, entry in enumerate(self.all_json):
            if idx % (len(self.all_json) // 10) == 0:
                print(f'Processing index: {idx} of {len(self.all_json)}')
            content = file_reader(entry)
            self.dict_['paper_id'].append(content.paper_id)
            self.dict_['title'].append(content.title)
            self.dict_['abstract'].append(content.abstract)
            self.dict_['body_text'].append(content.body_text)

    def get_all_json(self):
        return glob.glob(
            f'{self.root_path}/noncomm_use_subset/*.json', recursive=True)
