from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.apps import apps
from homepage.models import Comment
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import textblob
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os
from textblob.classifiers import NaiveBayesClassifier
from textblob.classifiers import DecisionTreeClassifier
from textblob import classifiers
import re

def textanalysis(request):
    return render(request, 'textanalysis/textanalysis.html')

def gettext(request):
    info = Comment.objects.values('Artist','Artwork_Title','Comment_Box').order_by('-id')[:10]
    for i in info:
        k = str(i)
        diction = eval(k)
        text = diction.get('Comment_Box')
        blob_ = TextBlob(text)
        blob = word_tokenize(text)
        stop_words= set(stopwords.words('english'))
        filtered_sent= []
        for w in blob:
            if w not in stop_words:
                filtered_sent.append(w)

        vader = SentimentIntensityAnalyzer()
        y = vader.polarity_scores(text)
        fdist = FreqDist(filtered_sent)
        if -1<= y['compound'] < -0.6:
            res = ('Negative')
        if -.6<= y['compound'] < -0.2:
            res = ('Somewhat Negative')
        if -0.2 <= y['compound'] < 0.2:
            res = ('Neutral')
        if 0.2 <= y['compound'] < .6:
            res = ('Somewhat Positive')
        if .6 <= y['compound'] <= 1.0:
            res = ('Positive')
        l = (fdist.most_common(5))


        return render(request, 'textanalysis/textanalysis.html', {'l': l, "res":res})