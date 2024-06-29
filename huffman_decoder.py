import pickle

class HuffmanDecoder:
    @staticmethod
    def decompress(path):
        file = open(path, 'rb')
        
        padding = file.read(1)
        padding = int.from_bytes(padding, 'big')

        tableSize = file.read(4)
        tableSize = int.from_bytes(tableSize, 'big')
       
        table = file.read(tableSize)
        table = pickle.loads(table)

        bytes = file.read()
        file.close()


        bitsArray = []
        for byte in bytes:
            byte = bin(byte)[2:]
            missingZeros = '0' * (8 - len(byte)) 
            byte = "".join([missingZeros, byte])

            for bit in byte:
                bitsArray.append(bit)
        

        idxToRemove = len(bitsArray) - 8
        for _ in range(padding):
            del bitsArray[idxToRemove]
        

        decompressedText = []
        currBitSequence = ""
        for bit in bitsArray:
            currBitSequence += bit

            if currBitSequence in table:
                decompressedText.append(table[currBitSequence])
                currBitSequence = ""

        print("".join(decompressedText))



        

        
        