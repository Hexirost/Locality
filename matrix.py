import pygame
import simpy
from NetworkGraph import NetworkGraph

env = simpy.RealtimeEnvironment(initial_time=0, factor=0.05, strict=False)

pygame.init()

size = width, height = 1000, 800

screen	= pygame.display.set_mode(size)
display = pygame.display
image	= pygame.image
event	= pygame.event

graph = NetworkGraph(env, screen, display, image, event)

env.process(graph)

env.run(until= 100)