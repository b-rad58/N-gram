open file
read into a string 
seperate into list by whitespace
create dictionary
add each gram (of size n)
while (string >= n) {
	dict += string[0-2]
	string = string[1-string.length()]
}
vectorSize = dictionary.size()
for (dictionary element)
	key = key/vectorSize


Sim(X, Y) = 1.0 - (Diff(X, Y)/2.0)

Diff(X,Y) is the sum over all possible n-grams of the absolute values of the differences in frequency of occurrence of each n-gram in textfiles X and Y.
