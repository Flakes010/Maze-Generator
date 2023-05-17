from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint
import maze_generator

MAZE_WIDTH = 39 # Width of the maze (must be odd).
MAZE_HEIGHT = 19

def input(key):
    if key == "m":
        print(maze_generator.maze)
    if key == "n": # new
        for e in liste:
            destroy(e)
        maze = maze_generator.make_random()
        generator(maze)

app = Ursina()

Sky(texture="sky_sunset")

ground = Entity(model="plane", scale=400, texture="grass", collider="box")

# player = FirstPersonController()

liste = []

def generator(maze_dict):
    liste.clear()
    player_offset = True
    start = randint(1, 10)
    end = randint(1, 10)
    index_start = 0
    index_end = 0

    for w in range(MAZE_WIDTH):
        for h in range(MAZE_HEIGHT):
            if maze_dict[(w, h)] == chr(9608):
                maze = Entity(model="cube", position=((w*4), 4, h*4), scale=(4,12,4), collider="box", color=color.light_gray, texture="brick",texture_scale=(2,2))
            
            else:
                maze = Entity(model="cube", position=((w*4), 4, h*4), scale=(4,12,4), color=color.clear)
                
                if player_offset:
                    # player.position = maze.position + Vec3(0, -4, 0)
                    player_offset = False
                
                if start>0 and w==1:
                    print("start = ", start)
                    start -= 1
                    index_start = h
            
                if end>0 and w==37:
                    print("end = ", end)
                    end -= 1
                    index_end = h
            liste.append(maze)  

    destroy(liste[index_start]) 
    destroy(liste[index_end-19])      

EditorCamera()

generator(maze_generator.maze)

app.run()
