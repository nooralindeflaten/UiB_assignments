
'''
block cipher simon cipher

Block size 16bits
Li and Ri are 8 bits long

Sk denotes a left cyclic shift by k bits
AND is for and
Ki is the round key 8 bits

4 rounds k 32 bits

construct keys 


I have just used the sample files, and not produced a file for my own,
but my output is the same as the sample output files. 
'''
import itertools


def readkeys(round):
    f = open("/Users/nooralindeflaten/Downloads/sample_data/cipher_key.txt","r")
    K1 = f.read()
    K = [int(x) for x in K1 if x != "\n"]
    K0 = K[:8]
    K2 = K[8:16]
    K3 = K[16:24]
    K4 = K[24:]
    if round == 0:
        return K0
    if round == 1:
        return K2
    if round == 2:
        return K3
    if round == 3:
        return K4


def shift(n,L):
    x = L[n:] + L[:n]
    return x


def xor(v1,v2):
    res = []
    for i in range(len(v1)):
        b = (v1[i] + v2[i]) % 2
        res.append(b)
    return res


def AND(A,B):
    res = []
    for i in range(len(A)):
        b = A[i] & B[i]
        res.append(b)
    return res
'''
bitwise AND
def bAND(a,b):
    C = [str(int(a[i],2) & int(b[i])) for i in range(len(a))]
    print(C)
    h = ''.join('0:0b'.format(int(x)) for x in C)
    print(h)

'''
def Round(L,R,KEY):
    # shifting S1
    S1 = shift(1,L)
    # shifting S5
    S5 = shift(5,L)
    #shifting S2
    S2 = shift(2,L)
    #print("L ", L, "S1 ",S1, " S5: ", S5, len(S5))
    # AND s1 and s2
    S1and5 = AND(S1,S5)
    #xor R and S1,S2
    XOR1 = xor(S1and5,R)
    #xor 2
    XOR2 = xor(S2,XOR1)
    #xor with key
    XOR3 = xor(XOR2,KEY)
    return XOR3,L

#preform
def preform():
    # collecting input
    f = open("/Users/nooralindeflaten/Downloads/sample_data/cipher_in1.txt","r")
    plain = f.read()
    PL = [int(x) for x in plain if x != "\n"]
    # original left and righ
    L = PL[:8]
    R = PL[8:]
    #KEY = readkeys(1)
    for i in range(4):
        KEY = readkeys(i)
        print(KEY)
        newL,NewR = Round(L,R,KEY)
        L = newL
        R = NewR
        #print("KEY: ", KEY)
    CIPHER = R + L
    print(CIPHER)
        #print("KEY ", i, " : ",KEY)

def bruteforce():
    x = itertools.product([0,1],repeat=8)
    z = list(x)
    y = []
    for i in z:
        y.append(list(i))
    return y

def decryption(CL,CR,KEY):
    # R = L. this means that
    '''
    we have the key, and the shifts we need to find R
    we can try all the different combinations of an 8 bit sequence. And comparing it
    to the known result which is CL
    '''
    # find original left
    KEYS = bruteforce()
    test = []
    newRight = []
    for i in KEYS:
        test,t2 = Round(CR,i,KEY)
        #print(test)
        if test == CL:
            # last right will be i
            # last left will be CR
            newRight = i
    return CR,newRight

def preformD():
    f = open("/Users/nooralindeflaten/Downloads/sample_data/cipher_out1.txt","r")
    PL = f.read()
    # PL input text for decryption
    C = [int(x) for x in PL if x != "\n"]
    CL = C[8:]
    CR = C[:8]
    count = 3
    for i in range(4):
        key = readkeys(count)
        # find new left
        lastL,lastR = decryption(CL,CR,key)
        CL = lastL
        CR = lastR
        count -= 1
    Cipher = CL + CR
    print(Cipher)
    
def main():
    readkeys(4)
    #print(AND([1,0,0,1],[0,1,0,1]))
    preform()
    #decryption()
    preformD()
if __name__=="__main__":
    main()