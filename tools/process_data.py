# coding=utf-8
import nltk
from nltk import word_tokenize
from nltk.tag import pos_tag, map_tag

def process_review(review):
    tokens = nltk.word_tokenize(review)
    posTagged = pos_tag(tokens)
    simplifiedTags = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in posTagged]
    simplifiedTags = [i for i in simplifiedTags if i[1] != 'ADP' and i[1] != 'DET']

    return simplifiedTags

def get_phrases(simplifiedTags):
    len_list=len(simplifiedTags)
    key_phrase=[]
    num=0
    while num<len_list:
        tag=simplifiedTags[num][1]
        word=simplifiedTags[num][0]
        if(num+1<len_list):
            tag_next=simplifiedTags[num+1][1]
            word_next=simplifiedTags[num+1][0]
        else:
            tag_next=''
            word_next=''
        if(num+2<len_list):
            tag_third=simplifiedTags[num+2][1]
            word_third=simplifiedTags[num+2][0]
        else:
            tag_third=''
            word_third=''
        if(tag=='ADV'):
            if(tag_next=='ADJ'):
                if(tag_third=='NOUN'):
                    key_phrase.append(' '.join([word, word_next, word_third]))
                    num+=3
                    continue
            elif(tag_next=='VERB'):
                if(tag_third=='NOUN'):
                    key_phrase.append(' '.join([word, word_next, word_third]))
                    num+=3
                    continue
        elif(tag=='ADJ'):
            if(tag_next=='NOUN'):
                key_phrase.append(' '.join([word, word_next]))
                num+=2
                continue
        num+=1

    return key_phrase