# Author (Created): Roger "Equah" Hürzeler
# Date (Created): 12019.12.27 HE
# License: apache-2.0


import equah.sbsint


# [>] List To Integer
# [i] Converts a list containing SBLInt bytes to an integer.
# [P] {list|bytes|bytearray} bl => List of SBLInt bytes.
# [R] {(int, int)} => Tuple of SBLInt value and amount of bytes read.
def list_to_int(bl) :
    
    sblint = 0
    
    sblint_len, pos = equah.sbsint.list_to_int(bl)
    
    while sblint_len >= 1 :
        sblint += bl[pos] << (8 * (sblint_len - 1))
        sblint_len -= 1
        pos += 1
        pass
    
    return (sblint, pos)

# [>] Integer To Bytearray
# [i] Converts an integer to SBLInt bytearray.
# [P] {int} i => Integer to convert to SBLInt.
# [P] {bytearray} buff => Bytearray to which SBLInt will be written.
# [R] {int} => Amount of written bytes to represent SBLInt.
def int_to_bytearray(i, buff) :
    
    size = required_bytes(i)
    shift = size - 1
    
    size += equah.sbsint.int_to_bytearray(size, buff)
    
    while shift >= 0 :
        buff.append((i >> (8 * shift)) & 0xFF)
        shift -= 1
        pass
    
    return size

# [>] Required Bytes
# [i] Computes the amount of required bytes to store the number.
# [P] {int} i => Integer to get required storage size of.
# [R] {int} => Amount of bytes to represent the given integer.
def required_bytes(i) :
    
    size = 0
    compare = 0
    
    while i > compare :
        
        compare = compare + (0xFF << (8 * size))
        size += 1
        pass
    
    
    return size
