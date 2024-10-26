__author__ = "Prayas"

import re

#check file name before execution it could be 2091693
file_name = "regex_sum_2110012.txt"
#file_name = "regex_sum_2091693.txt" 
with open(file_name, 'r') as file:
    text = file.read()

numbers = re.findall(r'[0-9]+', text)

total_sum = sum(int(num) for num in numbers)

print("Sum:", total_sum)

#For 2091693 sum is 358113
#For 2110012 sum is 