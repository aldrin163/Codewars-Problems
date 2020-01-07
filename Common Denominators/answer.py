from math import gcd

def lcm(array):
    a = array[0]
    for i in array[1:]:
      l = a*i//gcd(a,i)
      a = l
    return l

def convertFracts(lst):
    denominators = []
    for i in lst:
        denominators.append(i[1])
    if not len(denominators):
        return []
    l = lcm(denominators)       
    return [[ (l*i[0]//i[1]) ,l] for i in lst]