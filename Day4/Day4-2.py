rows = 0
columns = 0
current_row = 0
current_column = 0
list_of_A = []

def left(position, size_x, size_y):
    if position[0] > 0:
        return (position[0]-1,position[1],4)

def right(position, size_x, size_y):
    if position[0] < (size_x - 1):
        return (position[0]+1,position[1],6)

def up(position, size_x, size_y):
    if position[1] > 0:
        return (position[0],position[1]-1,8)

def down(position, size_x, size_y):
    if position[1] < (size_y - 1):
        return (position[0],position[1]+1,2)


def left_down(position, size_x, size_y):
    if (position[0] > 0 and (position[1] < (size_y - 1))):
        return (position[0]-1,position[1]+1,1)

def left_up(position, size_x, size_y):
    if position[0] > 0 and position[1] > 0:
        return (position[0]-1,position[1]-1,7)

def right_down(position, size_x, size_y):
    if position[0] < (size_x - 1) and position[1] < (size_y - 1):
       return (position[0]+1,position[1]+1,3)

def right_up(position, size_x, size_y):
    if position[0] < (size_x - 1) and position[1] > 0:
        return (position[0]+1,position[1]-1,9)




def around_position(position, size_x, size_y):
    #triple: x,y,direction direction= numpad number,  5 is the middle
    around = []
    #left 4
    around.append(left(position, size_x, size_y))
    #right 6
    around.append(right(position, size_x, size_y))
    #up 8
    around.append(up(position, size_x, size_y))
    #down 2
    around.append(down(position, size_x, size_y))
    #left-down 1
    around.append(left_down(position, size_x, size_y))
    #left-up 7
    around.append(left_up(position, size_x, size_y))
    #right-down 3
    around.append(right_down(position, size_x, size_y))
    #right-up 9
    around.append(right_up(position, size_x, size_y))
    return around

def check_at(x, y, direction,letter_to_look_for, puzzle):
    #triple: x,y,direction direction= numpad number,  5 is the middle
    #left 4
    position = (x,y)
    size_x = len(puzzle[0])
    size_y = len(puzzle)
    check_coord =  None
    if direction == 4:
        check_coord = (left(position, size_x, size_y))
    #right 6
    elif direction == 6:
        check_coord = (right(position, size_x, size_y))
    #up 8
    elif direction == 8:
        check_coord = (up(position, size_x, size_y))
    #down 2
    elif direction == 2:
        check_coord = (down(position, size_x, size_y))
    #left-down 1
    elif direction == 1:
        check_coord = (left_down(position, size_x, size_y))
    #left-up 7
    elif direction == 7:
        check_coord = (left_up(position, size_x, size_y))
    #right-down 3
    elif direction == 3:
        check_coord = (right_down(position, size_x, size_y))
    #right-up 9
    elif direction == 9:
        check_coord = (right_up(position, size_x, size_y))
    if check_coord is not None and puzzle[check_coord[1]][check_coord[0]] == letter_to_look_for:
        return True
    else:
        return False

def check_around(list_of_X, letter_to_look_for, puzzle):
    #triple: x,y,direction direction= numpad number,  5 is the middle
    found_at_position = []
    for x in list_of_X:
        for entry in around_position((x[0], x[1]),len(lines[0]), len(lines)):
            if entry is not None:
                if puzzle[entry[1]][entry[0]] == letter_to_look_for:
                    found_at_position.append((entry))
    return found_at_position



with open("Day4input", "r") as input:
        text = input.read()
        print(text)
        lines = text.splitlines()
        for line in lines:
            rows +=1
            if columns == 0:
                columns = len(line)
            for letter in line:
                if letter == "A":
                    list_of_A.append((current_column,current_row))
                    print(f"Found A at {current_column},{current_row}")
                current_column += 1
            current_column = 0
            current_row += 1

x_mas_count = 0
for a in list_of_A:
    if (((check_at(a[0], a[1], 9,"M", lines) and check_at(a[0], a[1], 1,"S", lines)) or (check_at(a[0], a[1], 9,"S", lines) and check_at(a[0], a[1], 1,"M", lines))) and ((check_at(a[0], a[1], 7,"M", lines) and check_at(a[0], a[1], 3,"S", lines)) or (check_at(a[0], a[1], 7,"S", lines) and check_at(a[0], a[1], 3,"M", lines)))):
        x_mas_count += 1





print(x_mas_count)
