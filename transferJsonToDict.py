# -*- coding: utf-8 -*-

import json, os

# def byteify(input):
#     if isinstance(input, dict):
#         return {byteify(key): byteify(value)
#                 for key, value in input.iteritems()}
#     elif isinstance(input, list):
#         return [byteify(element) for element in input]
#     elif isinstance(input, unicode):
#         return input.encode('utf-8')
#     else:
#         return input

def xmlToDict(filename):
    fullname = "boRecipe\\" + filename
    f = open(fullname)
    lines = f.readlines()
    f.close()
    allRecipeData = str()
    for line in lines:
        line.replace("\n", " ")
        allRecipeData += line
    #allRecipeDataDict = ast.literal_eval(allRecipeData)
    allRecipeDataDict = json.loads(allRecipeData)
    #allRecipeDataDict = byteify(allRecipeDataDict)
    f = open('boRecipeTII\\' + filename[:-4] + 'dic.txt', 'w')
    writein = allRecipeDataDict['Title']
    f.write(writein)
    f.write('\n')
    # print writein

    ingre = allRecipeDataDict['Ingredients']
    writein = ''
    for i in ingre:
        writein += i['Name']
        writein += ','
        writein += ' '

    # print writein
    f.write(writein.encode('utf-8', 'ignore'))
    f.write('\n')

    instr = allRecipeDataDict['Instructions']
    instr = instr.replace('\r\n', ' ')
    # instr.replace('\n', ' ')
    # print instr
    f.write(instr.encode('utf-8', 'ignore'))

    # for k in allRecipeDataDict:
        # if allRecipeDataDict[k] == None:
        #     value = 'NA'
        # else:
        #     value = str(allRecipeDataDict[k])
        #     value = value.replace('\n', '')
        # f.write(k + '\t' + value + '\n')
    f.close()
    ID = fnames[2:-4]
    #ID = line.split("\t")[1]
    f = open("boRecipeTII\\validID.txt", "a")
    f.write(ID)
    f.write('\n')
    f.close()
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

# print len(transferID), type(transferID)

for i in transferID[30000:]:
    fnames = 'Re' + str(i) + ".txt"
    xmlToDict(fnames)
