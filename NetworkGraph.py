import pygame
import simpy

class NetworkGraph(pygame):
	def __init__(self, env, screen, display, image, event):
		self.env		= env
		self.screen		= screen
		self.display	= display
		self.image		= image
		self.event		= event

	def run(self):
		while True:
			for event in self.event.get():
				if event.type == pygame.QUIT: sys.exit()
			black = 0, 0, 0
			self.screen.fill(black)
			#<Code goes here>
			self.display.flip()
			yield self.env.timeout(1)