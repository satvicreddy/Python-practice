# You are given a string .
# Your task is to verify that  is a floating point number.

# In this task, a valid float number must satisfy all of the following requirements:

#  Number can start with +, - or . symbol.
# For example:
# ✔
# +4.50
# ✔
# -1.0
# ✔
# .5
# ✔
# -.7
# ✔
# +.4
# ✖
#  -+4.5

#  Number must contain at least  decimal value.
# For example:
# ✖
#  12.
# ✔
# 12.0  

#  Number must have exactly one . symbol.
 
 
 # Enter your code here. Read input from STDIN. Print output to STDOUT
import re

regex = re.compile(r"^[+-]?\d*?\.\d+$")

for _ in range(int(input())):
    print(bool(regex.match(input())))
