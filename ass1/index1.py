#########################################################
##  CS 4750 (Fall 2016), Assignment #1, Question #1    ##
##   Script File Name: tcomp1.py                       ##
##       Student Name: Bradley Gavan                   ##
##         Login Name: bmg610                          ##
##              MUN #: 201208634                       ##
#########################################################
#!/usr/bin/python3

import sys

#Reads the ignored word file, removing all non-alpha characters and organizing the words into a list
fin= open(sys.argv[1], 'r').read()
for char in fin:
   if not char.isalpha():
      if not char.isspace():
          fin = fin.replace(char, "")
ignoreList = fin.split()

#Reads the textfile, removing non-alpha characters and organizing the words into a list
fin= open(sys.argv[2], 'r').read()
for char in fin:
   if not char.isalpha():
      if not char.isspace():
          fin = fin.replace(char, "")
textList = fin.split()

#compares the words from the ignored file to the textfile
#the non-ignored words are put into a new list 'wordList'
#duplicates are removed from 'wordList' by converting it to a set and then back to a list
#a dictionary is created with a key for each non-ignored word
wordList = []
dictText = {}
for word in textList:
   if not word in ignoreList:
      wordList.append(word)
      dictText[word] = ""
wordList = list(set(wordList))

#the textfile is split into a list, seperated by new line characters
#non-alpha characters are removed
fin= fin.split('\n')
for line in fin:
   for char in line:
      if not char.isalpha():
            line = line.replace(char, "")

#the out file (index1.txt) is open and set to truncate
#the dictionary is updated, adding the line number to the value when the key is found on a line
fout = open(sys.argv[3], 'w')
for word in wordList:
   i=1
   for line in fin:
      if word in line:
         dictText[word] = dictText[word] + str(i) + " "         
      i+=1

#'finalList' is created and holds the words + line #s of each non-ignored word
#the list is sorted and written to the out file
finalList = []
for key in dictText:
   finalList.append("" + key + ": " + dictText[key] + "\n")
finalList.sort()
for line in finalList:
   fout.write(line)
   


sys.exit()
