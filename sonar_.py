import random
import sys

def drawBoard(board):
	hline = '	'
	for i in range(1, 6):
		hline += ('	' * 9) + str(i)

	print(hline)
	print('	' + ('0123456789' * 6))
	print()

def getDraw(board, row):