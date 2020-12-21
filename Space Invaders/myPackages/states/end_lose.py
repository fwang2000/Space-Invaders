from myPackages.states import end

class End_Lose(end.End):

	def __init__(self):

		super().__init__("Game Over")