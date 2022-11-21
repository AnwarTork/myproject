from board import board

board_obj = board(matrix=(1,1))
board_obj.input_print_board()
board_obj.calculate_neighbors(0,1)
board_obj.playing_the_game(0,0,up)