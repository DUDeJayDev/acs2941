# Given two binary strings a and b, return their sum as a binary string.

def addBinary(a: str, b: str) -> str:
    a_bin = int(a, 2)
    b_bin = int(b, 2)

    c = bin(a_bin + b_bin)

    #return "{}".format((bin(a_bin + b_bin)))[2:]
    return "{}".format(c).replace("0b", "") # sorry

addBinary("1011", "1111")