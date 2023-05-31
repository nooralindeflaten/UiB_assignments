

import itertools

def xor(v1,v2):
    res = []
    for i in range(len(v1)):
        b = (v1[i] + v2[i]) % 2
        res.append(b)
    return res

'''

c = [str(int(a[i])^int(b[i])) for i in range len(a)]
c = ''.join(c)
def bxor(a,b):
    C = bin(int(a,2) ^ int(b,2))
    return C
'''

def mult(a,b,pol):
    res = []
    for i in range(len(a)):
        res.append(0)
    
    for i in range(len(a)):
        if b[i] == 1:
            shift = a
            for s in range(i):
                overflow = (shift[-1] == 1)
                shift = [0] + shift[:-1]
                if overflow:
                    shift = xor(shift,pol)
            res = xor(res,shift)
    return res

def createX():
    x = itertools.product([0,1],repeat=6)
    y = list(x)
    #h = itertools.combinations(y,y)
    return y

def preform(x,k,irr):
    #multiply x^3 over the polynomial 
    mult1 = mult(mult(x,x,irr),x,irr)
    # (x+k)
    xorxk = xor(x,k)
    # (x,k)^3
    mult2 = mult(mult(xorxk,xorxk,irr),xorxk,irr)
    # xor x^3 and (x+k)
    xor1 = xor(mult1,mult2)
    xor2 = xor(xor1,k)
    return xor2

def lookuptable(irr):
    x = createX()
    y = createX()
    for i in range(len(x)):
        xf = list(x[i])
        for j in range(len(y)):
            f = open("/Users/nooralindeflaten/Downloads/test1/INF143AOBLIG1/lookuptabletask3.out","a")
            yf = list(y[j])
            ff = preform(xf,yf,irr)
            textoutput = " ".join(str(e) for e in xf)
            t1 = " ".join(str(e) for e in yf)
            t2 = " ".join(str(e) for e in ff)
            f.write(textoutput + "," + t1 + " -> " + t2 + "\n")
            #print("round", ff,yf,xf)
            f.close()



def main():
    pol = [1,0,0,0,0,1]
    #pol = [1,1,0]
    lookuptable(pol)
    

if __name__=="__main__":
    main()

