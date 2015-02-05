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
		team.display_Team()
		games = nflgame.games(2014, home=team.get_Team(), away=team.get_Team())
		for game in games:
			if game.is_home(team.get_Team()):
				print game.nice_score()
				print game.score_home_q1
				print game.score_home_q2
				print game.score_home_q3
				print game.score_home_q4
			else:
				print game.nice_score()
				print game.score_away_q1
				print game.score_away_q2
				print game.score_away_q3
				print game.score_away_q4



if __name__ == "__main__":
	main()
