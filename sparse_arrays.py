class TrieNode:
    def __init__(self, key=''):
        """
        Each node in a Trie which holds information about the
        label (or key), its children, whether it is an endpoint
        and the number of times this particular word (if endpoint),
        occurs in the Trie.
        """
        self.key = key
        self.children = {}
        self.endpoint = False
        self.number = 0


class Trie:
    def __init__(self):
        """
        Constructor for the Trie class using the Trie nodes. 
        """
        self.head = TrieNode()

    def build_from_list(self, words):
        """
        Build a Trie using a list of words alloted.
        """
        for word in words:
            cur = self.head
            for id, letter in enumerate(word):
                if letter not in cur.children:
                    newTrie = TrieNode(letter)
                    cur.children[letter] = newTrie
                cur = cur.children[letter]
                if id == len(word) - 1:
                    cur.endpoint = True
                if cur.endpoint:
                    if id == len(word) - 1:  # last letter
                        cur.number += 1

    def find_num_occurences(self, word):
        """
        Given a word, find the number of occurences of the word in
        the Trie.
        """
        cur = self.head
        num = 0
        for letter in word:
            if letter not in cur.children:
                break
            else:
                cur = cur.children[letter]
        if cur.endpoint:
            num = cur.number
        return num


def sparse_array_trie(strings, queries):
    """
    There is a collection of input strings and a collection of query
    strings. For each query string, determine how many times it occurs
    in the list of input strings. Return an array of the results.

    The following is a solution that employs the Trie data structure. 

    A simpler solution using hash maps lies below.
    """
    trie = Trie()
    trie.build_from_list(strings)
    return [trie.find_num_occurences(query) for query in queries]


def sparse_array_hash(strings, queries):
    """
    The following is a simple approach based on hash maps. It solves the
    problem in O(n) time and space complexity. 
    """
    count = {}
    for string in strings:
        count[string] = count.get(string, 0) + 1
    return [count.get(query, 0) for query in queries]


if __name__ == '__main__':

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    print(sparse_array_hash(strings, queries))
    print(sparse_array_trie(strings, queries))
