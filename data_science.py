
'                                               IMPORT NECESSARY LIBRARIES                                                                                       '
'-----------------------------------------------------------------------------------------------------------------------'

import os
from collections import defaultdict
from nltk.tokenize import word_tokenize
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textstat.textstat import textstatistics
from nltk.stem import WordNetLemmatizer


'                                               INITIALIZE VARIABLES                                                                                       '
'-------------------------------------------------------------------------------------------------------------------------------------'

d=defaultdict(list)
stop_words=set()

def tok(s):
    #STEP 1=Cleaning using Stop Words Lists

    files = [f for f in os.listdir("StopWords")]

    #print(files)
    for i in range(len(files)):
        l='StopWords\\{}'.format(files[i])
        with open(l,"r") as f:
            x=f.read().split("\n")
            for j in range(len(x)):
                stop_words.add(x[j].lower())
    f.close()

    x=s.split(" ")
    ans=''
    for i in range(len(x)):
        if(x[i] not in stop_words):
            ans+=x[i]+' '
    tokens = word_tokenize(ans.lower())
    return tokens

def complex_words(s):
    tokens = tok(s)
    complex_cnt = 0
    for token in tokens:
        vowels = 0
        if token.endswith(('es','ed')):
            pass
        else:
            for l in token:
                if (l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u'):
                    vowels += 1
            if vowels > 2:
                complex_cnt += 1
    return complex_cnt

def Sentiment_analysis(s):

    #STEP 1=Cleaning using Stop Words Lists
    d.clear()
    files = [f for f in os.listdir("StopWords")]

    #print(files)
    for i in range(len(files)):
        l='StopWords\\{}'.format(files[i])
        with open(l,"r") as f:
            x=f.read().split("\n")
            for j in range(len(x)):
                stop_words.add(x[j].lower())
    f.close()

    x=s.split(" ")
    ans=''
    for i in range(len(x)):
        if(x[i] not in stop_words):
            ans+=x[i]+' '

    #STEP 2=Creating a dictionary of Positive and Negative words


    files1 = [f for f in os.listdir("MasterDictionary")]
    pos=[]
    neg=[]
    for i in range(len(files1)):
        l='MasterDictionary\\{}'.format(files1[i])
        with open(l,"r") as f:
            x=f.read().split("\n")
            for j in range(len(x)):
                if(i==0):
                    neg.append(x[j].lower())
                else:
                    pos.append(x[j].lower())
    
    f.close()

    y=s.split("\n")
    for i in range(len(y)):
        z=y[i].split(" ")
        for j in range(len(z)):
            if(z[j]!=''):
                if(z[j] in pos):
                    d['pos'].append(z[j])
                elif(z[j] in neg):
                    d['neg'].append(z[j])
    
    #STEP 3=Extracting Derived variables

    tokens = word_tokenize(ans.lower())
    positive_score=len(d['pos'])
    negetive_score=len(d['neg'])
    polarity_score=(positive_score-negetive_score)/((positive_score+negetive_score)+0.000001)
    subjectivity_score=(positive_score+negetive_score)/(len(ans)+0.000001)
    return [positive_score,negetive_score,polarity_score,subjectivity_score]




def analysis_of_readability(s):
    y=s.split("\n")
    c1=0
    for i in range(len(y)):
        for j in range(len(y[i])):
            if(y[i][j]!=" "):
                c1+=1
    
    average_sentence_length=len(y)/c1
    percentage_of_complex_words=complex_words(s)/len(s)
    fog_index=0.4*(average_sentence_length+percentage_of_complex_words)
    return [average_sentence_length,percentage_of_complex_words,fog_index]

def average_number_of_words_per_sentence(s):
    y=s.split("\n")
    c2=0
    
    for i in range(len(y)):
        for j in range(len(y[i])):
            if(y[i][j]!=" "):
                c2+=1
    return len(y)/c2


def word_count(text):
    x = re.sub("[?_/,.<>!@#$%^&*()]","",text)
    tokens = word_tokenize(x.lower())
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    return(len(lemmatized_tokens))


def syllable_count(s):
    return textstatistics().syllable_count(s)


def personal_pronouns(s):
    regexPattern1 = [r"\bWe\b",r"\bwe\b",r"\bI\b",r"\bi\b"r"\bmy\b",r"\bMy\b",r"\bours\b",r"\bOurs\b",r"\bus\b",r"\bUs\b"]
    c4=0
    for p in range(len(regexPattern1)):
        x=regexPattern1[p]
        for m in re.findall(x, s):
            c4+=1
    return c4


def average_word_length(s)-> int:
    y=s.split()
    words=len(y)
    c3=0
    for i in range(len(y)):
        c3+=len(y[i])

    ans=c3/words
    return ans
#print(average_word_length(s))


#print(syllable_count(s))

#print(personal_pronouns(s))
