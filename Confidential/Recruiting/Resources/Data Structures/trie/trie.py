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
    
    def isPrefix(self, word):
        
        def isPrefix_helper(word):
            curr = self.root
            for letter in word:
                index = ord(letter) - ord('a')
                
                if not curr.children[index]:
                    return None
                
                curr = curr.children[index]
            return curr
          
        node = isPrefix_helper(word)
        return not(node is None)
    
    def contains(self, word):
        node = self.isPrefix_helper(word)
        if not node or not node.isEndOfWord:
            return False
        return True