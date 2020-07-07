#!/usr/bin/python

import pygame, sys
import numpy as np
import atexit
import random

black = [0, 0, 0]
white = [255,255,255]
grey = [180,180,180]

block_width = 60
block_height = 12

fname = 'trainedQ_breakout'

resolution = 10
alpha = 0.5
l = 0.9 #lambda

STATES = {
    'Alive':0,
    'Dead':-100,
    'Scores':10,
    'Hit':1
}

#the game's constant variables
ball_radius = 10
paddle_width = 80
paddle_height = 10
#paddle_max_vec = 15


class Brick():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, block_width, block_height)



class Breakout(object):


    def __init__(self,data):

        self.highscore = 0
        self.isAuto = True
        self.command = 0
        self.iteration = 0
        self.Q = np.zeros((1280//resolution,480//resolution,3))

        if data is not None:
            try:
                self.iteration = int(data['iter'])
                self.highscore = int(data['high'])
                self.Q = data['trainedQ']
            except:
                print("Can't load data from input file, wrong format.")
                raise

        pygame.init()

        #allows for holding of key
        pygame.key.set_repeat(1,0)

        self.resetGame()

        self.screen = pygame.display.set_mode([640,480])
        self.myfont = pygame.font.SysFont("Arial",  30)

        self.se_brick = pygame.mixer.Sound('sound/brick_hit.wav')
        self.se_wall = pygame.mixer.Sound('sound/wall_hit.wav')
        self.se_paddle = pygame.mixer.Sound('sound/paddle_hit.wav')

    def initBricks(self):
        self.bricks = []
        for i in range(1,9):
            for j in range(1,5):
                temp = Brick(70*i-35,50+20*j)
                self.bricks.append(temp)

    def resetGame(self):
        #pygame.time.wait(2000)
        self.ball_x = 300
        self.ball_y = 450-ball_radius
        self.ball_speed_x = 3
        self.ball_speed_y = 5

        self.randomAngle()

        self.paddle_x = 300
        self.paddle_y = 470
        self.paddle_speed = 10
        #self.paddle_vec = 0
        self.com_vec = 0

        self.score = 0
        self.ball_hit_count = 0
        self.paddle_hit_count = 0

        self.initBricks()

    def update(self):
        #if paddle_max_vec < abs(self.paddle_vec):
        #    self.paddle_vec = paddle_max_vec * self.paddle_vec / abs(self.paddle_vec)

        #self.paddle_x += self.paddle_vec

        if self.paddle_x < 0:
            self.paddle_x = 0
            #self.paddle_vec = 0
        if self.paddle_x > self.screen.get_width() - paddle_width:
            self.paddle_x = self.screen.get_width() - paddle_width
            #self.paddle_vec = 0

        self.current_reward = STATES['Alive']
        ##MOVE THE BALL
        self.ball_y += self.ball_speed_y
        self.ball_x += self.ball_speed_x

        self.hitDetect()

    def randomAngle(self):
        self.ball_y = 450-ball_radius
        ran = random.randint(0,4)
        self.ball_speed_x = (7 - ran) * self.ball_speed_x/abs(self.ball_speed_x)
        self.ball_speed_y = (3 + ran)* self.ball_speed_y/abs(self.ball_speed_y)
        self.ball_hit_count = 0

    def hitDetect(self):
        ##COLLISION DETECTION
        ball_rect = pygame.Rect(self.ball_x-ball_radius, self.ball_y-ball_radius, ball_radius*2,ball_radius*2) #circles are measured from the center, so have to subtract 1 radius from the x and y
        paddle_rect = pygame.Rect(self.paddle_x, self.paddle_y, paddle_width, paddle_height)

        #check if the ball is off the bottom of the self.screen
        if self.ball_y > self.screen.get_height() - ball_radius:
            if pygame.display.get_active():
                self.se_wall.play()
            self.current_reward = STATES['Dead']
            self.iteration+=1
            s = 'Iteration: '+repr(self.iteration) + ', max score: ' + repr(self.score) + ', hit count: '+repr(self.paddle_hit_count)

            if self.score > self.highscore:
                self.highscore = self.score
                s += ' NEW HIGHSCORE!'

            print(s)
            self.resetGame()

        #for screen border
        if self.ball_y < ball_radius:
            self.ball_y = ball_radius
            self.ball_speed_y = -self.ball_speed_y
            if pygame.display.get_active():
                self.se_wall.play()
        if self.ball_x < ball_radius:
            self.ball_x = ball_radius
            self.ball_speed_x = -self.ball_speed_x
            if pygame.display.get_active():
                self.se_wall.play()
        if self.ball_x > self.screen.get_width() - ball_radius:
            self.ball_x = self.screen.get_width() - ball_radius
            self.ball_speed_x = -self.ball_speed_x
            if pygame.display.get_active():
                self.se_wall.play()

        #for paddle
        if ball_rect.colliderect(paddle_rect):
            self.ball_speed_y = -self.ball_speed_y
            self.current_reward = STATES['Hit']
            self.ball_hit_count +=1
            self.paddle_hit_count +=1
            if pygame.display.get_active():
                self.se_paddle.play()

            if len(self.bricks) == 0:
                self.initBricks()
        #for bricks
        for brick in self.bricks:
            if brick.rect.colliderect(ball_rect):
                if pygame.display.get_active():
                    self.se_brick.play()
                self.score = self.score + 1
                self.bricks.remove(brick)
                self.ball_speed_y = - self.ball_speed_y
                #self.current_reward = STATES['Scores']

        if self.ball_hit_count > 3:
            self.randomAngle()

    def input(self):
        self.isPressed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.command = 1
                    self.isPressed = True
                    #self.paddle_vec -= self.paddle_speed

                elif event.key == pygame.K_RIGHT:
                    self.command = 2
                    self.isPressed = True
                    #self.paddle_vec += self.paddle_speed
                elif event.key == pygame.K_a:
                    self.isAuto = not self.isAuto

        if not self.isPressed:
            self.command = 0

        return True

    def decision(self):
        self.prev = [(self.ball_x-self.paddle_x+640)/resolution,self.ball_y/resolution]

        #Observe what state is in and perform the action that maximizes expected reward.
        actions = self.Q[
            int((self.ball_x-self.paddle_x+640)/resolution),
            int(self.ball_y/resolution),
            :]

        maxs = [i for i,x in enumerate(actions) if x == np.argmax(actions)]
        if len(maxs) > 1:
            if self.command in maxs:
                com_command = self.command
            else:
                com_command = random.choice(maxs)
        else:
            com_command = np.argmax(actions)

        if self.isAuto is True:
            self.command = com_command


        if self.command == 1:
            #self.paddle_vec -= self.paddle_speed
            self.paddle_x -= self.paddle_speed
        elif self.command == 2:
            #self.paddle_vec += self.paddle_speed
            self.paddle_x += self.paddle_speed
        #else:
            #if self.paddle_vec >0:
                #self.paddle_vec -= self.paddle_speed
            #elif self.paddle_vec < 0:
                #self.paddle_vec += self.paddle_speed

    def observe(self):
        prev_Q = self.Q[int(self.prev[0]),int(self.prev[1]),int(self.command)]

        self.Q[
            int(self.prev[0]),
            int(self.prev[1]),
            int(self.command)
            ] = (prev_Q + alpha * (self.current_reward + l * max(self.Q[int((self.ball_x-self.paddle_x+640)/resolution),int(self.ball_y/resolution),:]) - prev_Q))

    def draw(self):
        self.screen.fill(white)

        score_label = self.myfont.render(str(self.score), 100, pygame.color.THECOLORS['black'])
        self.screen.blit(score_label, (5, 10))

        count_label = self.myfont.render(str(self.paddle_hit_count), 100, pygame.color.THECOLORS['gray'])
        self.screen.blit(count_label, (70, 10))

        if self.isAuto is True:
            auto_label = self.myfont.render("Auto", 100, pygame.color.THECOLORS['red'])
            self.screen.blit(auto_label, (570, 10))
        
        for brick in self.bricks:
            pygame.draw.rect(self.screen, [0, 120, 120], brick.rect,0)
        
        pygame.draw.circle(self.screen, [0,0,255], [int(self.ball_x), int(self.ball_y)], ball_radius, 0)
        pygame.draw.rect(self.screen, [255,0,0], [self.paddle_x, self.paddle_y, paddle_width, paddle_height], 0)

        pygame.display.update()

    def quit(self):
        pygame.quit()

    def saveData(self):
        data = [int(self.iteration), int(self.highscore),self.Q]
        return data


@atexit.register
def save():
    savedata = game.saveData()
    np.savez(fname,iter = savedata[0],high = savedata[1],trainedQ = savedata[2])
    print("Data saved successfully.")


if len(sys.argv) > 1:
    fname = str(sys.argv[1]).replace('.npz','')

    try:
        data = np.load(str(fname)+'.npz')
        game = Breakout(data)
        s = "Q loaded from " + str(fname) + " successfully."
        print(s)

    except IOError:
        s = "Error: can't find file or read data from " + str(fname) +".npz, initializing a new Q matrix"
        print(s)
        game = Breakout(None)


    #game loop
    while game.input():
        game.decision()
        game.update()
        game.observe()
        game.draw()

    game.quit()
else:
    print('INPUT ERROR: no file name provided. Read README.md for help.')
