from random import randint
from soundandmusic import *
from  objekte import  *
import screen

class item(objekt):
    def __init__(self, pos_x, pos_y, size_x, size_y, direction, speed, points, color, frame):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self.direction = direction
        self.speed = speed
        self.points = points
        self.color = color
        self.frame = frame
        objekt.count_item += 1
    def acquire(self):
        self.pos_x = randint(50, (screen.W - self.size_x - 50))
        self.pos_y = randint(50, (screen.H - self.size_y - 50))
        return True

#Point and Speed
class item_point(item):
    def __init__(self, pos_x, pos_y, size_x, size_y, direction, speed, points, color, frame):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self.direction = direction
        self.speed = speed
        self.points = points
        self.color = color
        self.frame = frame


    def acquire_by_include(self, player_list, witch_item): #1. Point 2.Speed
        count = 0
        player_list_len = len(player_list)
        #Check Item include
        for x in range(player_list_len):
            if (player_list[x].draw_player().contains(self.draw_player())):
                #Point
                if (witch_item == 1):
                    self.acquire()
                    sound().blue_item()
                    count += 1
                    player_list[x].points += 1
                #Speed
                elif (witch_item == 2):
                    self.acquire()
                    sound().speed_item()
                    player_list[x].speed += 0.5
                    player_list[x].speed_point += 1
                    return True

                else: print("ERROR: False entry: acquire_by_include(self, player_list, witch_item) ->witch_item<-")

    def acquire(self):
        self.pos_x = randint(50, (screen.W - self.size_x - 50))
        self.pos_y = randint(50, (screen.H - self.size_y - 50))
        return True

class item_destroy(item):
    def __init__(self):
        self.pos_x = randint(0, (screen.W - 50))
        self.pos_y = randint(10, (screen.H - 50))
        self.size_x = 400
        self.size_y = 40
        self.direction = 2
        self.speed = 2
        self.color = (255, 255, 255)
        self.frame = 0


    def acquire(self):
        sound().destroy_item()
        self.pos_x = randint(0, (screen.W - 50))
        self.pos_y = randint(10, (screen.H - 50))
        self.size_x = randint(20, 550)
        self.size_y = randint(20, 550)
        self.speed = randint(1, 4)
        self.direction = self.random_direc()

    def bumping(self, player_list):
        for x in range(len(player_list)):
            if (player_list[x].draw_player().colliderect(self.draw_player())):
                #Player punish
                player_list[x].speed = 1
                player_list[x].speed_point = 0
                self.acquire()

    def random_direc(self):
        ran_number = randint(0, 9)
        while not ((ran_number == 2) or (ran_number == 4) or (ran_number == 6) or (ran_number == 8)):
            ran_number = randint(0, 9)

        return ran_number

    def start(self, player_list):
        self.draw_player()
        self.edge_change(player_list)
        self.move()
        return self

    #Exit Edge
    def edge_change(self, player_list):
        # Exit Edge
        x2 = self.pos_x + self.size_x
        y2 = self.pos_y + self.size_y
        player_list_len = len(player_list)

       # Rechts raus
        if ((x2) >= screen.W):
            cp = copy.copy(self)
            cp.pos_x = (((x2) - screen.W) - self.size_x)
            cp.draw_player()
            for x in range(player_list_len):
                if (player_list[x].draw_player().colliderect(cp.draw_player())):
                    # Player punisch
                    player_list[x].speed = 1
                    player_list[x].speed_point = 0
                    # DAMAGE
                    # Self
                    self.acquire()
        if (self.pos_x  >= screen.W):
            del cp
            self.pos_x = 0

        # Links raus
        if ((self.pos_x  <= 0)):
            cp = copy.copy(self)
            cp.pos_x = (screen.W + self.pos_x)
            cp.draw_player()
            for x in range(player_list_len):
                if (player_list[x].draw_player().colliderect(cp.draw_player())):
                    # Player punisch
                    player_list[x].speed = 1
                    player_list[x].speed_point = 0
                    #DAMAGE
                    # Self
                    self.acquire()
        if ((x2) <= 0):
            del cp
            self.pos_x = screen.W - x2 - 100

        # Oben raus
        if ((self.pos_y  <= 0)):
            cp = copy.copy(self)
            cp.pos_y = (screen.H + self.pos_y)
            cp.draw_player()
            for x in range(player_list_len):
                if (player_list[x].draw_player().colliderect(cp.draw_player())):
                    # Player punisch
                    player_list[x].speed = 1
                    player_list[x].speed_point = 0
                    #DAMAGE
                    # Self
                    self.acquire()
        if ((y2) <= 0):
            del cp
            self.pos_y = screen.H - self.size_y

        # unten raus
        if (y2 >= screen.H):
            cp = copy.copy(self)
            cp.pos_y = (((y2) - screen.H) - self.size_y)
            cp.draw_player()
            for x in range(player_list_len):
                if (player_list[x].draw_player().colliderect(cp.draw_player())):
                    # Player punisch
                    player_list[x].speed = 1
                    player_list[x].speed_point = 0
                    #DAMAGE
                    # Self
                    self.acquire()
        if (self.pos_y >= screen.H):
            del cp
            self.pos_y = 0

    def change_direction(self, direction):
        #TODO nach einer zufälling Zeit von 5 - 30 sec soll es die richtung wechseln
        if direction == 1:
            self.direction = 1
        elif direction == 2:
            self.direction = 2
        elif direction == 3:
            self.direction = 3
        elif direction == 4:
            self.direction = 4
        elif direction == 5:
            self.direction = 5
        elif direction == 6:
            self.direction = 6
        elif direction == 7:
            self.direction = 7
        elif direction == 8:
            self.direction = 8
        elif direction == 9:
            self.direction = 9

class item_fiep(item):
    def __init__(self):
        self.pos_x = randint(0, screen.W)
        self.pos_y =  randint(0, screen.H)
        self.size_x = 50
        self.size_y = 25
        self.direction = 5
        self.color = (255, 255, 0)
        self.frame = 0

    def acquire_by_include(self, player_list, witch_item):
        for x in range(len(player_list)):

            if (player_list[x].draw_player().contains(self.draw_player())):
                sound().yellow_item()
                for x_2 in range(len(player_list)):
                    if not x == x_2:
                        player_list[x_2].pos_x = randint(0, screen.W)
                        player_list[x_2].pos_y = randint(0, screen.H)
                self.acquire()