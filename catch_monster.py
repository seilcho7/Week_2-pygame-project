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
            if type(char) == Hero:
                char.show = False

# Monster class inherit from Character class
class Monster(Character):
    # Monsters starts moving around
    # They come back from other side of the screen
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

# Goblin class inherit from Monster class
class Goblin(Monster):
    pass

    

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
    textfont = pygame.font.SysFont(None, 30)
    win_text = textfont.render('Hit ENTER to play again!', 1, (0, 0, 0))
    lose_text = textfont.render('You lose! Hit ENTER to play again.', 1, (0, 0, 0))
     
     
     # Set background music
    pygame.mixer.init()
    music = pygame.mixer.Sound('sounds/music.wav')
    music.set_volume(0.3)
    
    # Set win sound effect
    win = pygame.mixer.Sound('sounds/win.wav')
    win.set_volume(1.0)

    # Set lose sound effect
    lose = pygame.mixer.Sound('sounds/lose.wav')
    lose.set_volume(0.5)

    # Counter to play win, lose only once
    win_sound = 0
    lose_sound = 0
    
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
    # Load goblin image
    goblin_image = pygame.image.load('images/goblin.png')

    # Game initialization
    # Set initial location of hero
    hero = Hero(240, 324)
    
    # Set initial location of monster
    monster = Monster(241, 112)
    
    # Set initial location of monster
    goblin = Goblin(random.randint(0, 512), random.randint(0, 480))

    # Show image only when True
    hero.show = True
    monster.show = True
    goblin.show = True

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

        # Call function for collision
        hero.distance(monster)
        goblin.distance(hero)

        # Game logic
        hero.move(hero.direction_x, hero.direction_y)
        monster.move()
        goblin.move()

        change_dir_countdown -= 1
        
        # When countdown hit 0, monster change to random direction and speed
        if change_dir_countdown == 0:
            monster.change_direction(random.randint(0, 3), random.randint(0, 5))
            goblin.change_direction(random.randint(0, 3), random.randint(0, 2))
            change_dir_countdown = 30

        
        # Draw background
        screen.fill(blue_color)
        screen.blit(background_image, [0, 0])
        
        # Show hero as long as it is alive
        if hero.show == True:
            screen.blit(hero_image, [hero.x, hero.y])   
        
        # When goblin catch hero, play sound effect, put text, end game
        else:
            if lose_sound == 0:
                lose.play()
                lose_sound = 1
            screen.blit(lose_text, (90, 224))
            hero.x = 0
            hero.y = 0
            
            # Play again when ENTER is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    lose_sound = 0
                    # Put monster back in random position
                    hero.x = random.randint(0, 512)
                    hero.y = random.randint(0, 480)
                    hero.show = True 

        # Show monster as long as hero does not catch
        if monster.show == True:        
            screen.blit(monster_image, [monster.x, monster.y])

        # When catch a monster, play sound effect, put text, end game
        else:
            if win_sound == 0:
                win.play()
                win_sound = 1
            screen.blit(win_text, (140, 224))
            goblin.show = False
            goblin.x = 0
            goblin.y = 0
            
            # Play again when ENTER is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    win_sound = 0
                    # Put monster back in random position
                    monster.x = random.randint(0, 512)
                    monster.y = random.randint(0, 480)
                    monster.show = True
                    goblin.show = True
        
        # Show goblins
        if goblin.show == True:
            screen.blit(goblin_image, [goblin.x, goblin.y])
        
        # Game display
        pygame.display.update()
        clock.tick(60)
    
    pygame.quit()

if __name__ == '__main__':
    main()