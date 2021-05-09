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


class Node:
    def __init__(self, char):
        self.val = char
        self.children = {}
        self.end = False

    def __repr__(self):
        return f'Node({self.val} : {self.children.keys()})'


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node(c)
            curr = curr.children[c]
        curr.end = True

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end

    def starts_with(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

    def words_with_prefix(self, prefix):
        def dfs(curr, s):
            if curr.end:
                result.append(prefix + s)
            for child in curr.children:
                dfs(curr.children[child], s + child)

        result = []
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return []
            curr = curr.children[c]

        dfs(curr, '')
        return result


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

# class Trie:
#     def __init__(self):
#         self.trie = {}
#
#     def insert(self, word):
#         node = self.trie
#         for c in word:
#             if c not in node:
#                 node[c] = {}
#             node = node[c]
#         node['$'] = True
#
#     def search(self, word):
#         node = self.trie
#         for c in word:
#             if c in node:
#                 node = node[c]
#             else:
#                 return False
#         return '$' in node
#
#     def startsWith(self, prefix):
#         node = self.trie
#         for c in prefix:
#             if c in node:
#                 node = node[c]
#             else:
#                 return False
#         return True


trie = Trie()

# trie.insert('apple')
# trie.insert('appear')
# trie.insert('appearance')
# trie.insert('app')
# trie.insert('approach')
# trie.insert('applet')
# trie.insert('apprehend')
# assert trie.search('apple') is True
# assert trie.starts_with('app') is True
# assert trie.search('app') is True
#
# print(trie.words_with_prefix('app'))

trie.insert('a')
trie.insert('aa')
trie.insert('aaa')

assert trie.search('a') is True
assert trie.search('aa') is True
assert trie.search('aaa') is True
assert trie.search('aaaa') is False

assert trie.starts_with('a') is True
assert trie.starts_with('aa') is True
assert trie.starts_with('aaa') is True
assert trie.starts_with('aaaa') is False

print(trie.words_with_prefix('a'))

# ["Trie","insert",  "search", "search",  "search", "startsWith","startsWith","startsWith"]
# [[],    ["hello"], ["hell"], ["helloa"],["hello"],["hell"],     ["helloa"],  ["hello"]]
# trie.insert('hello')
# print(trie.search('hell'))
# print(trie.search('helloa'))
# print(trie.search('hello'))
# print(trie.starts_with('hell'))
# print(trie.starts_with('hello'))

# trie.insert('apple')
# trie.insert('app')
# print(trie.search('app'))
# ["Trie", "insert",  "search",  "search", "startsWith", "insert", "search"]
# [[],     ["apple"], ["apple"], ["app"] , ["app"],      ["app"] , ["app"]]
