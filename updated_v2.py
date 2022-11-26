#File: sentiment_mod.py

import nltk
import random
#from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize
import numpy as np



class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.predict(features)
            votes.append(v[0])
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.predict(features)
            votes.append(v[0])

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf


# documents_f = open("pickled_algos/documents.pickle", "rb")
# documents = pickle.load(documents_f)
# documents_f.close()

vec = open("updated_ver2_models/vectoriser.pickle", "rb")
vectoriser = pickle.load(vec)
vec.close()




word_features500k_f = open("pickled_algos/word_features5k.pickle", "rb")
word_features = pickle.load(word_features500k_f)
word_features500k_f.close()


def find_features(document):
    features = vectoriser.transform([document])

    return features



open_file = open("updated_ver2_models/BNB.pickle", "rb")
BNB = pickle.load(open_file)
open_file.close()


open_file = open("updated_ver2_models/LR.pickle", "rb")
LR = pickle.load(open_file)
open_file.close()



open_file = open("updated_ver2_models/SVC.pickle", "rb")
SVC = pickle.load(open_file)
open_file.close()




voted_classifier = VoteClassifier(LR, SVC, BNB)




def sentiment(text):
    feats = find_features(text)
    return voted_classifier.classify(feats),voted_classifier.confidence(feats)