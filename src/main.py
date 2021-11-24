import pygame as pg
from models import Game

game = Game()
game.initialize()
clock = game.clock
game.start_balls()

gameExit = False
while not gameExit:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			gameExit = True


	game.move_balls()
	game.game_display.fill("dark green")
	game.display_balls()
	game.update_display()
	clock.tick(50)

game.quit()
