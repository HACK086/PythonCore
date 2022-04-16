user_input = str(input("Enter cells: "))
user_input = user_input.replace('_', ' ')
cells = [x for x in user_input]

matrix = [[cells[0], cells[1], cells[2]],
     [cells[3], cells[4], cells[5]],
     [cells[6], cells[7], cells[8]]]


# output
def board_output(board):
    print("---------")
    for i in board:
        print("| ", end="")
        for j in i:
            print(j, end=" ")
        print("|")
    print("---------")


board_output(matrix)
while True:
    move = input("Enter the coordinates: ")
    sp_move = move.split()
    if move[0].isdigit() is not True or move[2].isdigit() is not True:
        print("You should enter numbers!")
        continue
    if int(sp_move[0]) > 3 or int(sp_move[1]) < 0:
        print("Coordinates should be from 1 to 3!")
        continue
    elif "X" in matrix[int(sp_move[0]) - 1][int(sp_move[1]) - 1] or "O" in matrix[int(sp_move[0]) - 1][int(sp_move[1]) - 1]:
        print("This cell is occupied! Choose another one!")
        continue
    else:
        break

coordinate_x, coordinate_y = move.split()
coordinate_x = int(coordinate_x) - 1
coordinate_y = int(coordinate_y) - 1

matrix[coordinate_x][coordinate_y] = "X"
board_output(matrix)