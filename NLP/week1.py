"""
Define a trigram language model with the following parameters:

q(the|*,*) = 1, q(dog|*,the) = 0.5
q(cat|*,the) = 0.5, q(walks|the,cat) = 1
q(STOP|cat, walks) = 1, q(runs|the,dog) = 1
q(STOP|dog, runs) = 1

Now consider a test corpus with the following sentences

    the dog runs STOP,  the cat walks STOP,  the dog runs STOP

What is the perplexity of the language model on this test corpus to three
decimal places?  (Note: use log_2 for your calculations.  Note that the
number of words in this corpus, M, is equal to 12)
"""
import math

def q(word, prev_word_2, prev_word_1):
    if word == "the":
        if prev_word_2 == "*" and prev_word_1 == "*":
            return 1.0
    elif word == "dog":
        if prev_word_2 == "*" and prev_word_1 == "the":
            return 0.5
    elif word == "cat":
        if prev_word_2 == "*" and prev_word_1 == "the":
            return 0.5
    elif word == "walks":
        if prev_word_2 == "the" and prev_word_1 == "cat":
            return 1.0
    elif word == "runs":
        if prev_word_2 == "the" and prev_word_1 == "dog":
            return 1.0
    elif word == "STOP":
        if prev_word_2 == "cat" and prev_word_1 == "walks":
            return 1.0
        elif prev_word_2 == "dog" and prev_word_1 == "runs":
            return 1.0
    else:
        return 0.0

def p(sentence):
    prob = 1.0
    words = ["*", "*"] + sentence.split() 
    for i in range(2, len(words)):
        prob *= q(words[i], words[i-2], words[i-1])
    return prob

def perplexity(sentences):
    M = 0
    sigma = 0
    for sentence in sentences:
        print "Testing sentence: ", sentence
        M += len(sentence.split())
        print "M = ", M
        sigma += math.log(p(sentence), 2)
        print "sigma = ", sigma
    return math.pow(2, -1*(sigma/M))

test_corpus = ["the dog runs STOP", "the cat walks STOP", "the dog runs STOP"]

print perplexity(test_corpus)
