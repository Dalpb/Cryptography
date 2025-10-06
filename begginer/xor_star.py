from Crypto.Util.number import *
string = "label"
integer = 13
b_str = ord(string[0])
b_int = long_to_bytes(integer)
byte = b_int[0] # accedo al primer byte
print((b_int[0] >>2) & 1) ## bitwise operators, acceder al bit
print(bin(b_int[0])) # to see bits

# consider that bytes contains one byte
def xor(b1: bytes, b2: bytes):
    r =""
    for k in range(7):
        bit_b1 = (b1[0] >> k) & 1
        bit_b2 = (b2[0] >> k) & 1
        bit_r =  ((not bit_b1) and bit_b2 ) or ((not bit_b2) and bit_b1)
        r = str(int(bit_r)) + r
    return r

def main():
    numbers = []
    for i in range(0,len(string)):
        char = string[i]
        ch_integer = ord(char)
        byte_char = long_to_bytes(ch_integer)
        xorbyte =  xor(byte_char,b_int)
        numbers.append(int(xorbyte,2))

    print(numbers)
    print("".join(chr(o) for o in numbers))


main()


# 765 -> 1011111101
# b_int -> [10, 1111101] así se comporta