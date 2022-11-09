"""Generate Markov text from text files."""

#First, you’ll create a Python script to procedurally generate original 
#content based on an excerpt from Green Eggs and Ham by Dr. Seuss. Then, 
#you’ll enhance your script so that it works on any corpus (any existing piece of text) 
#and even combinations of corpuses.

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    #open input text file
    contents = open('green-eggs.txt').read()

    #return the contents
    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """


    #break up input text
        #add rstrip is spacing is weird
    words = text_string.split()

    #initialize empty dictionary
    chains = {}

    #create for loop to parse through input text to find words & -1 to keep in a parameter
    for word in range(len(words) - 2):

        #turn words into the dictionary structure
        chains_key = (words[word], words[word + 1])
        #print(chains_key)

        #assign variable to list
        chains_value = words[word + 2]
        #print(chains_value)

        #create condition in the event that the word isn't the dictionary
        if chains_key not in chains:
            chains[chains_key] = []

        #add the chain value to the chain key
        chains[chains_key].append(chains_value)

    #print(chains)

    #return
    return chains




def make_text(chains):
    """Return text from chains."""

    #initialize empty words list to return words into
    words = []

    #use random’s choice function to pick a random key from chains.keys() 
    #and use the list() constructor to convert it into a list
    chosen_words = choice(list(chains.keys()))  
    chosen_keys = [chosen_words[0], chosen_words[1]]
    
    #create a for loop to parse through chains 
    #parse through our 2 chosen keys? 
    #remmeber list must go inside function not outside:
    #chosen_word[1] = list(choice(words.keys()))


    print(chosen_keys)
    # print(chosen_word[1])


    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
