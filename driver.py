
'                                               IMPORT NECESSARY LIBRARIES                                                                                       '
'-----------------------------------------------------------------------------------------------------------------------'

from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
from data_science import Sentiment_analysis,complex_words,analysis_of_readability,average_number_of_words_per_sentence,average_word_length,syllable_count,personal_pronouns,word_count

'                                           READ INPUT XLSX FILE USING PANDAS                                                                                        '
'-------------------------------------------------------------------------------------------------------------------------------------'
df=pd.read_csv("input.csv")

'                                 MAKE A DIRECTORY FOR STORING EXTRACTED TEXT FROM EACH WEBSITE                                                                     '
'-------------------------------------------------------------------------------------------------------------------------------------'

path = 'Data extraction'
if not os.path.exists(path):
    os.makedirs(path)

'                                               INITIALIZE VARIABLES                                                                                       '
'-------------------------------------------------------------------------------------------------------------------------------------'

Lines=[]
POSITIVE_SCORE=[]
NEGATIVE_SCORE=[]
POLARITY_SCORE=[]
SUBJECTIVITY_SCORE=[]
AVG_SENTENCE_LENGTH=[]
PERCENTAGE_OF_COMPLEX_WORDS=[]
FOG_INDEX=[]
c=[]
e=[]
f=[]
g=[]
h=[]
k=[]
S=''


'                                        FUNCTION TO EXTRACT TEXT FROM WEBPAGES                                                                                       '
'-------------------------------------------------------------------------------------------------------------------------------------'
def data_ex(s):
    for i in range(len(df)):
        r = requests.get(df['URL'][i]) 
        soup = BeautifulSoup(r.content, 'html5lib') 
        contents=soup.find_all(['p'])

        Lines=[]
        for j in range(16,len(contents)-3):
            co=contents[j].get_text()
            for pw in range(len(co)):
                if(co[pw].isalnum()==True or co[pw]==" "):
                    s+=co[pw]

            # \n is placed to indicate EOL (End of Line)  
            s+="\n"
            Lines.append(s)
            s=''
            
        #
        filename='{}.txt'.format(str(df['URL_ID'][i]))
        file1 = open(os.path.join(path, filename), "w")
        file1.writelines(Lines)
        file1.close() 

'                                               STORE PARAMETERS                                                                                       '
'-------------------------------------------------------------------------------------------------------------------------------------'
def ex_to_string():
    global POSITIVE_SCORE,NEGATIVE_SCORE,POLARITY_SCORE,SUBJECTIVITY_SCORE,AVG_SENTENCE_LENGTH,PERCENTAGE_OF_COMPLEX_WORDS,FOG_INDEX,c,e,f,g,h,k,S
    for i in range(len(df)):
        S=''
        r = requests.get(df['URL'][i]) 
        soup = BeautifulSoup(r.content, 'html5lib') 
        contents=soup.find_all(['p'])
        #print(i)

        # CHANGING THE PARAMETER 16,3 BELOW TO MANAGE NOT INCLUDING HEADER AND FOOTER 
        for j in range(16,len(contents)-3):
            co=contents[j].get_text()
            for p in range(len(co)):
                if(co[p].isalnum()==True or co[p]==" "):
                    S+=co[p]
                
            S+="\n"
            
        POSITIVE_SCORE.append(Sentiment_analysis(S)[0])
        NEGATIVE_SCORE.append(Sentiment_analysis(S)[1])
        POLARITY_SCORE.append(Sentiment_analysis(S)[2])
        SUBJECTIVITY_SCORE.append(Sentiment_analysis(S)[3])
        AVG_SENTENCE_LENGTH.append(analysis_of_readability(S)[0])
        PERCENTAGE_OF_COMPLEX_WORDS.append(analysis_of_readability(S)[1])
        FOG_INDEX.append(analysis_of_readability(S)[2])
        c.append(average_number_of_words_per_sentence(S))
        e.append(complex_words(S))
        f.append(word_count(S))
        g.append(syllable_count(S))
        h.append(personal_pronouns(S))
        k.append(average_word_length(S))
        #break

'                                               OUTPUT THE CSV FILE                                                                                       '
'-------------------------------------------------------------------------------------------------------------------------------------'
def export():
    global POSITIVE_SCORE,NEGATIVE_SCORE,POLARITY_SCORE,SUBJECTIVITY_SCORE,AVG_SENTENCE_LENGTH,PERCENTAGE_OF_COMPLEX_WORDS,FOG_INDEX,c,e,f,g,h,k
    data={
        'URL_ID':df['URL_ID'],
        'URL':df['URL'],
        'POSITIVE SCORE':POSITIVE_SCORE,
        'NEGATIVE SCORE':NEGATIVE_SCORE,
        'POLARITY SCORE':POLARITY_SCORE,
        'SUBJECTIVITY SCORE':SUBJECTIVITY_SCORE,
        'AVG SENTENCE LENGTH':AVG_SENTENCE_LENGTH,
        'PERCENTAGE OF COMPLEX WORDS':PERCENTAGE_OF_COMPLEX_WORDS,
        'FOG INDEX':FOG_INDEX,
        'AVG NUMBER OF WORDS PER SENTENCE':c,
        'COMPLEX WORD COUNT':e,
        'WORD COUNT':f,
        'SYLLABLE PER WORD':g,
        'PERSONAL PRONOUNS':h,
        'AVG WORD LENGTH':k,

        }
    DF=pd.DataFrame(data)
    DF.to_csv("output.csv")

if __name__=='__main__': 

    data_ex('')   
    ex_to_string()
    #print(PERCENTAGE_OF_COMPLEX_WORDS)
    export()
