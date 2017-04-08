# -*- coding: utf-8 -*-

import json, ast

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

def xmlToDict(filename):
    fullname = "boRecipe\\" + filename
    f = open(fullname)
    lines = f.readlines()
    f.close()
    allRecipeData = str()
    for line in lines:
        #line.strip("\n")
        allRecipeData += line
    #allRecipeDataDict = ast.literal_eval(allRecipeData)
    allRecipeDataDict = json.loads(allRecipeData)
    allRecipeDataDict = byteify(allRecipeDataDict)
    f = open('boRecipePYDic\\' + filename[:-4] + 'dic.txt', 'w')
    for k in allRecipeDataDict:
        if allRecipeDataDict[k] == None:
            value = 'NA'
        else:
            value = str(allRecipeDataDict[k])
            value = value.replace('\n', '')
        f.write(k + '\t' + value + '\n')
    f.close()
    f = open('boRecipePYDic\\' + filename[:-4] + 'dic.txt')
    line = f.readline().rstrip()
    ID = line.split("\t")[1]
    f = open("boRecipePYDic\\validID.txt", "a")
    f.write(str(ID) + '\n')
    return

def getFileID():
    totalID = []
    f = open('boRecipe\\validID.txt')
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        fID = line
        totalID.append(fID)
    return totalID

transferID = getFileID()
print len(transferID), type(transferID)

for i in transferID[1:30]:
    fnames = 'Re' + str(i) + ".txt"
    xmlToDict(fnames)

