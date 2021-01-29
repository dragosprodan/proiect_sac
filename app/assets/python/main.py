from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize, sent_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

import pandas as pd
import utils

utils.import_resources()

def text_tokenization(text):
    tokenized_text = sent_tokenize(text)
    return tokenized_text

def word_tokenization(text):
    tokenized_word = word_tokenize(text)
    for el in tokenized_word:
        el.replace(' ','')
    return tokenized_word

# frec dist without stopwords
def filtered_frequency_distribution(tokenized_word):
    filtered_data = []
    stop_words = set(stopwords.words("english"))
    for w in tokenized_word:
        if w not in stop_words:
            filtered_data.append(w)
    fdist = FreqDist(filtered_data)
    return fdist

# normalize words
def lexicon_normalization(filtered_words):
    stem = PorterStemmer()
    normalized_words = []
    for w in filtered_words:
        normalized_words.append(stem.stem(w))
    return normalized_words

def lemmatization(filtered_words):
    lem = WordNetLemmatizer()
    lemmed_words = []
    for w in filtered_words:
        lemmed_words.append(lem.lemmatize(w,"v"))
    return lemmed_words

def frequency_distribution(tokenized_word):
    fdist = FreqDist(tokenized_word)
    fdist.plot(20, cumulative=False)

# if it's false then the text is informal
def language_register(tokenized_word, dictionary):
    count_data = []
    for word in dictionary:
        count = tokenized_word.count(word)
        count_data.append(count)
    if sum(count_data) > len(tokenized_word)/10:
        return False
    else:
        return True

# train with bag of words method
def train_sentiment_bow(data):
    token = RegexpTokenizer(r'[a-zA-Z0-9]+')
    cv = CountVectorizer(lowercase=True, stop_words='english', ngram_range=(1, 1), tokenizer=token.tokenize)
    text_counts = cv.fit_transform(data['Phrase'])
    X_train, X_test, y_train, y_test = train_test_split(text_counts, data['Sentiment'], test_size=0.3, random_state=1)
    clf = MultinomialNB().fit(X_train, y_train)
    predicted = clf.predict(X_test)
    print("MultinomialNB Accuracy:", metrics.accuracy_score(y_test, predicted))
    return clf, cv

#train using term frequency method
def train_sentiment_tf(data):
    tf = TfidfVectorizer()
    text_tf = tf.fit_transform(data['Phrase'])
    X_train, X_test, y_train, y_test = train_test_split(text_tf, data['Sentiment'], test_size=0.3, random_state=123)
    clf = MultinomialNB().fit(X_train, y_train)
    predicted = clf.predict(X_test)
    print("MultinomialNB Accuracy:", metrics.accuracy_score(y_test, predicted))
    return clf, tf

#test traind sent_analys using real data
def test_real_data(data, clf, tf):
    real_panda = pd.DataFrame(data)
    real_tf = tf.transform(real_panda[0])
    _, real_test, _, _ = train_test_split(real_tf, real_panda[0], test_size=len(data)-1, random_state=1)
    real_pred = clf.predict(real_test)
    return real_pred

def run():
    train_data = pd.read_csv('data/ml_train/train.tsv', sep='\t')
    clf, tf = train_sentiment_tf(train_data)
    real_data_list = utils.read_data("data/UK 1999.06.08.xml")
    for real_data in real_data_list:
        frequency_distribution(word_tokenization(real_data))
        pred = test_real_data(word_tokenization(real_data), clf, tf)
        print(sum(pred)/len(pred))

run()
