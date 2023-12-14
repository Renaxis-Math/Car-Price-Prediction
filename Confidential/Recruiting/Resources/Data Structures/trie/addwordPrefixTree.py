from functools import lru_cache

class Node:
    def __init__(self):
        self.isEndOfWord = False
        self.children = [None] * 26 # index i'th represents i'th letter

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curr = self.root
        
        for letter in word:
            index = ord(letter) - ord('a')
            
            if not curr.children[index]:
                curr.children[index] = Node()
                
            curr = curr.children[index]
            
        curr.isEndOfWord = True
    
    def printTrie(self, curr, word):
        for index, child in enumerate(curr.children):
            if child:
                letter = chr(index + ord('a'))
                self.printTrie(child, word + letter)

        if curr.isEndOfWord:
            print(word)
            
    def isPrefix_helper(self, prefix):
        curr = self.root
        for letter in prefix:
            index = ord(letter) - ord('a')
            
            if not curr.children[index]:
                return None
            
            curr = curr.children[index]
        return curr
    
    def isPrefix(self, word):
        node = self.isPrefix_helper(word)
        return not(node is None)
    
    def contains(self, word):
        node = self.isPrefix_helper(word)
        if not node or not node.isEndOfWord:
            return False
        return True

    def jumpsTo(self, prefix):
        if not self.isPrefix(prefix):
            return None
        
        curr = self.root
        
        for letter in prefix:
            index = ord(letter) - ord('a')
            curr = curr.children[index]
            
        return curr
            
            
# Given a vocabulary and a starting prefix, 
# the two take turns adding letters to a prefix. 
# The new prefix is ​still in the vocabulary, 
# and whoever makes up a complete word first LOSES / NOT WINS.

# def hrt2(dictionary):
#     """
#     Game Theory Min-Max Strategy:
    
#     To have the best outcome (win the game) of the current player, 
#     check all possible actions of the other players 
#     and determine the worst action (leading to a lost) for the other player.
#     """
#     t = Trie()
#     for word in dictionary:
#         t.insert(word)
            
#     def solve(root, other_roots):
#         children = root.children
        
#         for i in range(len(children)):
#             child = children[i]

#             if child and not child.isEndOfWord:
#                 children[i] = None
                
#                 res = solve(child, children)
#                 if not res:
#                     return True
                
#                 children[i] = child
                
#         for other_root in other_roots:
#             if other_root and not other_root.isEndOfWord:
#                 res = solve(other_root, [])
                
#                 if not res:
#                     return True
                  
#         return False
    
#     return solve(t.root, [])

nextPlayerDict = {}
nextPlayerDict["1"] = "2"
nextPlayerDict["2"] = "1"

def canCurPlayerWin(root, solved):
    if root in solved:
        return solved[root]
    # Because the new prefix is ​still in the vocabulary,
    # options are limited to a root's children.
    options = root.children
    
    for option in options:
        if option != None and (not option.isEndOfWord):
            
            nextPlayerMove = canCurPlayerWin(option, solved)
            if not nextPlayerMove:
                solved[root] = True
                return True
    
    solved[root] = False
    return False

def hrt(dictionary, prefix, nextPlayerDict, curPlayer):
    t = Trie()
    for word in dictionary:
        t.insert(word)
        
    curRoot = t.jumpsTo(prefix)
    if curRoot != None:
    
        if canCurPlayerWin(curRoot, {}):
            return curPlayer
        return nextPlayerDict[curPlayer]
    
    return curPlayer

def hrt_dp(dictionary, cur_player):
    
    def get_options(i, cur_prefix):
        options = set()
        for word in dictionary:
            if word[:i] == cur_prefix and i < len(word)-1:
                options.add(word[i])
                
        return options

    memo = {}
    def can_cur_player_win(i, cur_prefix):

        if cur_prefix in set(dictionary):
            memo[(i, cur_prefix)] = True
            return True
    
        if (i, cur_prefix) in memo:
            return memo[(i, cur_prefix)]
        
        options = get_options(i, cur_prefix)
        for option in options:
            res = can_cur_player_win(i+1, cur_prefix + option)
            if not res:
                memo[(i, cur_prefix)] = True
                return True

        memo[(i, cur_prefix)] = False
        return False
    
    if can_cur_player_win(0, ""):
        return cur_player
    return nextPlayerDict[cur_player]

# d1 = ["a"]
# assert hrt(d1, "") == False

# d2 = ["ab"]
# assert hrt(d2, "") == True
# assert hrt(d2, "a") == False

# d3 = ["abcd", "abede", "acd"]
# assert hrt(d3, "") == False
# assert hrt(d3, "ab") == True

# d4 = ["ab", "abc", "dab", "dacd"]
# assert hrt(d4, "") == True
# assert hrt(d4, "ab") == False
# assert hrt(d4, "da") == True

d1 = ["a"]
assert hrt(d1, "", nextPlayerDict, "1") == "2" 
assert hrt(d1, "b", nextPlayerDict, "1") == "1"

assert hrt_dp(d1, "1") == "2"

d2 = ["ab"]
assert hrt(d2, "", nextPlayerDict, "1") == "1"
assert hrt(d2, "a", nextPlayerDict, "2") == "1"

assert hrt_dp(d2, "2") == "2"

d3 = ["abcd", "abede", "acd"]
assert hrt(d3, "", nextPlayerDict, "1") == "2"
assert hrt(d3, "ab", nextPlayerDict, "2") == "2"

assert hrt_dp(d3, "1") == "2"

d4 = ["ab", "abc", "dab", "dacd"]
assert hrt(d4, "", nextPlayerDict, "1") == "1"
assert hrt(d4, "ab", nextPlayerDict, "1") == "2"
assert hrt(d4, "da", nextPlayerDict, "2") == "2"

assert hrt_dp(d4, "1") == "1"

d5 = ["cat", "dogs", "cats"]
assert hrt(d5, "", nextPlayerDict, "1") == "1"

assert hrt_dp(d5, "1") == "1"

d6 = ["cat", "dog", "cats"]
assert hrt(d6, "", nextPlayerDict, "1") == "2"

assert hrt_dp(d6, "1") == "2"
