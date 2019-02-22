import pygame
import random
import math

# Character class sets initial position and movement of hero and monster
class Character():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction_x = 0
        self.direction_y = 0

    # Calculate distance
    def distance(self, char):
        if math.sqrt((self.x - char.x)**2 + ((self.y - char.y))**2) < 32:
            if type(char) == Monster:
                char.show = False
                self.x = 240
                self.y = 324
                


    # Monsters randomly move around, and as they hit end of the screen,
    # they come back from other side of the screen

# Monster class inherit from Character class
class Monster(Character):
    # Monster starts moving around
    def move(self):
        self.x += self.direction_x
        self.y += self.direction_y
        if self.y < 0:
            self.y = 480
        elif self.x < 0:
            self.x = 512
        elif self.x > 512:
            self.x = 0
        elif self.y > 480:
            self.y = 0

    # Randomly change speed and direction of the monsters
    def change_direction(self, number, speed):
        # Change direction to north
        if number == 0:
            self.direction_y = speed
            self.direction_y = -self.direction_y

        # Change direction to south
        elif number == 2:
            self.direction_y = speed
            self.direction_y = self.direction_y
 
        # Change direction to east
        elif number == 1:
            self.direction_x = speed
            self.direction_x = self.direction_x
 
        # Change direction to west
        else:
            self.direction_x = speed
            self.direction_x = -self.direction_x

# Hero class inherit from Character class
class Hero(Character):  
    # As arrow keys are pressed, hero move to the direction of the arrow
    def move(self, direction_x, direction_y):
        if direction_x == 3:
            self.x += direction_x
        if direction_x == -3:
            self.x += direction_x
        if direction_y == 3:
            self.y += direction_y
        if direction_y == -3:
            self.y += direction_y
    

def main():
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    # Set surface and font for text
    pygame.font.init()
    textfont = pygame.font.SysFont(None, 40)
    end_text = textfont.render('Hit ENTER to play again!', 1, (0, 0, 0))
    
     # Set background music
    pygame.mixer.init()
    music = pygame.mixer.Sound('sounds/music.wav')
    music.set_volume(0.3)
    
    # Set win sound effect
    win = pygame.mixer.Sound('sounds/win.wav')
    win.set_volume(1.0)

    win_sound = 0
    
    music.play()


    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Catch Monster')
    clock = pygame.time.Clock()
    
    # Load background image
    background_image = pygame.image.load('images/background.png').convert_alpha()
    
    # Load hero image
    hero_image = pygame.image.load('images/hero.png')

    # Load monster image
    monster_image = pygame.image.load('images/monster.png')

    # Game initialization
    # Set initial location of hero
    hero = Hero(240, 324)
    hero.show = True
    
    # Set initial location of monsters
    monster = Monster(241, 112)
    # monster_two = Monster(241, 112)
    # monster_three = Monster(241, 112)
    # monster_four = Monster(241, 112)
    monster.show = True

    change_dir_countdown = 30

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            # When arrow keys are pressed down, move hero character to direction of arrow
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    hero.direction_y = 3
                elif event.key == pygame.K_UP:
                    hero.direction_y = -3
                elif event.key == pygame.K_LEFT:
                    hero.direction_x = -3
                elif event.key == pygame.K_RIGHT:
                    hero.direction_x = 3
            # When arrow keys are released, hero stops
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    hero.direction_y = 0
                elif event.key == pygame.K_UP:
                    hero.direction_y = 0
                elif event.key == pygame.K_LEFT:
                    hero.direction_x = 0
                elif event.key == pygame.K_RIGHT:
                    hero.direction_x = 0
        
        # Stops hero before bush
        if hero.x <= 32:
            hero.x = 32
        if hero.x >= 448:
            hero.x = 448
        if hero.y <= 32:
            hero.y = 32
        if hero.y >= 416:
            hero.y = 416


        # Event handling

        if event.type == pygame.QUIT:
            stop_game = True

        hero.distance(monster)

        # Game logic
        hero.move(hero.direction_x, hero.direction_y)
        monster.move()
        # monster_two.move()
        # monster_three.move()
        # monster_four.move()

        change_dir_countdown -= 1
        
        # When countdown hit 0, monster change to random direction and speed
        if change_dir_countdown == 0:
            monster.change_direction(random.randint(0, 3), random.randint(0, 5))
            # monster_two.change_direction(random.randint(0, 3), random.randint(2, 5))
            # monster_three.change_direction(random.randint(0, 3), random.randint(2, 5))
            # monster_four.change_direction(random.randint(0, 3), random.randint(2, 5))
            change_dir_countdown = 30

        
        # Draw background
        screen.fill(blue_color)
        screen.blit(background_image, [0, 0])
        
        # Show hero as long as it is alive
        if hero.show == True:
            screen.blit(hero_image, [hero.x, hero.y])    

        # Show monsters as long as hero does not catch
        if monster.show == True:        
            screen.blit(monster_image, [monster.x, monster.y])
            # screen.blit(monster_image, [monster_two.x, monster_two.y])
            # screen.blit(monster_image, [monster_three.x, monster_three.y])
            # screen.blit(monster_image, [monster_four.x, monster_four.y])
        
        # When catch a monster, play sound effect, put text in the middle, end game
        else:
            if win_sound == 0:
                win.play()
                win_sound = 1
            screen.blit(end_text, (90, 224))
            
            # Reset hero and monster position back to original
            hero.x = 240
            hero.y = 324
            monster.x = 241
            monster.y = 112
            
            # Play again when ENTER is pressed
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        win_sound = 0
                        monster.show = True





        # Game display
        pygame.display.update()
        clock.tick(60)
    
    pygame.quit()

if __name__ == '__main__':
    main()