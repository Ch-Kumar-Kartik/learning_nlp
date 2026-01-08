import nltk
from nltk.probability import FreqDist
from nltk.corpus import stopwords # list of stopwords (common words to ignore) from NLTK's corpus module

stop_words = set(stopwords.words('english'))

"""
stopwords.words('english') uses the NLTK library to load a list of common English "stopwords" (words like "the", "is", "in", "and", etc., which are usually filtered out in text processing and NLP tasks because they carry little meaningful information)

It converts this list of stopwords into a Python set using set(...). Sets allow for much faster lookup (checking if a word is a stopword) compared to lists
"""

# read the corpus
with open('datasets/hamlet.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# tokenize the text into words (split the text (which contains the entire contents of .txt) into individual tokens, typically words and punctuation)
words = nltk.word_tokenize(text)

# Convert words to lowercase and filter to keep only alphabetic words
words = [word.lower() for word in words if word.isalpha()]

# Remove stopwords 
words = [word for word in words if word not in stop_words]

# Create a frequency distribution
fDist = FreqDist(words)

# 10 most common words and their counts
for x,v in fDist.most_common(10):
    print(x,v)

# 10 most common words and their relative frequencies
for x,v in fDist.most_common(10):
    print(x, v/len(fDist))
    
    
