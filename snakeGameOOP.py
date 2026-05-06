import pygame
from pygame.locals import *
import time
from random import randint

SIZE = 20
BACKGROUND_COLOR = (92 ,25, 84)

class Eyes:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("eyes.jpg").convert()
        self.parent_screen = parent_screen
        self.x = SIZE*3
        self.y = SIZE*3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = randint(1, 24)*SIZE
        self.y = randint(1, 24)*SIZE

class Snake:
    def __init__(self, parent_screen, length): 
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("block.jpg").convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = 'down'

    def increase_length(self):
        self.length += 1
        self.x.append(-1) 
        self.y.append(-1)
    
    def move_left(self):
        self.direction = 'left'
    def move_right(self):
        self.direction = 'right'
    def move_up(self):
        self.direction = 'up'
    def move_down(self):
        self.direction = 'down'

    def walk(self):
        for i in range(self.length-1, 0, -1):
             self.x[i] =  self.x[i - 1]
             self.y[i] =  self.y[i - 1]  
        if self.direction == "left":
            self.x[0] -= SIZE
        if self.direction == "right":
            self.x[0] += SIZE
        if self.direction == "up":
            self.y[0] -= SIZE
        if self.direction == "down":
            self.y[0] += SIZE
        self.draw()

    def draw(self):
        #self.parent_screen.fill(BACKGROUND_COLOR)
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

class Game:

    def __init__ (self):
        pygame.init()
        pygame.display.set_caption("codebasics Snake And Apple Game")

        pygame.mixer.init()
        self.play_background_music()

        self.surface = pygame.display.set_mode((600, 600))
        self.render_background()
        #self.surface.fill(BACKGROUND_COLOR)
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.eyes = Eyes(self.surface)
        self.eyes.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
             if y1 >= y2 and y1 < y2 + SIZE:
                 return True
        return False

    def display_score(self):
        font = pygame.font.SysFont('arial', 30) 
        score = font.render(f"Score: {self.snake.length - 1}", True, (200, 200, 200))
        self.surface.blit(score, (400, 10))

    def play_sound(self, sound):
        sound = pygame.mixer.Sound(f"{sound}.mp3")
        pygame.mixer.Sound.play(sound)
    
    def play_background_music(self):
        pygame.mixer.music.load("background_music.mp3")
        pygame.mixer.music.play()

    def render_background(self):
        bg = pygame.image.load("bg_bicture.jpg")
        self.surface.blit(bg, (0,0))

    def play(self):
        self.render_background()
        self.snake.walk()
        self.eyes.draw()
        self.display_score()
        pygame.display.flip()

        # snake coliding with apple

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.eyes.x, self.eyes.y):
            self.play_sound("eat")
            self.snake.increase_length()
            self.eyes.move()

        # snake coliding with itself
  
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound("crash")
                raise Exception("Collision Occured")
                
    def show_game_over(self):
        self.render_background()
        #self.surface.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont('arial', 30)  
        line1 = font.render(f"Game over! your score is {self.snake.length}", True, (200, 200, 200))
        self.surface.blit(line1, (150, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (110, 110, 5))
        self.surface.blit(line2, (50, 350))
        pygame.display.flip()
        pygame.mixer.music.pause()
    
    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.eyes = Eyes(self.surface)
 
    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == QUIT: 
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False
                    if not pause:
                        if event.key == K_UP:
                            self.snake.move_up() 
                        if event.key == K_DOWN:
                            self.snake.move_down()  
                        if event.key == K_LEFT:
                            self.snake.move_left() 
                        if event.key == K_RIGHT:
                            self.snake.move_right() 
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(0.2)
              
  
if __name__ == '__main__': 
    game = Game()
    game.run()
        
 








  
'''
def draw_block():
    surface.fill((92,25,84))
    surface.blit(block,(block_x, block_y))
    pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    
    surface = pygame.display.set_mode((1000, 500))
    surface.fill((92,25,84))
    block = pygame.image.load("block.jpg").convert()
    block_x = 100
    block_y = 100
    surface.blit(block,(block_x, block_y))
    pygame.display.flip()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if event.key == K_UP:
                    block_y -= 10 
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block() 
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block() 
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()  

            elif event.type == QUIT: 
                running = False
'''