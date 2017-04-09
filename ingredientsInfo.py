# -*- coding: utf-8 -*-

import json, os

def extractIngredients(filename):
    fullname = "boRecipe\\" + filename
    f = open(fullname)
    lines = f.readlines()
    f.close()
    allRecipeData = str()
    for line in lines:
        line.replace("\n", " ")
        allRecipeData += line
    #allRecipeDataDict = ast.literal_eval(allRecipeData)
    recipe = json.loads(allRecipeData)
    #allRecipeDataDict = byteify(allRecipeDataDict)

    ingredients = {}
    ingred = recipe['Ingredients']
    for i in ingred:
        ingredInfo = i['IngredientInfo']
        if ingredInfo == None:
            ingredInfo = i['Name']
        else:
            ingredInfo = ingredInfo['Name']
        if  ingredInfo in ingredients:
            ingredients[ingredInfo].append(i['Name'])
        else:
            ingredients[ingredInfo] = [i['Name']]
    return ingredients

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

masterIngredients = {}

for i in transferID[0:30]:
    fnames = 'Re' + str(i) + ".txt"
    eachIngredients = extractIngredients(fnames)
    for key in eachIngredients:
        if key in masterIngredients:
            for items in eachIngredients[key]:
                if items in masterIngredients[key]:
                    pass
                else:
                    masterIngredients[key].append(items)
        else:
            masterIngredients[key] = eachIngredients[key]


print len(masterIngredients), masterIngredients
