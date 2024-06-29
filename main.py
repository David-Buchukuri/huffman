from huffman_encoder import HuffmanEncoder
from huffman_decoder import HuffmanDecoder

encoder = HuffmanEncoder('./plaintext.txt')
encoder.compressTextIntoBinaryFile()
HuffmanDecoder.decompress('./encoded.bin')
