import nltk
from nltk.util import ngrams
from collections import Counter

sentence = "The quick brown fox jumps over the lazy dog"

tokens = nltk.word_tokenize(sentence)

n = 2

n_grams = ngrams(tokens,n)

n_grams_freq = Counter(n_grams)

def next_word_probability(ngram,n_gram_freq):
    ngram_list = list(ngram)
    ngram_count = n_gram_freq[ngram]
    preceding_word_count = n_grams_freq[tuple(ngram_list[:-1])]
    probability = ngram_count / preceding_words_count
    return probability

def generate_next_word(sentence,n_grams_freq,n):
    
    tokens = nltk.word_tokenize(sentence)
    
    prefix = tokens[-(n-1):]
    
    n_grams = ngrams(prefix, n-1)
    # calculate the probability of each possible next word
    probabilities = {word: next_word_probability(n_grams+(word,), n_grams_freq) for word in set(tokens)}
    # return the word with the highest probability
    return max(probabilities, key=probabilities.get)

# generate the next word in the sentence
next_word = generate_next_word(sentence, n_grams_freq, n)

# print the predicted next word
print("The predicted next word is:", next_word)
