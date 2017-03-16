# -*- coding: utf-8 -*- 

#api key: 6utU52O0vAhJZvKFXyw7us02mYMqF3cb
#example url: https://api2.bigoven.com/recipe/1?api_key=6utU52O0vAhJZvKFXyw7us02mYMqF3cb
import urllib2, json, ast


def bigOvenData(startNumber, endNumber):
    api_key = '6utU52O0vAhJZvKFXyw7us02mYMqF3cb'
    url = 'https://api2.bigoven.com/recipe/'
    idlist = range(100000)[startNumber:endNumber]
    for i in idlist:
        try:
            recipe_id = str(i)
            retrieved_url = url+recipe_id+"?api_key="+api_key
            print retrieved_url
            conn = urllib2.urlopen(retrieved_url, None)
            data = conn.read()
            #json_response = conn.read()
            #print json_response
            #yelp_data = json.loads(json_response)
            #print yelp_data
            file = "boRecipe\Re" + recipe_id + ".txt"
            f = open(file, "w")
            f.write(str(data))
            f.close()
            f = open("boRecipe\\validID.txt", "a")
            f.write(str(i)+"\n")
        except:
            print "the " + str(i) + "nd file does not exist"
    return

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

#add the ID ranges to use the bigOvenData e.g. bigOvenData(100, 200) download recipe of which id is in 100 - 200
bigOvenData(400, 600)
def xmlToDict(filename):
    fullname = "boRecipe\\" + filename
    f = open(fullname)
    lines = f.readlines()
    allRecipeData = str()
    for line in lines:
        #line.strip("\n")
        allRecipeData += line
    print len(allRecipeData)
    #allRecipeDataDict = ast.literal_eval(allRecipeData)
    allRecipeDataDict = json.loads(allRecipeData)
    allRecipeDataDict = byteify(allRecipeDataDict)
    return
    #print type(allRecipeDataDict), len(allRecipeDataDict), allRecipeDataDict['Ingredients']