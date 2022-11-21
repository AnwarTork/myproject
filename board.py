import numpy as np

class board :
    def __init__(self,row,cols):
        self.row = 3
        self.cols = 3
    def input_print_board(self):
        #row = int(input("Enter Number of rows:"))
        #cols = int(input("Enter Number of cols:"))
        for i in range(self.row):
            a = []
            for j in range(self.cols):
                val = int(input("Enter Number:"))
                a.append(val)
            self.matrix.append(a)
        arr = np.array(self.matrix)
        for i in range(self.row):
            for j in range(self.cols):
                print(arr[i][j], end=" ")
            print()
    def calculate_neighbors(self,row_index,col_index):
        row_index = int(input("input the cell's rows number that you will calculate the neighbors for it"))
        cols_index = int(input("input the cell's column numbers that you will calculate the neighbors for it"))
        neighbors = lambda x, y: [(x2, y2) for x2 in range(x - 1, x + 2)
                                  for y2 in range(y - 1, y + 2)
                                  if (-1 < x <= self.row and
                                      -1 < y <= self.cols and
                                      (x != x2 or y != y2) and
                                      (0 <= x2 <= self.row) and
                                      (0 <= y2 <= self.cols))]
        print(neighbors(row_index,col_index))


    def playing_the_game(self,row_index,cols_index,control,matrix):
        try:
            while True:
                row_index = int(input("input the cell's rows number for the start point "))
                cols_index = int(input("input the cell's column numbers for the start point"))
                control = input("Move left, right, up, down")
                control = control.lower()
                if control == "left":
                    print("you can not move on")
                elif control == "right":
                    matrix[row_index][cols_index] = matrix[row_index][cols_index + 1]
                    if matrix[row_index][cols_index + 1] == 0 :
                        print("you can not move on")
                    elif matrix[row_index][cols_index + 1] == matrix[row_index][cols_index]:
                        result = matrix[row_index][cols_index] + matrix[row_index][cols_index + 1]
                        print(result)
                        matrix[row_index][cols_index] = 0
                        matrix[cols_index][cols_index + 1] = 0
                    elif matrix[row_index][cols_index + 1] != matrix[row_index][cols_index] and matrix[row_index][cols_index + 1]  != 0 :
                        result = matrix[row_index][cols_index] + matrix[row_index][cols_index + 1]
                        print(result)
                        matrix[row_index][cols_index + 1 ] = matrix[row_index][cols_index]
                        matrix[row_index][cols_index] = 0
                elif control == "up":
                    print("you can not move on")
                elif control == "down":
                    matrix[row_index][cols_index] = matrix[row_index][cols_index + 1]
                    if matrix[row_index][cols_index + 1] == 0:
                        print("you lose")
                    elif matrix[row_index][cols_index + 1] == matrix[row_index][cols_index]:
                        result = matrix[row_index][cols_index] + matrix[row_index][cols_index + 1]
                        print(result)
                        matrix[row_index][cols_index] = 0
                        matrix[cols_index][cols_index + 1] = 0
                    elif matrix[row_index][cols_index + 1] != matrix[row_index][cols_index] and matrix[row_index][cols_index + 1] != 0:
                        result = matrix[row_index][cols_index] + matrix[row_index][cols_index + 1]
                        print(result)
                        matrix[row_index][cols_index + 1] = matrix[row_index][cols_index]
                        matrix[row_index][cols_index] = 0
        except IndexError:
            print("That's out of range, please pick somewhere else to move")


