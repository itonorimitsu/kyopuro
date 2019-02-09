"""はてなインターンの提出問題
encodeなどを使わず実装"""

# coding: utf-8

import string

# input_list = list(input())
input_list = list('UNGRAN')
upper = list(string.ascii_uppercase)
for i in input_list:
    index_num = (upper.index(i) + 13) % 26
    print(upper[index_num], end='')

print()

