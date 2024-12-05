import re
from operator import mul
pattern = "mul\(\d+,\d+\)"
sum = 0
#read input
with open("inputDay3", "r") as input:
    for line in input:
        matches = re.findall(pattern, line)
        print(matches)
        for match in matches:
            sum += eval(match)



print(sum)
