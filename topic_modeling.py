from gensim import corpora, models
import pandas as pd
import pyLDAvis.gensim
from data_loading import DataLoader, save_file, delete_content
import config
import pickle5 as pickle
import time
from sklearn.feature_extraction.text import CountVectorizer
import smart_open

print("Starting data loading")
data_loader = DataLoader()
print("Finishied data loading")


def get_corpus_topics(lda, dictionary, corpus, dic_topics):
    dict_result = {}
    data = data_loader.get_processed_papers()

    topic_paper = []

    for tokens in data:
        text_data = []
        for token in tokens['body_text']:
            for tok in token:
                text_data.append(tok)

        bow = dictionary.doc2bow(text_data)
        document_topics = lda.get_document_topics(
            bow=bow)
        for topic in document_topics:
            if float(topic[1]) <= 0.2:
                topic_id = topic[0]
                if tokens['title'] == "" and tokens['abstract'] != "":
                    topic_paper_appearance = {
                        'paper_id': tokens['paper_id'], 'title': tokens['abstract'], 'frecuencia': str(topic[1])}
                elif tokens['abstract'] == "" and tokens['title'] != "":
                    topic_paper_appearance = {
                        'paper_id': tokens['paper_id'], 'title': tokens['title'], 'frecuencia': str(topic[1])}
                else:
                    topic_paper_appearance = {
                        'paper_id': tokens['paper_id'], 'title': "", 'frecuencia': str(topic[1])}

                dic_topics[topic_id]['papers'].append(topic_paper_appearance)

        topic_paper.append(
            {'paper_id': tokens['paper_id'], 'topics': document_topics})

    #dic_paper_topic = {}
    return topic_paper, dic_topics


def training_model(number_topics=10, number_words=1):
    data = data_loader.get_processed_papers()

    data = pd.DataFrame(
        data, columns=['paper_id', 'title', 'abstract', 'body_text'])

    text_data = []

    for tokens in data['body_text']:
        for token in tokens:
            text_data.append(token)

    dictionary = corpora.Dictionary(text_data)
    corpus = [dictionary.doc2bow(text) for text in text_data]

    pickle.dump(corpus, open('corpus.pkl', 'wb'))
    dictionary.save('dictorionary.gensim')

    model = models.LdaModel(corpus, num_topics=number_topics,
                            id2word=dictionary, passes=15)
    model.save('model5.gensim')

    topics = model.print_topics(num_words=number_words)

    for topic in topics:
        print(topic)


def loadModel(is_display=False, number_words=1):
    print("Loading...")
    dictionary = corpora.Dictionary.load('dictorionary.gensim')
    corpus = pickle.load(open('corpus.pkl', 'rb'))
    lda = models.LdaModel.load('model5.gensim')

    topics = lda.print_topics(num_words=number_words)
    dic_topics = []
    for topic in topics:
        split_topic = topic[1].split("*\"")
        print("-" + str(split_topic))
        dic_topics.append({"topic": split_topic[1][:len(split_topic[1])-1],
                           "frecuency": split_topic[0],
                           "papers": []
                           })

    papers_topics, docs_topics = get_corpus_topics(
        lda, dictionary, corpus, dic_topics)

    if is_display is True:
        # pyLDAvis.enable_notebook()
        lda_display = pyLDAvis.gensim.prepare(
            lda, corpus, dictionary, sort=False)
        print("Load")
        pyLDAvis.save_html(lda_display, 'display.html')

    return docs_topics


# # Code to retrain the model
# start = time.time()
# local_time_start = time.ctime(start)
# print("Starting Training Model at " + str(local_time_start))
# training_model(number_topics=20)
# end = time.time()
# total_time = end - start
# local_time_end = time.ctime(end)
# print("Finished Tranining Model at " + str(local_time_end))
# format_total_time = time.strftime('%H:%M:%S', time.gmtime(total_time))
# print("Total Topic Modeling time: " + str(format_total_time) + " seconds")

def load_model():
    # Code to load the pass model
    start = time.time()
    local_time_start = time.ctime(start)
    print("Starting Loading at " + str(local_time_start))
    number_words = 1
    print(" - Number of words for topics loaded is: " + str(number_words))
    topics = loadModel(is_display=False, number_words=number_words)
    end = time.time()
    total_time = end - start
    local_time_end = time.ctime(end)
    print("Finished Loading Model at " + str(local_time_end))
    format_total_time = time.strftime('%H:%M:%S', time.gmtime(total_time))
    print("Total Topic Modeling Loading time: " +
          str(format_total_time) + " seconds")

    return topics


load_model()
