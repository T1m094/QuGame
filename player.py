import random
import item
from objekte import *
from random import randint
from soundandmusic import *

class player(objekt):
    def __init__(self):
        self.name = "Test"

        #Size Quadrat
        self.size_x = 100 #Default 100 TODO
        self.size_y = 100 #Default 100 TODO

        #Position and Speed at start
        #Player 1
        if objekt.count_player == 0:
            # Player
            self.pos_x = (screen.W/2) - 300
            self.pos_y = (screen.H / 2) - 50
            self.direction = 4
            self.color = (255, 0, 0)
            #Speed Item
            self.speed_item_pos_x = (screen.W/2) + 235
            self.speed_item_pos_y = (screen.H / 2) - 15
        #Player 2
        elif objekt.count_player == 1:
            # Player
            self.pos_x = (screen.W/2) + 200
            self.pos_y = (screen.H / 2) - 50
            self.direction = 6
            self.color = (0, 255, 0)
            # Speed Item
            self.speed_item_pos_x = (screen.W/2) - 265
            self.speed_item_pos_y = (screen.H / 2) - 15
        #Player 3
        elif objekt.count_player == 2:
            # Player
            self.pos_x = (screen.W/2) - 50
            self.pos_y = (screen.H/2) - 300
            self.direction = 8
            self.color = (255, 0, 255)
            # Speed Item
            self.speed_item_pos_x = (screen.W/2) - 15
            self.speed_item_pos_y = (screen.H/ 2) + 235
        #Player 4
        elif objekt.count_player == 3:
            # Player
            self.pos_x = (screen.W/2) - 50
            self.pos_y = (screen.H/2) + 200
            self.direction = 2
            self.color = (0, 255, 255)
            # Speed Item
            self.speed_item_pos_x = (screen.W/2) - 15
            self.speed_item_pos_y = (screen.H/ 2) - 265

        #For all player
        self.frame = 10
        self.points = 0
        self.speed = 1
        self.speed_point = 0
        self.max_speed = 4.5
        self.id = objekt.count_player
        self.item_s = item.item_point(self.speed_item_pos_x, self.speed_item_pos_y, 30, 30, 0, 0, 0, self.color, 0)

        #Schrift
        self.font = pygame.font.SysFont(None, 50)

        objekt.count_player += 1
        objekt.player_array.append(self)

    def start(self):
        self.draw_player()
        self.edge_change()
        self.move()
        #Speeditem
        if (self.speed < self.max_speed):
            self.item_s.start()
            self.item_s.start()
            self.item_s.acquire_by_include([self], 2)
        self.print_speedpoints()

        return self

    def pos_x(self):
        return self.pos_x

    def pos_y(self):
        return self.pos_x

    def pos_x2(self):
        x2 = self.pos_x + self.size_x

        return x2

    def pos_y2(self):
        y2 = self.pos_y + self.size_y
        return y2

    def direction(self):
        return self.direction

    def speed(self):
        return self.speed

    def change_direction(self, direction):
        if direction == 2:
            self.direction = 2
        elif direction == 4:
            self.direction = 4
        elif direction == 5:
            self.direction = 5
        elif direction == 6:
            self.direction = 6
        elif direction == 8:
            self.direction = 8

    #Exit Edge
    def edge_change(self):

        # Exit Edge
        x2 = self.pos_x + self.size_x
        y2 = self.pos_y + self.size_y

       #Right out
        if ((x2) >= screen.W):
            cp = copy.copy(self)
            cp.pos_x = (((x2) - screen.W) - self.size_x)
            cp.draw_player()
            if ((self.speed < self.max_speed) and (self.item_s.acquire_by_include([cp], 2))):
                self.speed_point = cp.speed_point
                self.speed = cp.speed
        if (self.pos_x  >= screen.W):
            del cp
            self.pos_x = 0

        #Left out
        if ((self.pos_x  <= 0)):
            cp = copy.copy(self)
            cp.pos_x = (screen.W + self.pos_x)
            cp.draw_player()
            if ((self.speed < self.max_speed) and (self.item_s.acquire_by_include([cp], 2))):
                self.speed_point = cp.speed_point
                self.speed = cp.speed
        if ((x2) <= 0):
            del cp
            self.pos_x = screen.W - x2 - 100

        #Out above
        if ((self.pos_y  <= 0)):
            cp = copy.copy(self)
            cp.pos_y = (screen.H + self.pos_y)
            cp.draw_player()
            if ((self.speed < self.max_speed) and (self.item_s.acquire_by_include([cp], 2))):
                self.speed_point = cp.speed_point
                self.speed = cp.speed
        if ((y2) <= 0):
            del cp
            self.pos_y = screen.H - self.size_y

        #Out below
        if (y2 >= screen.H):
            cp = copy.copy(self)
            cp.pos_y = (((y2) - screen.H) - self.size_y)
            cp.draw_player()
            if ((self.speed < self.max_speed) and (self.item_s.acquire_by_include([cp], 2))):
                self.speed_point = cp.speed_point
                self.speed = cp.speed
        if (self.pos_y >= screen.H):
            del cp
            self.pos_y = 0

    # Behavior
    def acquire_item_by_bumping(self, other_pos):
        if (((self.pos_x + self.size_x) > other_pos[0]) and (self.pos_x < (other_pos[0] + other_pos[2])) and (
                (self.pos_y + self.size_y) > other_pos[1]) and (self.pos_y < (other_pos[1]) + other_pos[3])):
            self.points += 1
            return True

    def print_speedpoints(self):
        #Point State
        self.point_view = self.font.render(str(self.points), True, (255, 255, 255))

        # Speed display
        distance = 0
        if self.id == 0:
            screen.screen.blit(self.point_view, (30, (screen.H - 50)))
            for i in range(self.speed_point):
                pygame.draw.rect(screen.screen, self.color, pygame.Rect(2 + distance, (screen.H - 15), 10, 10))
                distance += 10
            pygame.draw.rect(screen.screen, (80, 80, 80), [1, (screen.H - 18), 73, 16], 2)

        elif self.id == 1:
            screen.screen.blit(self.point_view, ((screen.W - 50), (screen.H - 50)))
            for i in range(self.speed_point):
                pygame.draw.rect(screen.screen, self.color, pygame.Rect((screen.W - 73) + distance, (screen.H - 15), 10, 10))
                distance += 10
            pygame.draw.rect(screen.screen, (80, 80, 80), [(screen.W - 74), (screen.H - 18), 73, 16], 2)

        elif self.id == 2:
            screen.screen.blit(self.point_view, (30,  50))
            for i in range(self.speed_point):
                pygame.draw.rect(screen.screen, self.color, pygame.Rect(2 + distance, 5, 10, 10))
                distance += 10
            pygame.draw.rect(screen.screen, (80, 80, 80), [0, 2, 73, 16], 2)

        elif self.id == 3:
            screen.screen.blit(self.point_view, (screen.W - 50, 50))
            for i in range(self.speed_point):
                pygame.draw.rect(screen.screen, self.color, pygame.Rect((screen.W - 82) + distance, 5, 10, 10))
                distance += 10
            pygame.draw.rect(screen.screen, (80, 80, 80), [(screen.W - 85), 2, 73, 16], 2)

#Player for Mainmenue
class simple_player(objekt):
    def __init__(self):
        # Player
        self.pos_x = randint(50, (screen.W - 50))
        self.pos_y = randint(50, (screen.H - 50))
        self.direction = self.random_direc()
        self.color = (randint(0, 255),randint(0, 255),randint(0, 255))

        self.size_x = 100
        self.size_y = 100
        self.frame = 8
        self.speed = random.uniform(0.5, 2.2)

    def random_direc(self):
        ran_number = randint(0, 9)
        while not ((ran_number == 2) or (ran_number == 4) or (ran_number == 6) or (ran_number == 8)):
            ran_number = randint(0, 9)
        return ran_number