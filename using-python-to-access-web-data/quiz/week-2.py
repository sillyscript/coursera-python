__author__ = "Prayas"


1. Which of the following best describes "Regular Expressions"?
Ans: A way to calculate mathematical values paying attention to operator precedence _> wrong

2. Which of the following is the way we match the "start of a line" in a regular expression?
Ans: ^

3. What would the following mean in a regular expression? [a-z0-9]
Ans: Match an entire line as long as it is lowercase letters or digits _> wrong


4. What is the type of the return value of the re.findall() method?
Ans: A list of strings


5. What is the "wild card" character in a regular expression (i.e., the character that matches any character)?
Ans: "."


6. What is the difference between the "+" and "*" character in regular expressions?
Ans: The "+" matches at least one character and the "*" matches zero or more characters


7. What does the "[0-9]+" match in a regular expression?
Ans: One or more digits


8. What does the following Python sequence print out?

import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

['From: Using the :']

Ans: ['From: Using the :']


9. What character do you add to the "+" or "*" to indicate that the match is to be done in a non-greedy manner?
Ans: ?


10. Given the following line of text:

import re
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
v = re.findall('\S+?@\S+', line)
print(v)

['stephen.marquard@uct.ac.za']

Ans: stephen.marquard@uct.ac.za
