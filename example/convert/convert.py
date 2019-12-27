# Author (Created): Roger "Equah" Hürzeler
# Date (Created): 12019.12.27 HE
# License: apache-2.0

import equah.sblint

# [>] Main
if __name__ == "__main__":
    
    # [i] Start number.
    start_number = 420
    
    # [i] To SBLInt bytearray.
    sblint_bytearray = bytearray()
    sblint_bytearray_len = equah.sblint.int_to_bytearray(start_number, sblint_bytearray)
    
    # [i] Back to number.
    # [NOTE] Returns tuple (number_value, amount_bytes_read).
    end_number, end_number_len = equah.sblint.list_to_int(sblint_bytearray)
    
    # [i] Print conversion of number.
    print("{} -> {} -> {}".format(start_number, sblint_bytearray, end_number))
    
    exit()
