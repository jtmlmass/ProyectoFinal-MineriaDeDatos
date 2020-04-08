from gensim import corpora, models
from data_loading import DataLoader, save_file, delete_content
import pickle

data_loader = DataLoader().get_instance()
data = data_loader.get_original_papers()


def training_model():
    text_data = []
    for tokens in data['body_text']:
        for token in tokens:
            text_data.append(token)

    dictionary = corpora.Dictionary(text_data)
    corpus = [dictionary.doc2bow(text) for text in text_data]

    pickle.dump(corpus, open('corpus.pkl', 'wb'))
    dictionary.save('dictorionary.gensim')

    model = models.LdaModel(corpus, num_topics=5,
                            id2word=dictionary, passes=15)
    model.save('model5.gensim')

    topics = model.print_topics(num_words=4)

    for topic in topics:
        print(topic)
