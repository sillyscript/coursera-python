__author__ = "Prayas"

import re

file_name = "regex_sum_2110012.txt" 
with open(file_name, 'r') as file:
    text = file.read()

numbers = re.findall(r'[0-9]+', text)

total_sum = sum(int(num) for num in numbers)

print("Sum:", total_sum)