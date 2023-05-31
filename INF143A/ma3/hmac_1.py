import hashlib
import sys


def XOR(bits1,bits2):
    return [ (b[0] + b[1]) % 2 for b in zip(bits1,bits2) ]

#Converts a sequence of bytes (read from a file) into a list of bits (0s and 1s)
def bytes_to_bits(B):
    bits = []
    for i in range(len(B)):
        current_byte = B[i]
        mask = 128
        for j in range(8):
            if (current_byte >= mask):
                bits.append(1)
                current_byte -= mask
            else:
                bits.append(0)
            mask = mask // 2
    return bits

#opposite of the above operation
def bits_to_bytes(B):
    byteseq = []
    num_bytes = len(B) // 8
    assert 8*num_bytes == len(B)
    for i in range(num_bytes):
        current_byte = 0
        bit_sequence = B[(i*8):((i+1)*8)]
        mask = 128
        for j in range(8):
            current_byte += mask * bit_sequence[j]
            mask = mask // 2
        byteseq.append(current_byte.to_bytes(1,"big"))
    return byteseq

#writes a sequence of bytes to a file
def write_file(output_file, byteseq):
    f = open(output_file, "wb")
    for i in range(len(byteseq)):
        f.write(byteseq[i])
    f.close()

#reads a sequence of bytes from a file
def read_file(input_file):
    f = open(input_file, "rb")
    data = f.read()
    f.close()
    return data


####################################### IMPLEMENTATION ###################################

def pad(P):
    # Pad a message P to a multiple of 512 bits
    blocks = []
    i = 0
    while i < len(P):
        if(i + 512 > len(P)):
            rest = len(P)
            offset = 512 - rest
            blocks += [0]*offset + P[i:]
        blocks += P[i:i+512]
        i += 512
    return blocks

def sha256_hash(bit_array):
    # Hash with sha256
    byte_array = bits_to_bytes(bit_array)
    h = hashlib.sha256(b''.join(byte_array)).digest()
    return bytes_to_bits(h)

def hmac(K,M):
    # size of blocks 64 bytes
    I_PAD = [0,0,1,1,0,1,1,0] * 64
    O_PAD = [0,1,0,1,1,1,0,0] * 64

    #The first block:
    i_key = XOR(K,I_PAD)
    o_key = XOR(K,O_PAD)
    inner_h = sha256_hash(i_key + M)
    outer_h = sha256_hash(o_key + inner_h)
    return outer_h

def main():
    #
    plaintext = ''
    key = ''
    output_file = ''
    if len(sys.argv) != 4:
            print("Usage: " + sys.argv[0] + " PLAINTEXT_FILE KEY_FILE IV_FILE OUTPUT_FILE")
    else:
        plaintext = sys.argv[1]
        key = sys.argv[2]
        output_file = sys.argv[3]
    
    P = bytes_to_bits(read_file(plaintext))
    K = bytes_to_bits(read_file(key))
    HMAC = hmac(K,P)
    #print(HMAC)
    write_file(output_file,bits_to_bytes(HMAC))
    #print(bits_to_bytes(HMAC))
    print("check your output file: ", output_file, " For results")

main()