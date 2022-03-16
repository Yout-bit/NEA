from _thread import start_new_thread
from random import randint
import socket as sock


from player import Player
from grid import Server_Grid
from projectile import Projectile 


#Resets all the players, projectiles and map
def setup(players, shots):
    mapnum = randint(0,7)
    level = Server_Grid(mapnum)
    for player in  players:
        player.reset(level)
    for shot in shots:
        shot.destroy()
        shot.countdown = 0
        shot.level = level

    return players, shots, mapnum

#Takes a player and projectile and checks first if the projectile hits the players hitbox. If so, it destroys both the player and projectile.
#Then, if it didn't hit the hitbox, it checks if the projectile hits the player. If so, it destroys the projectile.  
def check_hit(player, projectile):
    hitbox = player.get_hitbox()
    if hitbox != None and not player.dead:
        if hitbox.collidepoint(projectile.center):
            projectile.destroy()
            player.destroy()
        elif player.rect.collidepoint(projectile.center):
            projectile.destroy()

#Creates a player with hard coded starting value based on which number player they are
def create_player(players, number, conn, level):
    if number == 0:
        players.append(Player(80, 5, 80, 80, level, number, conn, "S"))
    elif number == 1:
        players.append(Player(80, 5, 720, 560, level, number, conn, "N"))
    elif number == 2:
        players.append(Player(80, 5, 80, 560, level, number, conn, "E"))
    else:
        players.append(Player(80, 5, 720, 80, level, number, conn, "W"))
    return players

#Takes an integer, then returns a 3 digit string of that number
def threefigs(number):
    number = str(int(number))
    while len(number) < 3:
        number = "0" + number 
    return number


mapnum = randint(0,7)
level = Server_Grid(mapnum)
players = []
shots = []

#Main gameplay loop
def threaded_main(mapnum):
    #Uses 3 global variables so both threads can manipulate them at the same time
    global players
    global shots
    game = "Menu"
    buffer = 120

    while True:
        if game == "Menu":
            #Adds the [Gamestate, No. of Player, Mapnumber] to the SendData 
            SendData = "0" + str(len(players)) + str(mapnum)
            ready = 0
            #Adds a little buffer before the players can ready in prevent accidental readying at the start of a new game or end of an old one
            if buffer > 0:
                buffer -= 1
            for player in players:
                #for each player, adds a 1/0 if they are Ready/Not to the SendData
                if player.ready and buffer == 0:
                    SendData += "1"
                    #Counts the number of ready players each frame to know when to start the game 
                    ready += 1 
                else:
                    SendData += "0"
                SendData += str(player.score)
            #If there is more than 0 players and the number of ready players = number of players, the game starts
            game = "Playing" if (len(players) != 0) and ready == len(players) else game
            
            
        if game == "Playing":
            #Adds the [Gamestate, No. of Player, Mapnumber] to the SendData 
            SendData = "1" + str(len(players)) + str(mapnum)
            dead = 0
            for i in range(len(players)):
                if players[i].dead:
                    #Counts the number of dead players each frame to know when to end the game
                    dead += 1 
                for j in range(len(shots)):
                    if i != j:
                        #Checks every projectile against every player for a hit except a players own projectile
                        check_hit(players[i], shots[j])
                for j in (players[i].get_pos() + shots[i].get_pos()):
                    #For each player and their projectile, takes the position and converts it to a 3 digit string then adds it to SendData
                    SendData += threefigs(j)
                #Adds each player's rotation and adds it to SendData
                SendData += players[i].get_rot()
            #If all but 1 players are dead, it resets the players and projectiles, randomises a new mapumn and restes the buffer as players often held the fire button. 
            #Then returns to the menu 
            if dead == len(players) - 1:
                players, shots, mapnum = setup(players, shots)
                buffer = 300
                game = "Menu"

        #Updates both the player's and projectile's position
        for player in players:
            player.update(SendData)
        for shot in shots:
            shot.update()


#Starts the main gameplay loop 
start_new_thread(threaded_main, (mapnum,))

#Sets up socket object
ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 5555

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))


print('Waiting for a Connection on: \nHost: ' + host + ', Port: ' + str(port))
ServerSocket.listen(5)


#Handling new connections
ClientCount= 0
while ClientCount != 4:
    Client, address = ServerSocket.accept()
    Client.sendall(str.encode("Welcome to the server"))
    players = create_player(players, ClientCount, Client, level)
    shots.append(Projectile(15, players[ClientCount], level))
    ClientCount += 1
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    print('Client Number: ' + str(ClientCount))

sock.close()
