#word frequency 
file = open('tst.txt','r')
book = file.read()

def tokenize():
	if book is not None:
		words = book.lower().split()
		return words
	else:
		return None

def map_book(tokens):
	hash_map = {}

	if tokens is not None:
		for elements in tokens:
			#remove punctutation
			word = elements.replace(",","")
			word = word.replace(".","")

			if word in hash_map:
				hash_map[word]=hash_map[word]+1
			else:
				hash_map[word]=1

		return hash_map
	else:
		return None

words= tokenize(book)

map= map_book(words)

for word in map:
	print('Word: [' + word + '] Frequency: ' + str(map[word]))


