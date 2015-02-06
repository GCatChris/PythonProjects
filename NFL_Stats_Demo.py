import nflgame

teams = nflgame.teams

class Team(object):

	def __init__(self, name):
		self.name = name

	def display_Team(self):
		print self.name

	def get_Team(self):
		return self.name


def main():
	nfl = []
	for team in teams:
		tmp = Team(team[0])
		nfl.append(tmp)

	for team in nfl:
		wins = 0
		losses = 0
		Q1 = 0
		Q2 = 0
		Q3 = 0
		Q4 = 0
		team.display_Team()
		games = nflgame.games(2014, home=team.get_Team(), away=team.get_Team())
		for game in games:
			if game.winner == team.get_Team():
				wins += 1
			else:
				losses += 1
			if game.is_home(team.get_Team()):
				print game.nice_score()
				Q1+= game.score_home_q1
				Q2+= game.score_home_q2
				Q3+= game.score_home_q3
				Q4+= game.score_home_q4
			else:
				print game.nice_score()
				Q1+= game.score_away_q1
				Q2+= game.score_away_q2
				Q3+= game.score_away_q3
				Q4+= game.score_away_q4
		team.display_Team()
		print "Average 1st Quater point total: ", Q1/16
		print "Average 2nd Quater point total: ", Q2/16
		print "Average 3rd Quater point total: ", Q3/16
		print "Average 4th Quater point total: ", Q4/16
		print "%d w %d l" % (wins, losses)


if __name__ == "__main__":
	main()
