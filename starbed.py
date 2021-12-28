import sys
import pygame
from random import randint
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

		self.stars = pygame.sprite.Group()
		self._create_star_field()

		
			

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
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)

	def _check_keydown_events(self,event):
		"""Respond to key presses."""
		if event.key == pygame.K_q:
				sys.exit()

	def _create_star_field(self):
		"""Create a field of stars."""

		#Create a star and find the number of stars in a row.
		#Spacing between each star is equal to one star width.
		star = Star(self)
		star_width, star_height = star.rect.size
		available_space_x = self.settings.screen_width -(2*star_width)
		number_stars_x = available_space_x // (2*star_width)

		#Determine the number of rows of aliens that fit on the screen.

		available_space_y = self.settings.screen_height - (2* star_height)
		number_rows = available_space_y // (2*star_height)

		#Create the bed of stars.
		for row_number in range(number_rows):
			for star_number in range (number_stars_x):
				self._create_star(star_number, row_number)
	
	def _create_star(self, star_number, row_number):
		"""Create a star and place it in the row."""
		random_number = randint(-10, 10)
		star = Star(self)
		star_width, star_height = star.rect.size
		star.x = star_width + random_number + 2*star_width*star_number
		star.rect.x = star.x 
		star.rect.y = star.rect.height + random_number + 2*star.rect.height * row_number
		
		#Randomize the stars further
		star.rect.x += randint(-5, 5)
		star.rect.y += randint(-5, 5)

		self.stars.add(star)

	def _update_screen(self):
		"""Update images on the screen and flip to the new screen."""
		self.screen.fill (self.settings.bg_color)
		self.stars.draw(self.screen)

		pygame.display.flip()

if __name__ == '__main__':
	#Make a new game instance, and run the game.
	sb = StarBed()
	sb.run_game()