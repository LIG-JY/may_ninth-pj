#2명의 players 가정합니다.


from randomo import randrange

def roll(p):
	return randrange(1,7)

player = input("roll or stop")

player_score = 0

def pig_gamge(x):
	if player == 'roll':
		temp = 0
		if roll(player) == 1:
			temp = 0
		else:
			temp = temp + roll(player)
	plater_score = player_score + temp
	return player_score





