# coding=utf-8
from iqap import IqapReader
import re
from NaiveBayes import NaiveBayes

"""
Program that uses the IQAP corpus and API written by Christopher Potts
and the NaiveBayes implementation from Stanford's CS 124 to detect deception
in indirect answers to yes/no questions.

Written by Stephanie Niu for LINGUIST 130a. 
"""
def featurize(q, a):
        features = []
        splitQ = q.split(" ")
        splitA = re.split(r'\s+|[,;.-]\s*', a)
    
        features.append(len(splitQ))
        features.append(len(splitA))
        features.append(splitA[0].lower())
        features.append(splitA[len(splitA) - 1].lower())
        features.append(q)
        features.append(a)

        return features

if __name__ == '__main__':
    corpus = IqapReader('iqap-data.csv')
    nb = NaiveBayes()
    for item in corpus.dev_set():
        features = item.featurize()

        nb.addExample(item.majority_label(), features)

    print nb.classify(featurize("Have you ever had any bank accounts in Swiss banks, Mr. Bronston?", \
        "The company had an account there for about six months, in Zurich."))

    print nb.classify(featurize("Do you like cheese?", "Yes."))
    print nb.classify(featurize("Do you like cheese?", "No."))

    print nb.classify(featurize("Is the president right to support the new legislation?", \
        "The president\'s wrong on that one."))

    print nb.classify(featurize("Did you see her?", "She was sick."))