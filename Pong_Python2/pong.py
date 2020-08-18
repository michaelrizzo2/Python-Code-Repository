#!/usr/bin/python2
#We first need to create the blank screen
#we need to first import the pygame and sys modules
import pygame,sys
from pygame.locals import *

#Now we need to set the number of frames per second
FPS=60
#Now we need to set the width and height of the window
window_height=400
window_width=600
#This is where we will set the line thickness, paddle sie and paddle offset
line_thickness=10
paddle_size=50
paddle_offset=20
#Now we need to setup the colors
black=(0,0,0)
white=(255,255,255)
#Now we will set up the main function to display the blank window
def main():
    pygame.init()
    #Set up global display surf variable
    global displaysurf
    #This is where we will set up the font information
    global basic_font,basic_font_size
    basic_font_size=20
    basic_font=pygame.font.Font('freesansbold.ttf',basic_font_size)
    #Now we need to set up the fps clock for the game
    fpsclock=pygame.time.Clock()
    #This is where we will set up the surface
    displaysurf=pygame.display.set_mode((window_width,window_height))
    #Now we need to set up the caption
    pygame.display.set_caption("Michael Pong")
    #Now we need to set up the locations for the ball and the paddle
    ballx=window_width/2-line_thickness/2
    bally=window_height/2-line_thickness/2
    #Now we need to set the player positions
    player_one_position=(window_height-paddle_size)/2
    player_two_position=(window_height-paddle_size)/2
    #This is where we will keep track of the scores
    player_score,computer_score=0,0
    #This is where we will keep track of the ball direction
    ball_direction_x=-1
    ball_direction_y=-1
    paddle_1=pygame.Rect(paddle_offset,player_one_position,line_thickness,paddle_size)
    paddle_2=pygame.Rect(window_width-paddle_offset-line_thickness,player_two_position,line_thickness,paddle_size)
    #Now we need to set the ball position
    ball=pygame.Rect(ballx,bally,line_thickness,line_thickness)
    #Now we need to draw the rectangles
    drawArena()
    drawPaddle(paddle_1)
    drawPaddle(paddle_2)
    drawBall(ball)
    #This will make the cursor invisible
    pygame.mouse.set_visible(0)
    #Now we need to setup the main game loop
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            #This will detect the motion of the mouse
            elif event.type==MOUSEMOTION:
                mouse_x,mouse_y=event.pos
                paddle_1.y=mouse_y
        drawArena()
        drawPaddle(paddle_1)
        drawPaddle(paddle_2)
        drawBall(ball)
        #This is where we will move the ball
        ball=moveball(ball,ball_direction_x,ball_direction_y)
        #This is where we will check if the ball has hit the edge
        ball_direction_x,ball_direction_y=check_edge_collision(ball,ball_direction_x,ball_direction_y)
        #This is where we will update the score
        player_score,computer_score=check_point_scored(paddle_1,ball,player_score,computer_score,ball_direction_x)
        #This will check if the ball was hit by the paddle
        ball_direction_x*=check_hit_ball(ball,paddle_1,paddle_2,ball_direction_x)
        #This is where we will move the seond paddle
        paddle_2=artificial_intelligence(ball,ball_direction_x,paddle_2)
        #This will display the score
        display_score(player_score,computer_score)
        #Update pygame display
        pygame.display.update()
        fpsclock.tick(FPS)
#This will display the surface for the pong game
def drawArena():
    displaysurf.fill((0,0,0))
    #Now we need to draw the outline
    pygame.draw.rect(displaysurf,white,((0,0),(window_width,window_height)),line_thickness*2)
    #Now we need to draw the center line
    pygame.draw.line(displaysurf,white,((window_width/2),0),((window_width/2),window_height),(line_thickness/4))

#Next we need to draw the paddle
def drawPaddle(paddle):
    #This will stop the paddle from moving too low
    if paddle.bottom>window_height-line_thickness:
        paddle.bottom=window_height-line_thickness
    #This will stop the paddle from moving too high
    elif paddle.top<line_thickness:
        paddle.top=line_thickness
    #This will draw the paddle
    pygame.draw.rect(displaysurf,white,paddle)

def drawBall(ball):
    pygame.draw.rect(displaysurf,white,ball)
#This is where we will move the ball
def moveball(ball,ball_direction_x,ball_direction_y):
    ball.x+=ball_direction_x
    ball.y+=ball_direction_y
    return ball
#This is where we we bounce the ball of the wall if the ball hits the edge
def check_edge_collision(ball,ball_direction_x,ball_direction_y):
    if ball.top==line_thickness or ball.bottom==window_height-line_thickness:
        ball_direction_y*=-1
    if ball.left==line_thickness or ball.right==window_width-line_thickness:
        ball_direction_x*=-1
    return ball_direction_x,ball_direction_y
#This will check if the ball has hit the paddle
def check_hit_ball(ball,paddle_1,paddle_2,ball_direction_x):
    if ball_direction_x==-1 and paddle_1.right==ball.left and paddle_1.top<ball.top and paddle_1.bottom>ball.bottom:
        return -1
    elif ball_direction_x==1 and paddle_2.left==ball.right and paddle_2.top<ball.top and paddle_2.bottom>ball.bottom:
        return -1 
    else:
        return 1
def check_point_scored(paddle_1,ball,player_score,computer_score,ball_direction_x):
    #This will reset the ball if the left wall is hit
    if ball.left==line_thickness:
        computer_score+=1
    #1 point for hitting the ball
    #elif ball_direction_x is -1 and paddle_1.right==ball.left and paddle_1.top<ball.top and paddle_1.bottom>ball.bottom:
     #   score+=1
    elif ball.right==window_width-line_thickness:
        player_score +=1
    return player_score,computer_score

#This will print the score on the screen
def display_score(player_score,computer_score):
    result_surface=basic_font.render("Player : %s Computer :%s"% (str(player_score),str(computer_score)),True,white)
    result_rectangle=result_surface.get_rect()
    result_rectangle.topleft=(window_width-240,25)
    displaysurf.blit(result_surface,result_rectangle)
#This function will allow the computer to move the paddle
def artificial_intelligence(ball,ball_direction_x,paddle_2):
    #If the ball is moving away from the paddle,move the paddle back to the center
    if ball_direction_x==-1:
        #if the paddle is at the bottom of the screen,move the paddle up
        if paddle_2.centery<window_height/2:
            paddle_2.y+=1
        #if the paddle is at the top of the screen, move the paddle down
        elif  paddle_2.centery>window_height/2:
            paddle_2.y-=1
    #This will make the computer paddle move when the ball is coming towards the paddle
    elif ball_direction_x==1:
        #Now we need to tell the paddle to move up if the paddle coordiantes are below the ball coordinates
        if paddle_2.centery<ball.centery:
            paddle_2.y+=.25
        else:
            paddle_2.y-=.25
    return paddle_2    

main()        
