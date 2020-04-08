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
    info = Comment.objects.values('Comment_Box').order_by('-id')[:10]
    a = str(info)
    b = a.replace("<QuerySet", "").replace("]>","").replace("{","").replace("}","").replace("[","").replace(".","").replace("?","").replace("!", "").replace(":","").replace("'", "").replace(",", "")
    values = b.split('Comment_Box')

    info1 = Comment.objects.values('Artwork_Title').order_by('-id')[:10]
    p = str(info1)
    c = p.replace("<QuerySet", "").replace("]>","").replace("{","").replace("}","").replace("[","").replace(".","").replace("?","").replace("!", "").replace(":","").replace("'", "").replace(",", "")
    keys = c.split('Artwork_Title')

    res = {} 
    for key in keys: 
        for value in values: 
            res[key] = value 
            values.remove(value) 
            break    
    n = res
    return render(request, 'textanalysis/textanalysis.html', {'n':n})

            
    # for i in info:
    #     k = str(i)
    #     diction = eval(k)
    #     text = diction.get('Comment_Box')
    #     tb = TextBlob(text)

    #     if tb.detect_language() == 'en':
    #         tb = text
    #     else:
    #         tb.translate(to='en')
    #         egv = tb.translate(to='en')
    #         translation = tb
    #         text = tb
            
    #         translation = tb
    #         evgg = str(egv)
    #         englishversion = evgg.replace("TextBlob", "").replace(".", "").replace("!","").replace("?","")
    #         iftranslation = [englishversion] +["----English translation"]

    #         blob_ = TextBlob(englishversion)
    #         blob = word_tokenize(englishversion)
    #         stop_words= set(stopwords.words('english'))
    #         filtered_sent= []
    #         for w in blob:
    #             if w not in stop_words:
    #                 filtered_sent.append(w)

    #         vader = SentimentIntensityAnalyzer()
    #         y = vader.polarity_scores(englishversion)
    #         fdist = FreqDist(filtered_sent)
    #         if -1<= y['compound'] < -0.6:
    #             res = ('Negative')
    #         if -.6<= y['compound'] < -0.2:
    #             res = ('Somewhat Negative')
    #         if -0.2 <= y['compound'] < 0.2:
    #             res = ('Neutral')
    #         if 0.2 <= y['compound'] < .6:
    #             res = ('Somewhat Positive')
    #         if .6 <= y['compound'] <= 1.0:
    #             res = ('Positive')
    #         CI = k.replace("'", "").replace("{", "").replace("}", "").replace(","," ----").replace("Comment_Box", "Comment")
    #         most_common = (fdist.most_common(5)) + ["--Top 5 Common Words"]
    #         SentimentAnalysis = [res] + ["--Sentiment Analysis"]

            # return render(request, 'textanalysis/textanalysis.html', {'most_common': most_common, "CI":CI, "SentimentAnalysis":SentimentAnalysis, "iftranslation":iftranslation})
        

        # blob_ = TextBlob(text)
        # blob = word_tokenize(text)
        # stop_words= set(stopwords.words('english'))
        # filtered_sent= []
        # for w in blob:
        #     if w not in stop_words:
        #         filtered_sent.append(w)

        # vader = SentimentIntensityAnalyzer()
        # y = vader.polarity_scores(text)
        # fdist = FreqDist(filtered_sent)
        # if -1<= y['compound'] < -0.6:
        #     res = ('Negative')
        # if -.6<= y['compound'] < -0.2:
        #     res = ('Somewhat Negative')
        # if -0.2 <= y['compound'] < 0.2:
        #     res = ('Neutral')
        # if 0.2 <= y['compound'] < .6:
        #     res = ('Somewhat Positive')
        # if .6 <= y['compound'] <= 1.0:
        #     res = ('Positive')
        # CI = k.replace("'", "").replace("{", "").replace("}", "").replace(","," ----").replace("Comment_Box", "Comment")
        # most_common = (fdist.most_common(5)) + ["--Top 5 Common Words"]
        # SentimentAnalysis = [res] + ["--Sentiment Analysis"]
        
        # return render(request, 'textanalysis/textanalysis.html', {'most_common': most_common, "CI":CI, "SentimentAnalysis":SentimentAnalysis})