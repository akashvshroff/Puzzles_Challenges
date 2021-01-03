class TrieNode:
    def __init__(self, key=''):
        """
        Each node in a Trie which holds information about the
        label (or key), its children, whether it is an endpoint
        and the number of times this particular word (if endpoint),
        occurs in the Trie.
        """
        self.key = key
        self.children = []
        self.endpoint = False
        self.number = 0


class Trie:
    def __init__(self):
        """
        Constructor for the Trie class using the Trie nodes. 
        """
        pass

    def build_from_list(self, words):
        """
        Build a Trie using a list of words alloted.
        """
        pass

    def find_num_occurences(self, word):
        """
        Given a word, find the number of occurences of the word in
        the Trie.
        """
        pass


def spare_array_trie(strings, queries):
    """
    There is a collection of input strings and a collection of query
    strings. For each query string, determine how many times it occurs
    in the list of input strings. Return an array of the results.

    The following is a solution that employs the Trie data structure. 

    A simpler solution using hash maps lies below.
    """
    pass


def sparse_array_hash(strings, queries):
    """
    The following is a simple approach based on hash maps. It solves the
    problem in O(n) time and space complexity. 
    """
    count = {}
    for string in strings:
        count[string] = count.get(string, 0) + 1
    return [count.get(query, 0) for query in queries]
