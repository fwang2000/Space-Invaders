from myPackages.states import edge_states
import pygame
import sys

class End(edge_states.EdgeState):

	def __init__(self, title_caption):

		super().__init__("INTRO", title_caption, "Replay", "Quit")

	def right_button_highlight(self):

		self.button_2_rect = self.button_2_text.get_rect(center=(515, 315))
		self.button_2_text = self.SMALL_FONT.render(self.button2_caption, True, self.LIGHT_BLUE)
		self.reset_left()

		self.righthighlight = True

		if self.click:

			pygame.quit()
			sys.exit(0)
