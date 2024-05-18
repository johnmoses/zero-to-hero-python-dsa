"""
Tries
"""

class Node:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        """
        Initialize the data structure
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Insert a word
        """
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = Node(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the string
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def starts_with(self, prefix: str) -> bool:
        """
        Returns true if there is any word
        Starting with the given prefix
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
trie = Trie()
trie.insert('feeling')
trie.insert('comfort')
trie.insert('favour')

print(trie.starts_with('f'))