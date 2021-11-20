import pygame as pg
from models import Game, Ball

game = Game()
game.initialize()
table = game.table
game_display = game.gameDisplay
clock = game.clock
game.start_balls()

gameExit = False
while not gameExit:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			gameExit = True

	
	game_display.fill("dark green")
	game.move_balls()
	game.display_balls()
	table.update_display()
	clock.tick(50)

game.quit()
