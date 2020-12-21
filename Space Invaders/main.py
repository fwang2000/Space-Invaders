from myPackages.states import intro, game, end_lose, end_win, one_player, two_player
from myPackages import prepare, tools

def main():

	run = tools.Control(prepare.CAPTION)

	state_dict = {
		
		"INTRO": intro.Intro(),
		"TWO_PLAYER": two_player.Two_Player(),
		"ONE_PLAYER": one_player.One_Player(),
		"END_LOSE": end_lose.End_Lose(),
		"END_WIN": end_win.End_Win()
	}

	run.state_setup(state_dict, "INTRO")
	run.main()

if __name__ == '__main__':

	main()