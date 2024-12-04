rows = 0
columns = 0
with open("Day4inputExample", "r") as input:
        for line in input:
            row = line.strip()
            rows +=1
            if columns == 0:
                print(row)
                columns = len(row)

print(rows, columns)
