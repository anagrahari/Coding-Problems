'''
 Build the Huffman coding tree and determine the codes for the following set of letters and weights Letter Frequency
 2 3 5 7 1 13 17 19 23 31 37 41 (b) What is the expected length in bits of a message containing n characters for this frequency distribution (c)
 Encode message "Deed" by using this Huffman code (d) Decode the following Huffman code 0100111101010

'''

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isEnd = False  # whether this node is an end of a word
        self.val = None
        self.children = dict()  # map a char to the child node


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, val):

        currNode = self.root

        for c in word:
            if c not in currNode.children:
                currNode.children[c] = TrieNode()

            currNode = currNode.children[c]

        currNode.isEnd = True
        currNode.val = val

    def search(self, word, index):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        #print word, 'word'
        currNode = self.root
        if currNode.val is not None and currNode.isEnd:
            return [currNode.val,index]

        for c in word:
            #print c
            if c not in currNode.children:
                return False

            currNode = currNode.children[c]
            index +=1
            if currNode.val is not None and currNode.isEnd:
                return [currNode.val,index]


        return [currNode.val, index]


trie = Trie()
trie.insert('1011', 'a')
trie.insert('100101', 'b')
trie.insert('110001', 'c')
trie.insert('100000', 'd')
trie.insert('111111', 'newline')
trie.insert('111110', 'p')
trie.insert('000001', 'q')



ans = ''
i = 0
val = '1111100000011011111111100101110001111110'
while i < len(val):
    #print val[i:]
    value = trie.search(val[i:], i)
    #print value
    i = value[1]
    if value[0] == 'newline':
        ans += '\n'
    else: ans += value[0]
print ans