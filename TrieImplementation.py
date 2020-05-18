# Implement a trie with insert, search, and startsWith methods.
#
# Example:
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true
#
# Note:
#     You may assume that all inputs are consist of lowercase letters a-z.
#     All inputs are guaranteed to be non-empty strings.
#
# from collections import defaultdict


# class Node:
#     def __init__(self, char):
#         self.char = char
#         self.children = []
#         self.last_char = False
#
#
# class Trie:
#     def __init__(self):
#         self.root = Node(None)
#
#     def insert(self, word):
#         curr = self.root
#         for i, char in enumerate(word):
#             child_node = self.get_child_node(curr, char)
#             if child_node:
#                 curr = child_node
#                 if i == len(word) - 1:
#                     curr.last_char = True
#             else:
#                 new_node = Node(char)
#                 if i == len(word) - 1:
#                     new_node.last_char = True
#                 curr.children.append(new_node)
#                 curr = new_node
#
#     def search(self, word):
#         curr = self.root
#         for i, char in enumerate(word):
#             child_node = self.get_child_node(curr, char)
#             if child_node is None:
#                 return False
#             curr = child_node
#             if i == len(word) - 1:
#                 return curr.last_char
#
#     def startsWith(self, prefix):
#         curr = self.root
#         for char in prefix:
#             child_node = self.get_child_node(curr, char)
#             if child_node is None:
#                 return False
#             curr = child_node
#         return True
#
#     @staticmethod
#     def get_child_node(curr, char):
#         for node in curr.children:
#             if char == node.char:
#                 return node
#         return None

class Trie:
    def __init__(self):
        self.d = {}

    def insert(self, word):
        node = self.d
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['$'] = True

    def search(self, word):
        node = self.d
        for c in word:
            if c in node:
                node = node[c]
            else:
                return False
        return '$' in node

    def startsWith(self, prefix):
        node = self.d
        for c in prefix:
            if c in node:
                node = node[c]
            else:
                return False
        return True


trie = Trie()
trie.insert('apple')
assert trie.search('apple') is True
assert trie.search('app') is False
assert trie.startsWith('app') is True
trie.insert('app')
assert trie.search('app') is True
