number_of_safe_reports = 0
list_of_reports = []
add_to_dampener = []



def check_report(report):
        safe = True
        mode = ""
        for n1,n2 in zip(report[:-1],report[1:]):
            if n1 < n2:
                if mode == "":
                    mode = "a"
                if mode == "d" or ((n2 - n1) > 3):
                    safe = False
                    break
            elif n1 > n2:
                if mode == "":
                    mode = "d"
                if mode == "a" or ((n1 - n2) > 3):
                    safe = False
                    break
            else:
                safe = False
                break
        return safe



#read input
with open("inputDay2", "r") as input:
    for line in input:
        mode = "" # a for ascending, d for descending
        numbers = [int(number) for number in line.split(" ")]
        list_of_reports.append(numbers)

for report in list_of_reports:
   if check_report(report):
       number_of_safe_reports += 1
   else:
       add_to_dampener.append(report)


for report in add_to_dampener:
    dampener = []
    for index, item in enumerate(report):
        #print(f"{index}: {report}\n")
        altered_report = []
        for i, element in enumerate(report):
            if i != index:
                altered_report.append(element)
        dampener.append(altered_report)
    for report in dampener:
        if check_report(report):
            number_of_safe_reports += 1
            break






print(f"Save reports: {number_of_safe_reports}")
