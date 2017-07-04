#This is a demo for encrypting a string using
#self-defined number system

import n_nary as nn

from string import ascii_letters as al
import sys

#ecription base map
ebm = ['a', '1@5', '64s', '*', '6','+9','&s', '30s', '5s','o', '0', '.1','8^-']


args = sys.argv
msg = args[1]

ascii_start = nums
ascii_end = nume

ascii_map = [(char,code) for char in al
                         for code in ascii_end-ascii_start]
ascii_map = dict(ascii_map)

msg_ascii_codes = [ascii_map[c] for c in msg]

msg_encripted_codes = [nn.n_nary_convert(code, 16, len(ebm),
                                         base_map2=ebm)
                                for code in msg_ascii_codes]

enc_str_l = [nn.nn_str(ebmi) for ebmi in msg_encripted_codes]
enc_str = ""
for es in enc_str_l:
    enc_str += es

print "encripted to: {0}".format(enc_str)





























