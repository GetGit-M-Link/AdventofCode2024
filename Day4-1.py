rows = 0
columns = 0
current_row = 0
current_column = 0
list_of_X = []

def around_position(position, size_x, size_y):
    #triple: x,y,direction direction= numpad number,  5 is the middle
    around = []
    #left
    if position[0] > 0:
        around.append((position[0]-1,position[1],4))
    #right
    if position[0] < size_x:
        around.append((position[0]+1,position[1],6))
    #up
    if position[1] > 0:
        around.append((position[0],position[1]-1,8))
    #down
    if position[1] < size_y:
        around.append((position[0],position[1]+1,6))
    #left-down 1
    #left-up 7
    #right-down 3
    #right-up 9


def check_around(position, letter_to_look_for, puzzle):
    #triple: x,y,direction direction= numpad number,  5 is the middle
    found_at_position = []
    for entry in around_position(position):
        if puzzle[entry[1]][entry[0]] == letter_to_look_for:
            found_at_position.append((entry))
    return found_at_position



with open("Day4inputExample", "r") as input:
        text = input.read()
        print(text)
        lines = text.splitlines()
        for line in lines:
            rows +=1
            if columns == 0:
                columns = len(line)
            for letter in line:
                if letter == "X":
                    list_of_X.append((current_column,current_row))
                    print(f"Found X at {current_column},{current_row}")
                current_column += 1
            current_column = 0
            current_row += 1

#for x in list_of_X:

print(rows, columns)
