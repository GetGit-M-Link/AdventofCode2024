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

score = 0
for number in list1:
    count = 0
    for second_number in list2:
        if number == second_number:
            count += 1
    score += (count * number)


print(score)

