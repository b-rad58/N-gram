#########################################################
##  CS 4750 (Fall 2016), Assignment #1, Question #1    ##
##   Script File Name: tcomp1.py                       ##
##       Student Name: Bradley Gavan                   ##
##         Login Name: bmg610                          ##
##              MUN #: 201208634                       ##
#########################################################
#!/usr/bin/python3

import sys

# a function to generate a dictionary of n-grams a given file 
def getNGrams(fin):
    i=0.0
    grams = fin.split()
    gramsDict = {}
    for g in grams:
        while len(g) >= n:
            i += 1
            gram = g[0:int(n)]
            if gramsDict.has_key(gram):
                gramsDict[gram] = gramsDict[gram]+1
            else:
                gramsDict[gram] = 1
            g = g[1:]
    if i != 0:
        for gram in gramsDict:
            gramsDict[gram] = float(gramsDict[gram]/i)	
    return gramsDict


n=int(sys.argv[2])
dictList = []

#open textfile X and create a dictionary of it's n-grams
fin= open(sys.argv[1], 'r').read()
dictList.append(getNGrams(fin))

#iterate through all the possible Y textfiles and creates their n-gram dictionaries
k=1
while k+2 < len(sys.argv):
    fin= open(sys.argv[k+2], 'r').read()
    dictList.append(getNGrams(fin))
    k += 1

#find the SimXY score for each textfile Y as well as keeps track of the highest SimXY score
j=1
mostSimilar = j+2
mostSimilarValue = 0
while j+2 < len(sys.argv):
    DiffXY=0
    for key in dictList[0]:
        if dictList[j].has_key(key):
            DiffXY += abs(dictList[0][key]-dictList[j][key])
        else:
            DiffXY += dictList[0][key]
    for key in dictList[j]:
        if not dictList[0].has_key(key):
            DiffXY += dictList[j][key]      
    SimXY = 1.0 - DiffXY/2.0
    if SimXY > mostSimilarValue:
        mostSimilarValue = SimXY
        mostSimilar = j+2
    j += 1
    print('Sim("' + sys.argv[1] + '","' + sys.argv[j+1] + '") = '+ '% .3f'% SimXY)  
print('File "' + sys.argv[mostSimilar] + '" is most similar to file "' + sys.argv[1] + '"')   


sys.exit()


