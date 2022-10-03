import copy
import pygame
import screen

class objekt:
    count_player = 0
    player_array = []
    count_item = 0
    x_pos = 0
    zeichnug = []

    # [pos_x[0], pos_y[1], size_x[2], size_y[3], direction[4], speed[5], points[6], color[7],Frame[8]
    def __init__(self, pos_x, pos_y, size_x, size_y,direction,b_speed, points, color,frame):
        self.pos_x = pos_x
        self.pos_y = size_y
        self.size_x = size_x
        self.size_y = size_y
        self.direction = direction
        self.b_speed = b_speed
        self.points = points
        self.color = color
        self.frame = frame

    def draw_player(self):
        self = pygame.draw.rect(screen.screen, self.color, [self.pos_x, self.pos_y, self.size_x,self.size_y], self.frame)
        return self

    def move(self):
        if self.direction == 2:
            self.pos_y += self.speed
        elif self.direction == 4:
            self.pos_x -= self.speed
        elif self.direction == 5:
            self.pos_x = self.pos_x
            self.pos_y = self.pos_y
        elif self.direction == 6:
            self.pos_x += self.speed
        elif self.direction == 8:
            self.pos_y -= self.speed

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
        if (self.pos_x  >= screen.W):
            del cp
            self.pos_x = 0

        #Left out
        if ((self.pos_x  <= 0)):
            cp = copy.copy(self)
            cp.pos_x = (screen.W + self.pos_x)
            cp.draw_player()
        if ((x2) <= 0):
            del cp
            self.pos_x = screen.W - x2 - 100

        #Out above
        if ((self.pos_y  <= 0)):
            cp = copy.copy(self)
            cp.pos_y = (screen.H + self.pos_y)
            cp.draw_player()
        if ((y2) <= 0):
            del cp
            self.pos_y = screen.H - self.size_y

        #Out below
        if (y2 >= screen.H):
            cp = copy.copy(self)
            cp.pos_y = (((y2) - screen.H) - self.size_y)
            cp.draw_player()
        if (self.pos_y >= screen.H):
            del cp
            self.pos_y = 0

    def start(self):
        self.draw_player()
        self.edge_change()
        self.move()
        return self

    def change_x_pos(self, sign, x):
        if sign:
            self.pos_x += x
        else:
            self.pos_x -= x

    def change_y_pos(self, sign, x):
        if sign:
            self.pos_y += x
        else:
            self.pos_y -= x

    def pos(self):
        X2 = (self.pos_x + self.size_x)
        Y2 = (self.pos_y + self.size_y)
        pos = [int(self.pos_x), int(self.pos_y), int(X2), int(Y2), self]
        return pos

    def opponent_bumping(self, other):
        if (objekt.bumping(self, other)):
            # haptisches feedback for withe
            if not self.joystick == None:
                self.joystick.rumble(1,1,100)
            if not other.joystick == None:
                other.joystick.rumble(1,1,100)
            #same direction
            if (((self.direction == 2) and (other.direction == 2))):
                if (self.other_over(other)):
                    self.change_y_pos(True, objekt.speed(self, other))
                if (self.other_under(other)):
                    other.change_y_pos(True, objekt.speed(self, other))
            if (((self.direction == 6) and (other.direction == 6))):
                if (self.other_left(other)):
                    self.change_x_pos(True, objekt.speed(self, other))
                if (self.other_right(other)):
                    other.change_x_pos(True, objekt.speed(self, other))
            if (((self.direction == 8) and (other.direction == 8))):
                if (self.other_over(other)):
                    other.change_y_pos(False, objekt.speed(self, other))
                if (self.other_under(other)):
                    self.change_y_pos(False, objekt.speed(self, other))
            if (((self.direction == 4) and (other.direction == 4))):
                if (self.other_left(other)):
                    other.change_x_pos(False, objekt.speed(self, other))
                if (self.other_right(other)):
                    self.change_x_pos(False, objekt.speed(self, other))
            #opposeite direction
            if (((self.direction == 6) and (other.direction == 4))):
                self.change_x_pos(False, objekt.speed(self, other))
                other.change_x_pos(True, objekt.speed(self, other))
            if (((self.direction == 4) and (other.direction == 6))):
                self.change_x_pos(True,objekt.speed(self, other))
                other.change_x_pos(False, objekt.speed(self, other))
            if (((self.direction == 2) and (other.direction == 8))):
                self.change_y_pos(False, objekt.speed(self, other))
                other.change_y_pos(True, objekt.speed(self, other))
            if (((self.direction == 8) and (other.direction == 2))):
                self.change_y_pos(True, objekt.speed(self, other))
                other.change_y_pos(False, objekt.speed(self, other))

            #not the same direction
            if ((other.direction == 4) or (other.direction == 6)):
                if(objekt.other_over(self,other) and (self.direction == 8)):
                    other.change_y_pos(False, (10))
                if(objekt.other_under(self, other) and (self.direction == 2)):
                    other.change_y_pos(True, (10))
                if(objekt.other_right(self, other)):
                    self.change_x_pos(False, (10))

            if ((other.direction == 8) or (other.direction == 2)):
                if(objekt.other_left(self, other) and (self.direction == 4)):
                    other.change_x_pos(False, (10))
                if(objekt.other_right(self, other) and (self.direction == 6)):
                    other.change_x_pos(True, (10))
#________________________________________
#Funktionen für bumping
#_-------------------------------------
    def bumping(self, other):
        if ((self.pos_x2()) >= other.pos_x) and (
                self.pos_x <= (other.pos_x2())) and (
                self.pos_y2() >= other.pos_y) and (
                self.pos_y <= (other.pos_y2())):
            return True
        else:
            return False
    def speed(self,other):
        if(self.speed > other.speed):
            return (self.speed * 10)
        else:
            return (other.speed * 10)

    def other_over(self, other):
        if ((other.pos_y2() - self.speed) <= self.pos_y):
            return True
        else:
            return False
    def other_under(self, other):
        if (((other.pos_y + self.speed) >= self.pos_y2())):
            return True
        else:
            return False
    def other_left(self, other):
        if ((other.pos_x2() - self.speed) <= self.pos_x):
            return True
        else:
            return False
    def other_right(self, other):
        if ((other.pos_x + self.speed) >= self.pos_x2()):
            return True
        else:
            return False