import nltk
from nltk.stem.porter import PorterStemmer
import numpy as np

stemmer = PorterStemmer()
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w, in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0
    return bag


# Test to make sure everything is working
'''sentence = ['hello', 'how', 'are', 'you']
words = ['hi', 'hello', 'I', 'you', 'bye', 'thank', 'cool']
bog = bag_of_words(sentence, words)
print(bog)'''
'''bog = bag of words'''

################################### Extra Tutorial Info ##################################


'''words = ['Organize', 'organizes', 'organizing']
stemmed_words = [stem(w) for w in words]
print(stemmed_words)'''

#a = 'when is the new ehr update?'
#print(a)
#a = tokenize(a)
#print(a)
'''Output should be string and tokenized string'''