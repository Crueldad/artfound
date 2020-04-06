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
        tb = TextBlob(text)

        if tb.detect_language() == 'en':
            tb = text
        else:
            tb.translate(to='en')
            egv = tb.translate(to='en')
            translation = tb
            tb = text
            
        translation = tb
        evgg = str(egv)
        englishversion = evgg.replace("TextBlob", "")
        iftranslation = [englishversion] +["----English translation"]

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
        CI = k.replace("'", "").replace("{", "").replace("}", "").replace(","," ----").replace("Comment_Box", "Comment")
        most_common = (fdist.most_common(5)) + ["--Top 5 Common Words"]
        SentimentAnalysis = [res] + ["--Sentiment Analysis"]

    info = Comment.objects.values('Artist','Artwork_Title','Comment_Box').order_by('-id')[1:10]
    for i in info:
        k1 = str(i)
        diction = eval(k1)
        text1 = diction.get('Comment_Box')
        tb1 = TextBlob(text1)

        if tb1.detect_language() == 'en':
            tb1 = text1
        else:
            tb1.translate(to='en')
            egv1 = tb1.translate(to='en')
            translation1 = tb1
            tb1 = text1
            
        translation1 = tb1
        evgg1 = str(egv1)
        englishversion1 = evgg1.replace("TextBlob", "")
        iftranslation1 = [englishversion1] +["----English translation"]

        blob_1 = TextBlob(text1)
        blob1 = word_tokenize(text1)
        stop_words1 = set(stopwords.words('english'))
        filtered_sent1= []
        for w in blob1:
            if w not in stop_words1:
                filtered_sent1.append(w)

        vader1 = SentimentIntensityAnalyzer()
        y1 = vader1.polarity_scores(text)
        fdist1 = FreqDist(filtered_sent1)
        if -1<= y['compound'] < -0.6:
            res1 = ('Negative')
        if -.6<= y['compound'] < -0.2:
            res1 = ('Somewhat Negative')
        if -0.2 <= y['compound'] < 0.2:
            res1 = ('Neutral')
        if 0.2 <= y['compound'] < .6:
            res1 = ('Somewhat Positive')
        if .6 <= y['compound'] <= 1.0:
            res1 = ('Positive')
        CI1 = k1.replace("'", "").replace("{", "").replace("}", "").replace(","," ----").replace("Comment_Box", "Comment")
        most_common1 = (fdist1.most_common(5)) + ["--Top 5 Common Words"]
        SentimentAnalysis1 = [res1] + ["--Sentiment Analysis"]


        

        


        return render(request, 'textanalysis/textanalysis.html', {'most_common': most_common, "CI":CI, "SentimentAnalysis":SentimentAnalysis, "iftranslation":iftranslation,\
            'most_common1': most_common1, "CI1":CI1, "SentimentAnalysis1":SentimentAnalysis1, "iftranslation1":iftranslation1})