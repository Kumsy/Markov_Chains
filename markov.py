"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    # Opening the file and reading the entire file
    file = open(file_path).read()


    return file


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
    # initiating a dictionary
    chains = {}
    # calling to open the file and storing the whole string in a variable
    my_text = open_and_read_file("green-eggs.txt")
    #splitting the string into a list of each word
    words = my_text.split()
    # print(words)
    # your code goes here

    # my_tuple = (,)
    #looping through the whole list of words in the text
    for i in range(len(words) - 2):
        #make each pair of words into a tuple
        my_tuple = (words[i], words[i + 1]) 
        #gets value of key if key is in chains or makes it an empty list
        my_list = chains.get(my_tuple, [])
        #sets my_tuple into dictionary with value defined above
        chains[my_tuple] = my_list
        #to make list of words that follow this tuple, append words[i+2]
        my_list += [words[i + 2]]
        # dict(my_tuple)
    # print(f'TUPLES{my_tuple}')
    # print("{" + "\n".join(f'{k}: {v}' for k, v in chains.items())  + "}")

    return chains

def make_text(chains):
    """Return text from chains."""

    words = []
    
    # for key, value in chains.items():
    #     words.append(choice(key))

    rand_key = choice(list(chains.keys()))

    # Puts random key in the word list
    words.extend(rand_key)

    # Gets a random choice value from the random key's list
    words.append(choice(chains[rand_key]))
    

    # this loops through the dictionary for as long as the length of the dictionary
    while True:
        try:
            # we turn the last two elements of our words list back into a tuple so we can look it up
            new_key = tuple(words[-2:])
            #we are indexing into the dict using the tuple we just made
            #choosing a random member of the list that follows that key
            #adding that random member to our words list
            words.append(choice(chains[new_key]))
        except:
            break
    # return words
    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
# print(input_text)

# Get a Markov chain
chains = make_chains(input_text)

# # Produce random text
random_text = make_text(chains)
print(random_text)

# print(random_text)
