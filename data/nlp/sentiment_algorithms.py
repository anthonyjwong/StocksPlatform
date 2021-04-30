from statistics import mean
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize.treebank import TreebankWordDetokenizer
stop_words = stopwords.words('english')

import threading

thread_lock = threading.Lock()

def clean_sentence(txt: str):
    """
    Normalizes the words of article for better analysis.
    Ex: 'being' -> 'be', 'did' -> 'do'
    Also cleans headlines from stopwords and punctuation.
    @params list of
    @return list of str
    source: digitalocean.com
    """
    thread_lock.acquire()
    article_tokens = [w for w in nltk.word_tokenize(
        txt) if w.isalpha() and w.lower() not in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized_sentence = []
    for word, tag in pos_tag(article_tokens):
        if tag.startswith('NN'):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'
        lemmatized_sentence.append(lemmatizer.lemmatize(word, pos))
    thread_lock.release()
    return TreebankWordDetokenizer().detokenize(lemmatized_sentence)

def sentiment_value(doc):
    """
    Returns true if average sentiment by 
    sentence is positive, otherwise returns false
    @params string (news article)
    @return bool
    """
    txt = ' '.join([token.text for token in doc])
    sia = SentimentIntensityAnalyzer()
    scores = []
    for token in nltk.sent_tokenize(txt):
        scores.append(sia.polarity_scores(token).get("compound"))
    return mean(scores)

def headline_sentiment(txt: str) -> bool:
    return sentiment_value(clean_sentence(txt))
