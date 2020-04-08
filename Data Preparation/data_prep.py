from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import nltk

# # We need this dataset in order to use the tokenizer
# nltk.download('punkt')

# # Also download the list of stopwords to filter out
# nltk.download('stopwords')

stemmer = PorterStemmer()


def process_text(text):
    # Make all the strings lowercase and remove non alphabetic characters
    text = re.sub('[^A-Za-z]', ' ', text.lower())

    # Tokenize the text; this is, separate every sentence into a list of words
    # Since the text is already split into sentences you don't have to call sent_tokenize
    tokenized_text = word_tokenize(text)

    # Remove the stopwords and stem each word to its root
    clean_text = [
        stemmer.stem(word) for word in tokenized_text
        if (word not in stopwords.words('english') and (len(word)) > 2)
    ]

    # Remember, this final output is a list of words
    return clean_text
