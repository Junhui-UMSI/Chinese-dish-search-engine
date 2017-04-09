# -*- coding: utf-8 -*-

import math
from nltk import word_tokenize
from stop_words import get_stop_words
from sklearn.feature_extraction.text import TfidfVectorizer

def getFileID():
    totalID = []
    f = open('boRecipeTII\\validID.txt')
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        fID = line
        totalID.append(fID)
    return totalID

stop_words = get_stop_words('en')
stop_words = [sw.encode('ascii') for sw in stop_words]

f = open('masterInstructions.txt')
all = ''
lines = f.readlines()

#number of documents
nod = len(lines)
print nod, "number of documents"

for line in lines:
    all += line

#allWordList contains all the tokens, word may exist in many times
allWordList = []
allWordList = word_tokenize(all)
for word in allWordList:
    if word in stop_words:
        allWordList.remove(word)
#average document length
adl = float(len(allWordList)) / nod
adl = float("{0:.2f}".format(adl))
print adl
#length of document
lod = {}

documentID = getFileID()
#for document Token: key is the document ID, value is the list of tokens for each doc
documentToken = {}
idx = 0
while idx < len(documentID):
    doc = lines[idx]
    ID = documentID[idx]
    docToken = word_tokenize(doc)
    for word in docToken:
        if word in stop_words:
            docToken.remove(word)
    word_number = len(docToken)
    documentToken[ID] = docToken
    lod[ID] = word_number
    idx += 1
print lod, len(lod)

#uniqueWordList: a list contain all unique word
uniqueWordList = []
for word in allWordList:
    if word in uniqueWordList:
        pass
    else:
        uniqueWordList.append(word)
wordDocOccur = {}
for word in uniqueWordList:
    for key in documentToken:
        if word in documentToken[key]:
            if word in wordDocOccur:
                wordDocOccur[word].append(key)
            else:
                wordDocOccur[word] = [key,]

#document frequency for each word, stored in a dictionary, if a document contains the word, the ID of the document is
# stored in
docFrequency = {}
for key in wordDocOccur:
    docFrequency[key] = len(wordDocOccur[key])
print len(docFrequency), docFrequency['chicken']

#term frequency for every word, key is word, value is a dictionary, which contains key as doc ID and value is term freq
# in each document
termFreqDic = {}
eachTermFreq = {}
for key in wordDocOccur:
    for ID in wordDocOccur[key]:
        doc = documentToken[ID]
        count = 0
        for word in doc:
            if word == key:
                count += 1
        eachTermFreq[ID] = count
    termFreqDic[key] = eachTermFreq
print len(termFreqDic), termFreqDic['chicken']

def pivoted(query, fileID):
    query = word_tokenize(query)
    fileID = str(fileID)
    score = 0
    for word in query:
        if word in uniqueWordList:
            termFreq = termFreqDic[word][fileID]
            docFreq = docFrequency[word]
            avgdl = adl
            docLength = lod[fileID]
            docNumber = nod
            idf = math.log((float(docNumber)+1)/docFreq)
            tf = (1+math.log(1+math.log(float(termFreq)))) / (1-0.5+0.5*docLength/avgdl)
            wordScore = tf * idf * termFreq
            score += wordScore
        else:
            score += 0
    return score

pivotedChickenDoc29 = pivoted('chicken', 29)
pivotedChickenDoc = pivoted('roasted chicken', 29)
print pivotedChickenDoc29, pivotedChickenDoc
