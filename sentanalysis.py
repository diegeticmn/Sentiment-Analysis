from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


with open('YOURFILE.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

text = data

blob = TextBlob(text)

for sentence in blob.sentences:
    print(sentence.sentiment)
