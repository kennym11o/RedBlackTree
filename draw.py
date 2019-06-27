from red_black_tree import Node
from red_black_tree import RedBlackTree
import pygame
import math
import sys


SCREENWIDTH = 1200
SCREENLENGTH = 600
def drawBT(node, x=SCREENWIDTH//2, y=0, l=1):
    if node == None or node.getKey() == None:
        return
    if node.color == "Black":
        color = (0,0,0)
    if node.color == "Red":
        color = (255, 0, 0)
    if node.looking == True:
        fontColor = (255, 255, 0)
    else:
        fontColor = (255, 255, 255)
    screen.blit(font.render(str(node.getKey()), True, fontColor, color), (math.floor(x), y))
    screen.blit(font.render(str(node.getValue()), True, fontColor, color), (math.floor(x), y+20))
    drawBT(node.getLeftChild(),x-x/math.pow(2,l) , y+50, l+1)
    drawBT(node.getRightChild(),x+x/math.pow(2,l), y+50, l+1)
pygame.init()
screen = pygame.display.set_mode((SCREENWIDTH, SCREENLENGTH))
font = pygame.font.Font(None, 24)
T = RedBlackTree()
clock = pygame.time.Clock()
current = None
while True:
    clock.tick(30)
    screen.fill((255,255,255))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                sys.exit()
            if i.key == pygame.K_i:
                print("Enter key(must be number): ")
                key = int(input())
                print("Enter value: ")
                value = input()
                T.insert(Node(key, value))
            if i.key == pygame.K_f:
                if current != None:
                    current.looking = False
                print("Enter key(must be number): ")
                key = int(input())
                current = T.find(key)
                if current != None:
                    current.looking = True
            if i.key == pygame.K_r:
                print("Enter key(must be number): ")
                T.remove(int(input()))
            if i.key == pygame.K_p:
                T.printInOrder()
    drawBT(T.root)
    pygame.display.flip()
