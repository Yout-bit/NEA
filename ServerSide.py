from asyncore import read
import socket
import os
from _thread import *
import sys
import pygame
from pygame.font import match_font
from pygame.key import *
from pygame.locals import *
import math
import random

from player import Player
from collisions import Collisions
from projectile import Projectile 


SCREEN_WIDTH = 880
SCREEN_HEIGHT = 720

Colours = {
    "BLUEY" : (144, 137, 218),
    "GREY"  : (153, 170, 181),
    "DARK"  : (44, 47, 51),
    "BLUE"  : (0, 0, 255),
    "RED"   : (255, 0, 0),
    "GREEN" : (0, 255, 0),
    "BLACK" : (0, 0, 0),
    "WHITE" : (255, 255, 255),
    "SHADOW": (103, 120, 131)
    }


def setup(players, shots):
    mapnum = random.randint(0,7)
    level = Collisions(mapnum)
    for player in  players:
        player.reset(level)
    for shot in shots:
        shot.destroy()
        shot.countdown = 0

    return players, shots, mapnum

def check_hit(player, projectile):
    hitbox = player.get_hitbox()
    if hitbox != None and not player.dead:
        if hitbox.collidepoint(projectile.center):
            projectile.destroy()
            player.destroy()
        elif player.rect.collidepoint(projectile.center):
            projectile.destroy()

def create_player(players, number, conn, level):
    if number == 0:
        players.append(Player(80, 5, 80, 80, level, number, conn))
    elif number == 1:
        players.append(Player(80, 5, 720, 560, level, number, conn))
    elif number == 2:
        players.append(Player(80, 5, 80, 560, level, number, conn))
    else:
        players.append(Player(80, 5, 720, 80, level, number, conn))
    return players

def threefigs(number):
    number = str(int(number))
    while len(number) < 3:
        number = "0" + number 
    return number


mapnum = random.randint(0,7)
level = Collisions(mapnum)
players = []
shots = []

#Data to send to cliants:
#[Game State(Menu/Game - 0/1), NumOfPlayers, Map, P1pos, S1pos, P1dir (rept for all players)]

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)

def threaded_main(mapnum):
    global players
    global shots
    game = "Menu"
    buffer = 120

    while True:
        if game == "Menu":
            x = "0" + str(len(players)) + str(mapnum)
            ready = 0
            while buffer > 0:
                buffer -= 1
            for player in players:
                if player.ready:
                    x += "1"
                    ready += 1 
                else:
                    x += "0"
            game = "Playing" if (len(players) != 0) and ready == len(players) else game
            
        if game == "Playing":
            dead = 0
            x = "1" + str(len(players)) + str(mapnum)
            for i in range(len(players)):
                if players[i].dead:
                    dead += 1 
                for j in range(len(shots)):
                    if i != j:
                        check_hit(players[i], shots[j])
                for j in (players[i].get_pos() + shots[i].get_pos()):
                    x += threefigs(j)
                x += players[i].get_rot()
            if dead == len(players) - 1:
                players, shots, mapnum = setup(players, shots)
                buffer = 120
                game = "Menu"
        for player in players:
            player.update(x)
        for shot in shots:
            shot.update()



start_new_thread(threaded_main, (mapnum,))


#Handelling new connections
ThreadCount = 0
while ThreadCount != 4:

    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    Client.send(str.encode('Welcome to the Servern'))
    #start_new_thread(threaded_client, (Client, str(ThreadCount)))
    players = create_player(players, ThreadCount, Client, level)
    shots.append(Projectile(15, players[ThreadCount], level, (0, 0, 0)))
    ThreadCount += 1
    print('Client Number: ' + str(ThreadCount))




