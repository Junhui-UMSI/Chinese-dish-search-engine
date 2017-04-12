# -*- coding: utf-8 -*-

from nltk import word_tokenize
import math, operator

f = open('uniquelist.txt')
uniqueWordList = []
lines = f.readlines()
for line in lines:
    line = line.rstrip()
    uniqueWordList.append(line)
f.close()

f = open('termFre.txt')
termFreqDic = {}
lines = f.readlines()
for line in lines:
    line = line.rstrip()
    diction = {}
    key = line.split(' ')[0]
    value = line.split(' ')[1]
    each = value.split(' ')
    for e in each:
        ID = e.split(',')[0]
        freq = e.split(',')[1]
        diction[ID] = freq
    termFreqDic[key] = diction
f.close()

f = open('lod.txt')
lod = {}
lines = f.readlines()
for line in lines:
    line = line.rstrip()
    ID = line.split(' ')[0]
    length = int(line.split(' ')[1])
    lod[ID] = length
f.close()

f = open('wordDocOccur.txt')
occurFile = {}
lines = f.readlines()
for line in lines:
    occurlist = []
    line = line.rstrip()
    word = line.split(' ')[0]
    occur = line.split(' ')[1]
    occurlist = occur.split(',')
    occurFile[word] = occurlist
f.close()

f = open('docFrequency.txt')
docFrequency = {}
lines = f.readlines()
for line in lines:
    line = line.rstrip()
    word = line.split(':')[0]
    try:
        docF = int(line.split(':')[1])
    except:
        docF = 0
    docFrequency[word] = docF

adl = 115.6
nod = 34741


def pivoted(query):
    query = word_tokenize(query)
    scoreDic = {}
    for word in query:
        if word in occurFile:
            ID = occurFile[word]
            for i in ID:
                score = 0
                termFreq = termFreqDic[word][i]
                docFreq = docFrequency[word]
                avgdl = adl
                docLength = lod[i]
                docNumber = nod
                idf = math.log((float(docNumber)+1)/docFreq)
                tf = (1+math.log(1+math.log(float(termFreq)))) / (1-0.5+0.5*docLength/avgdl)
                wordScore = tf * idf * termFreq
                score += wordScore
                if i in scoreDic:
                    scoreDic[i] += score
                else:
                    scoreDic[i] = score
        else:
            score = 0
    sortedScore = sorted(scoreDic.items(), key=operator.itemgetter(0), reverse=True)
    if len(sortedScore) > 10:
        firstTen = sortedScore.keys()[:10]
        return firstTen
    elif len(sortedScore) > 0:
        firstTen = sortedScore.keys()
        return firstTen
    else:
        return 'no relevant'

pivotedChickenDoc = pivoted('chicken')
print pivotedChickenDoc