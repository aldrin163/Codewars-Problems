from fractions import gcd
def convertFracts(lst):
    D = 1
    for _,d in lst:
        D*= d//gcd(d,D)
    return [[D*n//d,D] for n,d in lst]