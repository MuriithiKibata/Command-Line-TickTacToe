board = ["","","","","","","","",""]
WIN_COMBO =  [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]]
  
class Tic_Tack_Toe:
  def __init__(self, name, symbol):
    self.symbol = symbol
    self.name = name

  def set_symbol(self, symbol):
    self.symbol = symbol

    
  def render_board(self):
    print("-----------")
    print(f" {board[0]} | {board[1]} | {board[2]} |")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} |")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} |")
    print("-----------")
  
  def render_icon(self, index, token):
    board[index] = token
    
  @classmethod
  def available_postions(self):
   for i in range(0, 9):
     if board[i] == "":
       print(f"Postion {i} is available \n")

  @classmethod
  def game_instructions(self):
    board = ["0","1","2","3","4","5","6","7","8"]
    print("The board layout is represented as follows \n")
    print("-----------")
    print(f" {board[0]} | {board[1]} | {board[2]} |")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} |")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} |")
    print("----------- \n")
    print("To Play enter a number that is in one of the following the postions that is 0 - 8. Each play should select his or her symbol O or X. The goal is to have either three X's or O's either diagonally or horizontally. Enter your name and symbol in the following format (John Doe, O) or or in any other manner provided the name and symbol is separated by a comma (,). Enjoy :). \n")

    
    

Tic_Tack_Toe.game_instructions()

p1 = input("Player one enter a username and symbol (X) or (O) \n")
p2 = input("Player two enter a username and symbol (X) or (O) \n")



player1_details = p1.split(",")
player2_details = p2.split(",")
player_one = Tic_Tack_Toe(player1_details[0], player1_details[1])
player_two = Tic_Tack_Toe(player2_details[0], player2_details[1])
  
i = 1

while i < len(board) + 1:
    
  if i % 2 == 0:
    turn = player_two.name
  elif i % 2 == 1:
    turn = player_one.name
  num = input(f"{turn} Enter a position: ")

  if turn == player_one.name:
    player_one.render_icon(int(num), player_one.symbol)
    player_one.render_board()
  else:
    player_two.render_icon(int(num), player_two.symbol)
    player_two.render_board()
  Tic_Tack_Toe.available_postions()
  
  i += 1


