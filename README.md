# N-gram
CS4750 - Ass1

Question #1

An n-gram, n greater than or equal to 2, is a sequence of n non-whitespace characters. The n-gram frequency vwctor associated with a textfile is a vector NM indexed by the n-grams in the textfile such that the entry for n-gram x in this vector is the total number of occurrences of x in the textfile divided by the total number of n-grams in the textfile. For example, given the "ababa bba bb", the associated 2-gram frequency vector is
aa   0/7
ab   2/7
ba   3/7
bb   2/7
and the 3-gram frequency vector is
aaa  0/4
aab  0/4 
aba  2/4
abb  0/4
baa  0/4
bab  1/4
bba  1/4
bbb  0/4
Given two textfiles X and Y, let the similarity score between these textfiles be defined as 
Sim(X, Y) = 1.0 - (Diff(X, Y)/2.0), where Diff(X,Y) is the sum over all possible n-grams of the absolute values of the 
differences in frequency of occurrence of each n-gram in textfiles X and Y.

Write and document a Python script tcomp1.py which takes as command-line arguments a master textfile, a value of n, and two 
or more comparison textfiles and prints (1) the similarity of the master textfile and each comparison textfile and (2) the 
name of the comparison file that is most similar to the master textfile. Your script must work on datafiles nm1.dat, nm2.dat,
nm3.dat, nm4.dat, and nm5.dat to produce the output given in typescript-file tcomp1.script. Your code must implement the 
similarity computation using dictionaries to encode the non-zero entries in n-gram frequency matrices. You may assume that 
each given textfile has at least one word, i.e., no given textfile is composed entirely of whitespace characters.

Question #2

Given two textfiles X and Y, let the similarity score between these textfiles be defined as 
Sim(X, Y) = 1.0 - (SD(X, Y) / (nW(X) + nW(Y))), where nW(X) and nW(Y) are the numbers of words that occur in X and Y and
SD(X, Y) is the total number of words that occur uniquely in X or Y, i.e., (the number of words that occur in X that do not 
occur in Y) + (the number of words that occur in Y that do not occur in X). Note that nW() does not count the total number of words in a file, but rather the number of different words that occur in a file.
Write and document a Python script tcomp2.py which takes as command-line arguments a master textfile and two or more 
comparison textfiles and prints (1) the similarity of the master textfile and each comparison textfile and (2) the name 
of the comparison file that is most similar to the master textfile. Your script must work on datafiles tc1.dat, tc2.dat,
tc3.dat, tc4.dat, tc5.dat, and tc6.dat to produce the output given in typescript-file tcomp2.script. Your code must 
implement the similarity computation using sets.

Question #3

Write and document a Python script index1.py which takes as command-line arguments the names of an ignored-word file 
(one word per line), a text-file, and an index-file, and computes and outputs to the index-file a sorted index describing 
the lines on which each word in the text-file that is not in the ignored-word file occurs in the text-file. You may assume
that the only non-word characters in a text-file are apostrophes, quotation marks (single and double), parentheses,
exclamation marks, question marks, colons, semi-colons, commas, and periods. Your script must work on word-file word1.txt
and text-file text1.txt to produce index-file index1.txt as specified in typescript-file index1.script. You may assume that
all given files are formatted correctly.
