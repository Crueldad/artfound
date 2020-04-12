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
import json 


def parse_query(updated_querystring):
    char_index = 0
    main_dict = {}

    updated_querystring = updated_querystring.replace("<QuerySet [","")
    updated_querystring = str(updated_querystring[0:-2])

    print ("String to convert to Dictionary: ",updated_querystring)

    while len(updated_querystring) > 3:

        if updated_querystring[char_index] == "{":
            # print ("should start a dictionary")
            key_string = ""
            value_string = ""
            char_index += 19
            # print (" updated_querystring[char_index] : ",  updated_querystring[char_index])

            # Get Key Name
            while updated_querystring[char_index] != "'":
                key_string += updated_querystring[char_index]
                char_index += 1
            
            # Jump to Value
            char_index += 19
            # print ("New first letter: ",  updated_querystring[char_index] )

            # Get Value
            while updated_querystring[char_index] != "'":
                value_string += updated_querystring[char_index]
                char_index += 1

            # print ("Key String: ",key_string)
            # print ("Value String: ",value_string)
            
            # Convert from string to list
            value_list = [value_string]

            if key_string in main_dict:
               list_of_comments = main_dict[key_string]
               list_of_comments.append (value_string)
            else:
                main_dict[key_string] = value_list

        # Remove Key and Value from string before starting loop again
        updated_querystring = updated_querystring[char_index+4:]

        # print ("Updated after addinging to dict:  ", updated_querystring)
        char_index = 0

    return main_dict
def textanalysis(request):
    return render(request, 'textanalysis/textanalysis.html')

def gettext(request):
    
    info = Comment.objects.values('Artwork_Title','Comment_Box').order_by('-id')[:10]
    f = str(type(info))
    first_value =  Comment.objects.all()[:1].get()

    returned_query_string = str(info)
    parsed_dictionary = parse_query(returned_query_string)


    
    for x in parsed_dictionary:
        if x == 'FISHES SWIMMING':
            FSV = parsed_dictionary['FISHES SWIMMING']
            vader = SentimentIntensityAnalyzer()
            F = sum([vader.polarity_scores(sentence)['compound'] for sentence in FSV])/len([vader.polarity_scores(sentence)['compound'] for sentence in FSV])
            y = F
        if x == 'NAUTICAL WONDER':
            FSV1 = parsed_dictionary['NAUTICAL WONDER']
            vader = SentimentIntensityAnalyzer()
            N = sum([vader.polarity_scores(sentence)['compound'] for sentence in FSV1])/len([vader.polarity_scores(sentence)['compound'] for sentence in FSV1])
            y = N
        if x == 'DESERT BIRD':
            FSV2 = parsed_dictionary['DESERT BIRD']
            vader = SentimentIntensityAnalyzer()
            D = sum([vader.polarity_scores(sentence)['compound'] for sentence in FSV2])/len([vader.polarity_scores(sentence)['compound'] for sentence in FSV2])
            y = D

    if -1<= y < -0.6:
        sentiment = ('Overall sentiment is Negative')
    if -.6<= y < -0.2:
        sentiment = ('Overall sentiment is Somewhat Negative')
    if -0.2 <= y < 0.2:
        sentiment = ('Overall sentiment is Neutral')
    if 0.2 <= y < .6: 
        sentiment = ('Overall sentiment is Somewhat Positive')
    if .6 <= y <= 1.0:
        sentiment =('Overall sentiment is Positive')

    if F > N and F > D:
        Best_Comment = ('The artwork with the best comments is: Fishes Swimming')
        common = parsed_dictionary['FISHES SWIMMING']
    if N > F and N > D:
        Best_Comment = ('The artwork with the best comments is: Nautical Wonder')
        common = parsed_dictionary['NAUTICAL WONDER']
    if D > N and D > F:
        Best_Comment = ('The artwork with the best comments is: Desert Bird')
        common = parsed_dictionary['DESERT BIRD']

    K = ''   
    for word in common:
        K = K + ' ' + word
    kp = K.replace("TextBlob", "").replace(".", "").replace("!","").replace("?","")
    K = word_tokenize(kp)
    filtered_sent= []
    stop_words= set(stopwords.words('english'))
    for w in K:
        if w not in stop_words:
            filtered_sent.append(w)
    #print(filtered_sent)
    fdist = FreqDist(filtered_sent)
    # print(len(filtered_sent))
    x = (.10*len(filtered_sent))
    if x < 1:
        x = 1
    else:
        x = int(x)
    most_common_w = 'These are the common words from all comments under the choosen artwork:', (fdist.most_common(x)) 
        
    return render(request, 'textanalysis/textanalysis.html', {'parsed_dictionary':parsed_dictionary, 'Best_Comment':Best_Comment, 'sentiment':sentiment,\
        'most_common_w':most_common_w})
    
   

    


        
        # CI = k.replace("'", "").replace("{", "").replace("}", "").replace(","," ----").replace("Comment_Box", "Comment")
        # most_common = (fdist.most_common(5)) + ["--Top 5 Common Words"]
        # SentimentAnalysis = [ress] + ["--Sentiment Analysis"]

        
            

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

        # return render(request, 'textanalysis/textanalysis.html', {'CI':CI, 'most_common':most_common, 'SentimentAnalysis':SentimentAnalysis })

            
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