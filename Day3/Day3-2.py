import re
from operator import mul
pattern = "mul\(\d+,\d+\)|do\(\)|don't\(\)"
sum = 0
on = 0
off = 0
#read input
with open("inputDay3", "r") as input:
        text = input.read()
        matches = re.findall(pattern, text)
        enabled = True
        for match in matches:
            if match == "don't()":
                enabled = False
                off += 1
            elif match == 'do()':
                enabled = True
                on += 1
            else:
                if enabled:
                    print(f"{match}\n")
                    sum += eval(match)
                else:
                    print(f"not {match}\n")



print(sum)
