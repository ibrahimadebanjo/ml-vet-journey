theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(theBoard['top-L'] + "|" + theBoard['top-M'] + "|" + theBoard['top-R'] )
    print("+-+-+-")
    print(theBoard['mid-L'] + "|" + theBoard['mid-M'] + "|" + theBoard['mid-R'] )
    print("+-+-+-")
    print(theBoard['low-L'] + "|" + theBoard['mid-M'] + "|" + theBoard['low-R'] )
    print("+-+-+-")

turn = 'X'
for i in range(9):
   printBoard(theBoard)
   print('Turn for ' + turn + '. Move on which space?')
   move = input()
   theBoard[move] = turn
   if turn == 'X':
        turn = 'O'
   else:
        turn = 'X'
printBoard(theBoard)
print(theBoard)
# Full source Code here:http://nostarch.com/automatestuff/
