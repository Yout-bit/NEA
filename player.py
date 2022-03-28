from pygame import Surface, Rect
from pygame.math import Vector2 

centres = [Vector2(0,0), Vector2(0,0), Vector2(0,0), Vector2(0,0)]


class Player():
    def __init__(self, size, move_speed, start_x, start_y, level, name, conn, start_rot):
        super().__init__()
        self.conn = conn
        self.dir = Vector2(0,0)
        self.wish_dir = Vector2()
        self.level = level
        self.move_speed = move_speed
        self.size = int(size)
        self.name = str(name)
        self.start_x = start_x
        self.start_y = start_y
        self.rect = Rect(start_x, start_y, size, size)
        self.fire = False
        self.dead = False
        self.ready = False
        self.start_rot = start_rot
        self.score = 0

    #Checks whether the player can be moved by the input vector
    def detect_collision(self, vec):
        width_modifier = (self.size /2) -1 
        edge = Vector2(vec.x * (width_modifier) , vec.y * (width_modifier))   
        corner_1 = Vector2()
        corner_2 = Vector2() 
        if abs(vec.x) > 0:
            corner_1 = Vector2(self.rect.center) + edge + Vector2(0, width_modifier) + vec * self.move_speed
            corner_2 = Vector2(self.rect.center) + edge - Vector2(0, width_modifier) + vec * self.move_speed
        if abs(vec.y) > 0:
            corner_1 = Vector2(self.rect.center) + edge + Vector2(width_modifier, 0) + vec * self.move_speed
            corner_2 = Vector2(self.rect.center) + edge - Vector2(width_modifier, 0) + vec * self.move_speed

        return self.level.get_grid_value(corner_1.xy) == "#" or self.level.get_grid_value(corner_2.xy) == "#"

    #Checks if the centre of the player lies within a players width of the centre of the other player
    def detect_player(self):
        for i in centres:
            if (centres.index(i) != (int(self.name)) and i != Vector2(0,0)):
                i = Vector2(i)
                difference = Vector2((i.x - self.rect.centerx), (i.y - self.rect.centery))
                if (abs(difference.x) <= 80 and abs(difference.y == 0))  or (abs(difference.y) <=80 and abs(difference.x == 0)):
                    #if not self.detect_collision(self.dir):
                    self.dir = difference.normalize() * -1

    #Assigns the wish direction based on the input and checks if the player fires
    def input(self, inputs):
        self.wish_dir = Vector2(-1,0) if inputs[2] == "1" else self.wish_dir
        self.wish_dir = Vector2(1,0) if inputs[3] == "1"else self.wish_dir

        self.wish_dir = Vector2(0,1) if inputs[1] == "1" else self.wish_dir
        self.wish_dir = Vector2(0,-1) if inputs[0] == "1" else self.wish_dir
        if self.wish_dir.magnitude() != 0:
            self.wish_dir.normalize_ip()

        self.fire = False 
        if inputs[4] == "1":
            if self.dir.magnitude() != 0:
                self.fire = True
            self.ready = True


    #Normalise the direction vector then checks the wish direction does not push the player into a wall and is not opposite to the current direction. 
    #Then tests for collision with other players
    def update(self, output):
        if self.conn != False:
            if len(centres) - 1 < int(self.name):
                centres.append(self.rect.center)
            centres[int(self.name)] = self.rect.center
            print (self.conn)
            try:
                reply = self.conn.recv(4096).decode('utf-8')
                self.conn.sendall(str.encode(output)) 
            except ConnectionResetError:
                self.conn = False
                reply = "00000"
      
            if not self.dead:
                self.input(reply)
                if self.dir.magnitude() != 0:
                    normal_dir = self.dir.normalize()
                else:
                    normal_dir = Vector2(0,0)  

                #If the dot product of the 2 vectors = -1, they are opposite.
                if self.wish_dir.dot(normal_dir) != -1 and not self.detect_collision(self.wish_dir):
                    self.dir = self.wish_dir
                
                self.detect_player()
                if not self.detect_collision(self.dir):
                    self.rect.move_ip(self.dir * self.move_speed)

    #Resets all attributes to their initial value
    def reset(self, level):
        if not self.dead:
            self.score += 1
        self.dir = Vector2(0,0)
        self.wish_dir = Vector2()
        self.level = level
        self.rect = Surface((self.size, self.size)).get_rect()
        self.rect = Rect(self.start_x, self.start_y, self.size, self.size)
        self.fire = False
        self.dead = False
        self.ready = False

    #Temporarily stops the player from performing inputs and stops them colliding with shots 
    def destroy(self):
        self.dead = True
        self.rect.move_ip(999-self.rect.centerx, 999-self.rect.centery)

    #Returns the centre of the player
    def get_center(self):
        return Vector2(self.rect.center)

    #Returns the orientation of the player
    def get_rot(self):
        if self.dir == (0, 0):
            return self.start_rot
        elif self.dir == (0, -1):
            return "N" 
        elif self.dir == (1, 0):
            return "E"
        elif self.dir == (0, 1):
            return "S"
        else:
            return "W"

    #Gets a vector perpendicular to the given vector
    def perp(a):
        b = Vector2(0,0)
        b.x = a.y
        b.y = a.x
        return b

    #Returns the front point of the player (Used for projectile starting pos) 
    def get_front(self):
        return (self.rect.center + self.dir * (self.size / 2))

    #Returns position of the player
    def get_pos(self):
        return self.rect.left,  self.rect.top

    #Returns a Rect object that is the hitbox
    def get_hitbox(self):
        backrect = None
        if self.dir != (0,0):
            backrect = self.rect.copy()
            backrect.width -= (abs(self.dir.x) * 64)
            backrect.height -= (abs(self.dir.y) *64)
            backrect.top += 64 * (abs(self.dir.y) - self.dir.y) / 2 
            backrect.left += 64 * (abs(self.dir.x) - self.dir.x) / 2
        return backrect
    
    
