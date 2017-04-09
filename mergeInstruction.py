# -*- coding: utf=8 -*-



def getFileID():
    totalID = []
    f = open('boRecipeTII\\validID.txt')
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        fID = line
        totalID.append(fID)
    return totalID

def extractInstruction(fname):
    f = open(fname, 'r')
    lines=f.readlines()
    f.close()
    return lines[2]

transferID = getFileID()
mergeInstructions = ''
for i in transferID:
    mergeInstructions += extractInstruction("boRecipeTII\\Re" + i + "dic.txt")
    mergeInstructions += '\n'

f = open('masterInstructions.txt', 'w')
f.write(mergeInstructions)
f.close

