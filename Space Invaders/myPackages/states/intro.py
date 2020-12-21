from myPackages.states import edge_states

class Intro(edge_states.EdgeState):

	def __init__(self):

		super().__init__("ONE_PLAYER", "SPACE INVADERS", "One Player", "Two Players")

	def left_button_highlight(self):

		self.button_1_rect = self.button_1_text.get_rect(center=(275, 315))
		self.button_1_text = self.SMALL_FONT.render(self.button1_caption, True, self.LIGHT_BLUE)
		self.reset_right()
		self.lefthighlight = True

		if self.click:

			self.next = "ONE_PLAYER"
			self.fade_out(self.WIDTH, self.HEIGHT)
			self.state_reset()
			self.done = True

	def right_button_highlight(self):

		self.button_2_rect = self.button_2_text.get_rect(center=(515, 315))
		self.button_2_text = self.SMALL_FONT.render(self.button2_caption, True, self.LIGHT_BLUE)
		self.reset_left()

		self.righthighlight = True

		if self.click:
			self.next = "TWO_PLAYER"
			self.fade_out(self.WIDTH, self.HEIGHT)
			self.state_reset()
			self.done = True

	