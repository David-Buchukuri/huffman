from huffman_encoder import HuffmanEncoder

encoder = HuffmanEncoder('./plaintext.txt')
for char in encoder.encodeTable:
    print(f"{char} : {encoder.encodeTable[char]}") 
