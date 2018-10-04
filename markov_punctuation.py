"""Generate Markov text from text files."""

from random import choice
import random
import re

def open_and_read_file(file_path):
    """Take file path as string; return text as string.
    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    return open(file_path).read()


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.
    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.
    For example:
        >>> chains = make_chains("hi there mary hi there juanita")
    Each bigram (except the last) will be a key in chains:
        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]
    Each item in chains is a list of all possible following words:
        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    counter = 0
    # your code goes here
    key =[]
    text_list = re.findall(r"[\w']+|[.,!?;]", text_string)
    for word in text_list:
        key.append(word)
        if word == "." or word == "!" or word == "?":
            break
    key = " ".join(key)

    print(key)


            # counter += 1
    # print(chains)
    return chains



input_path = "green-eggs.txt"
n_grams = 4
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

chains = make_chains(input_text)

# new_chains = make_upper_keys(chains)
# Get a Markov chain
# Produce random text
# random_text = make_text(chains, n_grams)
# #
# print(random_text)
