from heapq import heapify, heappop, heappush

class Node:
    def __init__(self, count, char = None) -> None:
        self.count = count
        self.char = char
        self.right = None
        self.left = None
    
    def __lt__(self, other):
        return self.count < other.count

    def __repr__(self):
        return f"char: {self.char}, count: {self.count}"


class HuffmanEncoder:
    def __init__(self, path):
        file = open(path, 'r')
        self.text = file.read()
        file.close()
        
        self.encodeTable = {}
        self.decodeTable = {}

        self.__buildEncodingDecodingTables()

    
    def __buildEncodingDecodingTables(self):
        huffmanTree = self.__buildTree()
        self.__assignBinariesToChars(huffmanTree, ['0'])

        for char in self.encodeTable:
            binary = self.encodeTable[char]
            self.decodeTable[binary] = char

    def __assignBinariesToChars(self, node, currBinaryNumber):        
        if node.char:
            self.encodeTable[node.char] = "".join(currBinaryNumber)
            return
        
        currBinaryNumber.append('0')
        self.__assignBinariesToChars(node.left, currBinaryNumber)
        currBinaryNumber.pop()

        currBinaryNumber.append('1')
        self.__assignBinariesToChars(node.right, currBinaryNumber)
        currBinaryNumber.pop()

    
    def __buildTree(self):
        charNodes = self.__countChars()
        heapify(charNodes)

        while len(charNodes) > 1:
            leastFrequent = heappop(charNodes)
            secondLeastFrequent = heappop(charNodes)

            parentNode = Node(
                count = leastFrequent.count + secondLeastFrequent.count
            )

            parentNode.left = leastFrequent
            parentNode.right = secondLeastFrequent
            heappush(charNodes, parentNode)
        
        return charNodes[0]

    
    def __countChars(self):
        charCount = {}
        for char in self.text:
            if char not in charCount:
                charCount[char] = 0
            
            charCount[char] += 1
        

        charNodes = []
        for char in charCount:
            charNodes.append(
                Node(charCount[char], char)
            )
        
        return charNodes