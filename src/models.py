import pygame as pg
import math

class Game:
    def initialize(self):
        pg.init()
        self.table = Table(8)
        self.game_display = self.table.get_display()
        self.game_display.fill("dark green")
        self.clock = pg.time.Clock()
        self.set_limits()

    def quit(self):
        pg.quit()
        quit()

    def set_limits(self):
        width = self.table.internal_width
        length = self.table.internal_length
        rect = pg.Rect(width, length, width, length)
        pg.draw.rect(self.game_display, "black", rect)

    def start_balls(self):
        self.balls = []
        self.colors = ["yellow", "blue", "red"]
        width = int(self.table.internal_width/2)
        length = int(self.table.internal_length/2)
        # for i in range(15):
        #     width -= 10
        #     length -= 10
        #     new_ball = Ball(width, length, 10, 0, self.colors[i%len(self.colors)])
        #     self.balls.append(new_ball)
        new_ball = Ball(length, width, 10, 25, "red")
        self.balls.append(new_ball)
        # new_ball = Ball(width + 300, length, -10, 0, "green")
        # self.balls.append(new_ball)

    def display_balls(self):
        for ball in self.balls:
            ball.display(self.game_display)

    def move_balls(self):
        for ball in self.balls:
            self.table.reflect_ball(ball)
            ball.move()

    def update_display(self):
        self.set_limits()
        pg.display.update()


class Table:
    def __init__(self, size):
        self.internal_length = 5*224*(size/8)
        self.external_length = 5*262*(size/8)
        self.internal_width = 5*112*(size/8)
        self.external_width = 5*150*(size/8)        

    def get_display(self):
        return pg.display.set_mode((self.external_length, self.external_width))

    def reflect_ball(self, ball):
        if self.does_reflect_ball(ball):
            ball.velx *= -1
            ball.vely *= -1

    def does_reflect_ball(self, ball):
        if ball.posx < 0 or ball.posx > self.external_length:
            return True
        if ball.posy < 0 or ball.posy > self.external_width:
            return True
        return False


class Ball:
    def __init__(self, posx, posy, velx, vely, color):
        self.radius = 10
        self.posx = posx
        self.posy = posy
        self.velx = velx
        self.vely = vely
        self.color = color
        self.friction = 0

    def move(self):
        if self.velx < 0: self.velx += self.friction
        elif self.velx > 0: self.velx -= self.friction

        if self.vely < 0: self.vely += self.friction
        elif self.vely > 0: self.vely -= self.friction

        if(self.velx < 0.2 and self.velx > -0.2) : self.velx = 0
        if(self.vely < 0.2 and self.vely > -0.2) : self.vely = 0

        self.posx += self.velx
        self.posy += self.vely

    def display(self, game_display):
        pg.draw.circle(game_display, self.color, (self.posx,self.posy), self.radius)

    def does_collide(self, other_ball):
        x1 = self.posx
        x2 = other_ball.posx
        y1 = self.posy
        y2 = other_ball.posy

        distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        if distance <= self.radius:
            return True
        else:
            return False

    def collide(self, other_ball):
        self.velx = -1*self.velx 
        self.vely = -1*self.vely
        other_ball.velx = -1*other_ball.velx
        other_ball.vely = -1*other_ball.vely
    

# class Hole:
#     def __init__(self, posx, posy):
#         self.posx = posx
#         self.posy = posy
        
    