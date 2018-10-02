"""Generate Markov text from text files."""

from random import choice
import random

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

    # your code goes here

    split_string = text_string.split()
    split_string.append(None)
    for i in range(len(split_string) - 2):
        key = (split_string[i], split_string[i + 1])
        value = split_string[i + 2]

        if key in chains:
            chains[key].append(value)
        else:
            chains[key] = [value]

    return chains

def make_text(chains):
    key = choice(chains.keys())
    # start with a random key from the dictionary of chains
    word_list = [key[0], key[1]]
    # inilize list of words to be added to
    word_value = choice(chains[key])
    # word value is a random word in the list of values for our chains key

    while word_value is not None:
        # keep going until you get a value of None, which is with Sam I am
        key = (key[1], word_value)
        # make the new key the second word in the original key and the random choice of a value from the list of values of the original key
        word_list.append(word_value)
        # reassign word value to be a new value in the new key's list of values so we keep it going
        word_value = choice(chains[key])

    return " ".join(word_list)



input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
# Produce random text
random_text = make_text(chains)

print(random_text)
