# TODO

-   Show control schemes 
-   Bigger maps??? 
-   MORE MAPS
-   Adjustable player count and adjustible settings e.g. shot speed/player speed
-   Proper Pygame menu - https://pygame-menu.readthedocs.io/en/4.0.4/

---
### OpenGL
1. Create models.
    -  Player projectile(Little ball) and terrain (multiple types?)
2. Draw models in a pygame window
3. Plonk said models in the right place.
    -  Roatate
---


# DONE

### Basic pygame prototype
1. Display map `5/4/21`
2. Create player class
    -  Draw player in some way `5/4/21`
    -  Get movenment based on different inputs per player `5/4/21`
    -  Detect walls and stop `6/4/21`
    -  Not be allowed to roatae π radians `7/4/21`
    -  Dectect other players and filp `1/6/21`
    -  Draw box rather than picture and draw hitbox `1/6/21`
4. Get combat:
5. Crete projectile class
     -  Get when fired and starting position `7/4/21`
     -  Move and dectect walls `7/4/21`
     -  Destroy self `7/4/21`
     -  Draw projectile `7/4/21`
     -  Stop player from 're-firing' when its alredy in motion `8/4/21`
     -  Give a small cooldown `8/4/21`
6. Player projectile detection
     -  New player function - get_hitbox `8/4/21`
     -  Check for hits and decide a winner `8/4/21`
7. End Screen `8/4/21`
8. Change map system
     -  Make map into a class rather than a function `6/4/21`
     -  Store maps as strings rather than 2d arrays `27/6/21`
     -  NEW MAPS BABY - random map chosing at the start of the game `27/6/21`
9. All round improvements
     - Change player on player dection system `1/7/21`
     - Draw hitbox on player `2/7/21`
     - Change hitbox detection to use rect objects `2/7/21`
     - Add 'ready' screen `3/7/21`
     - Add option to repeat game with newly randomised map `3/7/21`

### Networking
1. Client - Server communication
     - Echo Server established and client communication
     - Server and Client have varible data to send
2. Game logic
     - Classes edited to remove unnecessary functions
     - Grid class split into 2 classes
     - Server esatblishes instances of classes on cliant join
     - Server given game logic from prototype
     - Server sends data from game logic 
     - Multipul Clients allowed 
3. Client end
     - Client displays game from recivied data
     - Client reads inputs and sends to Server
     - Client Given Connection menu
     - Client Menu visuals update

