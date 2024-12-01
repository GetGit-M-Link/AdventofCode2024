total_distance = 0
list1 = []
list2 = []
with open("inputDay1-1", "r") as input:
    for line in input:
        numbers = line.split("   ")
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))

list1.sort()
list2.sort()

for first_number, second_number in zip(list1, list2):
     line_distance = abs(first_number - second_number)
     total_distance += line_distance

print(total_distance)

