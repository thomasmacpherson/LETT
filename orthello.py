
pieces = (0,0,0) # player 1, 2 and total pieces

gridSize = 16

totalGamePlaces = gridSize * gridSize

turnPrint = ("Opponent's turn", "Your turn")
winPrint = ("You won", "You lost", "It was a draw")

playerColours = ((0,0,0),(255,255,255))

turn = True # player1's turn first


def checkInput(int x, int y):
	if gridColours[x][y] =! 0:
		printLCD(!turn, 1, "Can't go there", 2)
		changePixel(x, y, Red, 2)
		return False
	else:
		changePixel(x,y, playerColours[turn],0)
		return True

def checkForFlips(int x, int y):







while (pieces[2] < totalGamePlaces and (pieces[2]>1...): # main game loop
	printLCD(0,1,turnPrint1[turn],0) # player, line, message, time (0 stay until overridden)
	printLCD(1,1,turnPrint2[!turn],0)

	wait for input and checkInput(x, y):
		pass
	checkForFlips(x, y)
	
	turn = !turn


if pieces[0] > pieces[1]:
	printLCD(0,1, winPrint[0], 0)
	printLCD(1,1, winPrint[1], 0)

elif pieces[1] > pieces[0]:
	printLCD(0,1, winPrint[1], 0)
	printLCD(1,1, winPrint[0], 0)	

elif:
	printLCD(3,1, winPrint[2], 0)




