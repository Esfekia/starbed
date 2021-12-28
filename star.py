
import pygame
from pygame.sprite import Sprite

class Star(Sprite):
	"""A class to manage the star"""

	def __init__ (self, sb_game):
		"""Initialize the star and set its starting position."""
		super().__init__()

		self.screen = sb_game.screen
		###self.settings = sb_game.settings
		###self.screen_rect = sb_game.screen.get_rect()

		# Load the star image and get its rect.
		self.image = pygame.image.load('images/star.bmp')
		self.rect = self.image.get_rect()

		#Start each new star near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#Store the star's exact vertical position.
		self.y = float(self.rect.y)

