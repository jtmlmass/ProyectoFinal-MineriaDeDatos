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
data_loader = DataLoader().get_instance()
print("Finishied data loading")


def training_model(number_topics=10, number_words=1):
    print("Get Files")
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

    dic_topics = {}
    for topic in topics:
        split_topic = topic[1].split("*\"")
        #split_topic[1] = split_topic.replace("\"", "")
        print("-" + str(split_topic))
        dic_topics[str(topic[0])] = {"topic": split_topic[1][:len(split_topic[1])-1],
                                     "frecuency": split_topic[0]
                                     }
        print(topic)
    print(str(dic_topics))

    if is_display is True:
        # pyLDAvis.enable_notebook()
        lda_display = pyLDAvis.gensim.prepare(
            lda, corpus, dictionary, sort=False)
        print("Load")
        pyLDAvis.save_html(lda_display, 'display.html')

    return dic_topics


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


# Code to load the pass model
start = time.time()
local_time_start = time.ctime(start)
print("Starting Loading at " + str(local_time_start))
number_words = 1
print(" - Number of words for topics loaded is: " + str(number_words))
loadModel(is_display=False, number_words=number_words)
end = time.time()
total_time = end - start
local_time_end = time.ctime(end)
print("Finished Loading Model at " + str(local_time_end))
format_total_time = time.strftime('%H:%M:%S', time.gmtime(total_time))
print("Total Topic Modeling Loading time: " +
      str(format_total_time) + " seconds")
