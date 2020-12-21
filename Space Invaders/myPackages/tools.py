import pygame

class Control(object):

	'''
	Class that controls the entire project. Runs the game loop, contains
	the finite state dictionary and switches between the states. Logic to
	flip states is also here
	'''

	def __init__(self, caption):

		self.done = False
		self.state_dict = {}
		self.state_name = None
		self.state = None
		self.caption = caption

	def state_setup(self, state_dict, state_name):

		self.state_dict = state_dict
		self.state_name = state_name
		self.state = self.state_dict[self.state_name]
		
	def update(self):

		if self.state.quit:

			self.done = True

		elif self.state.done:

			self.state.done = False
			self.change_state()

		self.state.update()

	def change_state(self):

		self.state_name = self.state.next
		self.state = self.state_dict[self.state_name]

	def event_loop(self):

		self.state.get_event()

	def main(self):

		while not self.done:

			self.event_loop()
			self.update()
			pygame.display.update()


class _State(object):

	'''
	Abstract class for States. All states inherit this class.
	get_event and update must be overloaded
	'''

	def __init__(self):

		self.done = False
		self.quit = False
		self.next = None
		self.screen = pygame.display.get_surface()

	def get_event(self):

		raise NotImplementedError("Must be overloaded in child class")

	def update(self):

		raise NotImplementedError("Must be overloaded in child class")

	def _getscreen(self):

		return self.screen