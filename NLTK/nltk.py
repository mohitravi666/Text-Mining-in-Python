"""
@author: Ted

The script includes the following pre-processing steps for text:
- Sentence Splitting
- Term Tokenization
- Ngrams
- POS tagging
"""

import nltk.data
from nltk.util import ngrams
import re
from nltk.tokenize import sent_tokenize
from nltk import load
_POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
tagger = load(_POS_TAGGER)
#read the input
f=open('article.txt')
text=f.read().strip().lower()
f.close()


#split sentences
sentences=sent_tokenize(text)
print 'NUMBER OF SENTENCES: '+ str(len(sentences))

all2grams=set()

# for each sentence
for sentence in sentences:
    
    adjectives=set()#adjectives in this sentence
    adverbs=set()#adverbs in this sentences
    
    sentence=re.sub('[^a-z\d]',' ',sentence)#replace chars that are not letters or numbers with a space
    sentence=re.sub(' +',' ',sentence).strip()#remove duplicate spaces

    #tokenize the sentence
    terms = nltk.word_tokenize(sentence.lower())   
    
    tagged_terms=tagger.tag(terms)#do POS tagging on the tokenized sentence
    
    for pair in tagged_terms: 
        
        #if the word is an adjective
        if pair[1].startswith('JJ'): adjectives.add(pair[0])
        
        #if the word is an adverb
        elif pair[1].startswith('RB'): adverbs.add(pair[0]) 
           
    twograms = ngrams(terms,2) #compute 2-grams
    
    #for each 2gram
    for tg in twograms:  
        if tg[0] in adverbs  and tg[1] in adjectives: # if the 2gram is a an adverb followed by an adjective
            print tg
    
