#########################################################
##  CS 4750 (Fall 2016), Assignment #1, Question #1    ##
##   Script File Name: tcomp1.py                       ##
##       Student Name: Bradley Gavan                   ##
##         Login Name: bmg610                          ##
##              MUN #: 201208634                       ##
#########################################################
#!/usr/bin/python3

import sys

#creates a list of unique words for each textfile.
#the lists are converted to sets and then back to lists
#sets cannot contain duplicates, which leaves us with only unique words
i=1
wordsList = []
while i < len(sys.argv):
    fin= open(sys.argv[i], 'r').read()
    wordsList.append(list(set(fin.split())))
    i+=1

#create a count of unique words for each textfile
lenList = []
for wordList in wordsList:
    lenList.append(len(wordList))

#iterate through each Y textfile, creating is SimXY score with the X textfile
#also keeps track of which Y textfile has the highest SimXy score
j=1
mostSimilar = j+1
simXY = 0.0
while j+1 < len(sys.argv):
    tempSimXY = 0.0
    uniqueWordCount = 0.0
    for word in wordsList[0]:
        if not word in wordsList[j]:
            uniqueWordCount += 1
    for word in wordsList[j]:
        if not word in wordsList[0]:
            uniqueWordCount += 1
    tempSimXY = 1.0 - (uniqueWordCount / (len(wordsList[0]) + len(wordsList[j])))
    if tempSimXY > simXY:
        simXY = tempSimXY
        mostSimilar = j+1
    print('Sim("' + sys.argv[1] + '","' + sys.argv[j+1] + '") = '+ '% .3f'% tempSimXY)
    j+=1
print('File "' + sys.argv[mostSimilar] + '" is most similar to file "' + sys.argv[1] + '"')   

sys.exit()
