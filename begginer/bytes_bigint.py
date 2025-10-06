from Crypto.Util.number import *
# encode msg into numbers
imsg = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

bytes_msg = long_to_bytes(imsg) # tranform int into bytes
print(bytes_msg) # print covert bytes into characters