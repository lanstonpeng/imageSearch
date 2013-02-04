def hammingDis(h1,h2):
    num , diff = 0 ,h1 ^ h2 
    while diff:
        num += diff & 1
        diff = diff >> 1 
    return num

def hamming(h1,h2):
    num, diff = 0 ,h1 ^ h2
    while diff:
        diff &= diff - 1
        num += 1
    return num
#print hammingDis(2,3)

