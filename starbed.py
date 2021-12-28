import sys
import pygame

from settings import Settings
from star import Star

class StarBed:
	"""Overall class to manage assets and behavior."""

	def __init__(self):
		"""Initialize the code and create the resources."""

		pygame.init()

		self.settings = Settings()

		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Star Bed")

		self.star = Star(self)

	def run_game(self):
		"""Start the main loop for the code."""
		while True:
			
			# Watch for keyboard event to quit.
			self._check_quit()	

			# Redraw the screen during each pass through the loop.
			self._update_screen()

	def _check_quit(self):
		"""Respond to keypress to quit."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.key == pygame.K_q:
				sys.exit()

	def _update_screen(self):
		"""Update images on the screen and flip to the new screen."""
		self.screen.fill (self.settngs.bg_color)
		self.star.blitme()

		pygame.display.flip()

if __name__ == '__main__':
	#Make a new game instance, and run the game.
	sb = StarBed()
	sb.run_game()