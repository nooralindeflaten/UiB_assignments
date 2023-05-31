
'''
Construct an LFSR that will go through 2^30 - 1 distinct states before it loops

ANWSER
the new bit of the LFSR is the XOR of the 30th, 27th, and 0th
bits of the current state. Shifting all bits
one position to the right, and inserting the newly generated bit at the
start of the list

We can represent this as a reccurence relation:
S(t+30) = S(t+27) + S(t) (mod 2)

S(t)
Represents the state of the LFSR at a time t

S(t+30) represents the state after 30 steps.

This shows us that the output bit og the LFSR is the XOR of
the 30th, 27th, and 0th bits of the current state. 


'''
# construct the reccurense relation with code:
def LFSR(States,t):
    St = States[t][-1]
    St27 = States[t][-2]
    St30 = (St + St27) % 2
    # the new bit
    newState = [St30] + States[t][:-1]
    return newState

def lfone(state):
    # list of output of the state (the rightmost bit)
    outs = []
    # list for states visited
    States = []
    for i in range(500):
        #Adding the current state, and the output bit from it
        States.append(state)
        outs.append(state[-1])
        # creating the next stage at time i
        newState = LFSR(States,i)
        state = newState
    #print(States)
    Output = ''.join([str(x) for x in outs])
    return Output


def main():
    LFSR = [1] + [0]*28 + [1]
    l = lfone(LFSR)
    f = open("/Users/nooralindeflaten/Downloads/test1/INF143AOBLIG1/lfsr.out","a")
    f.write(l)
    f.close()


if __name__=="__main__":
    main()