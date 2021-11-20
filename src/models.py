import pygame as pg

class Game:
    def initialize(self):
        self.pg = pg.init()
        self.table = Table(8)
        self.gameDisplay = self.table.get_display()
        self.clock = pg.time.Clock()

    def quit(self):
        pg.quit()
        quit()

    def start_balls(self):
        self.balls = []
        self.colors = ["yellow", "blue"]
        width = int(self.table.internal_width/2)
        length = int(self.table.internal_length/2)
        for i in range(15):
            width -= 10
            length -= 10
            new_ball = Ball(width, length, 10, 0, self.colors[i%len(self.colors)])
            self.balls.append(new_ball)

    def display_balls(self):
        for ball in self.balls:
            ball.display(self.gameDisplay)

    def move_balls(self):
        for ball in self.balls:
            ball.move()

class Table:
    def __init__(self, size):
        self.internal_length = 5*224*(size/8)
        self.external_length = 5*262*(size/8)
        self.internal_width = 5*112*(size/8)
        self.external_width = 5*150*(size/8)

    def get_display(self):
        return pg.display.set_mode((self.external_length, self.external_width))

    def update_display(self):
        pg.display.update()


class Ball:
    def __init__(self, posx, posy, velx, vely, color):
        self.posx = posx
        self.posy = posy
        self.velx = velx
        self.vely = vely
        self.color = color
        self.friction = 0.1

    def move(self):
        if self.velx <= 0: self.velx = 0
        else: self.velx -= self.friction

        if self.vely <= 0: self.vely = 0
        else: self.vely -= self.friction

        self.posx += self.velx
        self.posy += self.vely

    def display(self, table_display):
        pg.draw.circle(table_display, self.color, (self.posx,self.posy), 6)
    


# class Hole:
#     def __init__(self, posx, posy):
#         self.posx = posx
#         self.posy = posy
        
    