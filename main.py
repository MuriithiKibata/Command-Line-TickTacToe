board = ["","","","","","","","",""]
WIN_COMBO =  [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]]
  
class Tic_Tack_Toe:
  def __init__(self, name, symbol):
    self.symbol = symbol
    self.name = name


  #This function renders the board
  def render_board(self):
    print("-----------")
    print(f" {board[0]} | {board[1]} | {board[2]} |")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} |")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} |")
    print("-----------")

  #This function sets and X or O to a given index if that index is not already taken
  def render_icon(self, index, token):
    if board[index] == "":
     board[index] = token
    else:
      print("THAT POSTION IS TAKEN")
    
  #This function is responsible for checks if one of the WIN_COMBO exits in the board array. If there is it return Game Over
  def game_over(self, symbol):
   arr = []
   status = ""
   for i in range(0, len(WIN_COMBO)):
    for j in range(0, 3):
     arr.append(board[WIN_COMBO[i][j]])
    if arr.count(symbol) == 3:
      status = "Game Over"
    arr.clear()
    
   return status

  #Checks which postions are available
  @classmethod
  def available_postions(self):
   for i in range(0, 9):
     if board[i] == "":
       print(f"Postion {i} is available \n")
  #Prints Out the instructions of how the game should be played
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


#Splits input string at comma to get a username and symbol. Which is used to create a new instance of the class.
player1_details = p1.split(",")
player2_details = p2.split(",")
player_one = Tic_Tack_Toe(player1_details[0], player1_details[1])


player_two = Tic_Tack_Toe(player2_details[0], player2_details[1])
  
i = 1
#variable that is used to control wether the game should carry on or has been won.
game_controller = "Continue"

#Game loop
while i < len(board) + 1 and game_controller != "Game Over":
#Determines who's turn it is two play
  if i % 2 == 0:
    turn = player_two.name
  elif i % 2 == 1:
    turn = player_one.name
    #Board index where symbol should be placed
  num = input(f"{turn} Enter a position: ")

  if turn == player_one.name:
    #Symbol is placed on the board at a given index
    player_one.render_icon(int(num), player_one.symbol)
    #Board is rendered
    player_one.render_board()
    #Variable current_player is set to the current player
    current_player = player_one.name
    #Checks if player_ones symbol is present on the board as a win combo
    game_controller = player_one.game_over(player_one.symbol)
  else:
    #Symbol is placed on the board at a given index.
    player_two.render_icon(int(num), player_two.symbol)
     #Board is rendered.
    player_two.render_board()
    #Variable current_player is set to the current player.
    current_player = player_two.name
    #Checks if player_ones symbol is present on the board as a win combo.
    game_controller = player_two.game_over(player_two.symbol)
  Tic_Tack_Toe.available_postions()
  #Loop control variable increment
  i += 1

#Renders out the current player who won.
if game_controller == "Game Over":
  print(f"{current_player} has Won!!")
