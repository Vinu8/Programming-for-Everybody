'''
 Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers. 

*******************************************************
import re

name = input('Enter file name : ')
if len(name) < 1 : name = 'regex_sum_42.txt'
handle = open(name)

sum = 0
num_list = []

for line in handle:
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    if len(num) < 1 : continue
    for i in num:
        num_list.append(int(i))

for i in num_list:
    sum = sum + i
print(sum)

*******************************************************
'''
import re
print( sum( [ int(i) for i in re.findall('[0-9]+',open(input('enter file name : ')).read()) ] ) )