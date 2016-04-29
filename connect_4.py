import numpy as np

class LOA():
	def __init__(self):
		self.board = np.zeros((6,7),dtype =int)
		self.state = np.zeros((6,7),dtype =int)
		self.first_move = 1
		self.player_number = input('enter the player no')
	
	def display(self):
		print '*************************************'
		print self.board

	def drop(self,move,player):
		if(self.board[0][move] != 0):
			print 'akala lav jaara bhenchod'
			return 1
		else:	
			for i in range(5,-1,-1):
				if(self.board[i][move] == 0):
					self.board[i][move] = player
					break
			return 0

	def game_over(self):
		n1 = 0
		for j in range(0,7):
				for i in range(5,-1,-1):
					self.state = np.copy(self.board)
					if(self.state[i][j] == 0 ):
						move = i,j		
						if(((self.comp_utility(move,2,5) == -1)|(self.comp_utility(move,4,5) == 1))):
							n1+=1

		return (0 if n1 ==0 else 1)						

	def get_move(self,player):
		self.state = np.copy(self.board)
		move = 3,5
		if(((self.comp_utility(move,2,4) == -1)|(self.comp_utility(move,4,4) == 1))):
			return -1
		else:
			self.score,self.move_ret = np.zeros(50,dtype = int),np.zeros(50,dtype = int)
			count = 0
			for j in range(0,7):
				for i in range(5,-1,-1):
					self.state = np.copy(self.board)
					if(self.state[i][j] == 0 ):
						move = i,j
						#print move
						if((self.comp_utility(move,2,4)== -1)):
							#print 'yada zhala aahe hein'
							if(self.board[i+1][j] != 0 ):
								return j
						self.score[count] = self.min_max(move,player)
						self.move_ret[count] = j
						count+=1
			max_move = self.move_ret[np.argmax(self.score)]
			y = max_move
			return y		


	def min_max(self,move,player):
		if(self.comp_utility(move,player,4)):
			return 100			
		elif(self.comp_utility(move,player,3)):
			return 50
		elif(self.comp_utility(move,player,2)):
			return 30			
		elif(self.comp_utility(move,player,1)):
			return 10			
		else:
			return 0			
	

	def comp_utility(self,move,player,peices):
		if (self.peices_in_order(move, player, (0, 1),peices) or
			self.peices_in_order(move, player, (1, 0),peices) or
			self.peices_in_order(move, player, (1, -1),peices) or
			self.peices_in_order(move, player, (1,  1),peices)):
			return (+1 if player==4 else -1)
		else:
			return 0
	
	def peices_in_order(self,move,player,(delta_x,delta_y),peices):
		x,y = move
		self.state[x][y] = player
		n = 0
		#print move
		while self.state.item((x,y)) == player:
			n+=1
			x,y = x + delta_x , y + delta_y
			if(((self.validate_x(x))|(self.validate(y)))):
				break
			else:
				pass
		x,y = move
		while self.state.item((x,y)) == player:
			n+=1
			x,y = x - delta_x , y - delta_y
			if(((self.validate_x(x))|(self.validate(y)))):
				break
			else:
				pass
		n -= 1
		#print n
		return (n >= peices)	

	def validate(self,move):
		if((move >= 0)& (move < 7) ):
			return 0
		else:
			return 1
	
	def validate_move(self,move):
		if((move >= 0)& (move <= 7) ):
			return 0
		else:
			return 1
	
	def validate_x(self,move):
		if((move >= 0)& (move < 6) ):
			return 0
		else:
			return 1

			
	def play_game(self):
		while True:
			#self.display()
			if(self.game_over() == 1):
				break
			if(self.player_number == 2):
				player = 2
				move =  input('enter the column')
				while(self.validate_move(move)):
					move =  input('enter the correct column')
				self.drop(move-1,player)
				self.display()
			if(self.game_over() == 1):
				break	
			player = 4
			if(self.first_move):
				move = 3
				self.first_move = 0
				self.player_number = 2
			else:					
				move = self.get_move(player)
			if(self.game_over() == 1):
				break	
			self.drop(move,player)
			self.display()
		print 'game sampla ghari jaave'	

if __name__ == '__main__':
	loa = LOA()
	loa.play_game()
