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
            
            # If monster hit goblin, monster change direction
            if type(char) == Goblin:
                self.direction_x = -self.direction_x
                self.direction_y = -self.direction_y

# Monster class inherit from Character class
class Monster(Character):
    # Monster starts moving around
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
    def move(self):
        self.x += self.direction_x
        self.y += self.direction_y
        
    # Goblin cannot go past bush and turns back when they hit bush
    def fence(self):
        if self.x <= 32:
            self.direction_x = -self.direction_x
        if self.x >= 448:
            self.direction_x = -self.direction_x
        if self.y <= 32:
            self.direction_y = -self.direction_y
        if self.y >= 416:
            self.direction_y = -self.direction_y

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
    
    # Hero cannot go past bush
    def fence(self):
        if self.x <= 32:
            self.x = 33
        if self.x >= 448:
            self.x = 447
        if self.y <= 32:
            self.y = 33
        if self.y >= 416:
            self.y = 415
    
def main():
    width = 512
    height = 480
    
    # Level counter
    level = 1

    # Set surface and font for text
    pygame.font.init()
    textfont = pygame.font.SysFont(None, 30)
    levelfont = pygame.font.SysFont(None, 26)
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
    goblin = Goblin(random.randint(33, 447), random.randint(33, 415))

    # Add more goblin
    goblin_two = Goblin(512, 480)
    goblin_three = Goblin(512, 480)
    
    # Show image only when True
    hero.show = True
    monster.show = True
    goblin.show = True
    goblin_two.show = False
    goblin_three.show = False

    # Count for monster and goblin change_direction function
    change_dir_countdown = 30

    stop_game = False
    while not stop_game:
        # Set level text to update every level
        level_text = levelfont.render(('Level %d' % level), 1, (255, 255, 255))
        
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

        # Call function for fence which prevent hero and monster
        # going outside bush
        Hero.fence(hero)
        Goblin.fence(goblin)
        Goblin.fence(goblin_two)
        Goblin.fence(goblin_three)
        


        # Event handling
        if event.type == pygame.QUIT:
            stop_game = True

        # Call function for collision
        hero.distance(monster)
        # Goblin catch hero
        goblin.distance(hero)
        goblin_two.distance(hero)
        goblin_three.distance(hero)
        # Monster bump with goblins
        monster.distance(goblin)
        monster.distance(goblin_two)
        monster.distance(goblin_three)
        # Goblins bump each other
        goblin.distance(goblin_two)
        goblin.distance(goblin_three)
        goblin_two.distance(goblin_three)

        # Game logic
        hero.move(hero.direction_x, hero.direction_y)
        monster.move()
        goblin.move()
        if level >= 2:
            goblin_two.move()
        if level >= 3:
            goblin_three.move()
        
        # Every loop, change_dir_countdown decrease by 1
        change_dir_countdown -= 1
        
        # When countdown hit 0, monster change to random direction and speed
        if change_dir_countdown == 0:
            monster.change_direction(random.randint(0, 3), random.randint(0, 5))
            goblin.change_direction(random.randint(0, 3), random.randint(0, 2))
            if level >= 2:
                goblin_two.change_direction(random.randint(0, 3), random.randint(0, 2))
            if level >= 3:
                goblin_three.change_direction(random.randint(0, 3), random.randint(0, 2))
            change_dir_countdown = 30

        
        # Draw background
        screen.blit(background_image, (0, 0))

        # Show level on top left
        screen.blit(level_text, (5, 5))
        
        # Show hero as long as it is alive
        if hero.show == True:
            screen.blit(hero_image, (hero.x, hero.y)  ) 
        
        # When goblin catch hero, play sound effect, put text, end game
        else:
            if lose_sound == 0:
                lose.play()
                lose_sound = 1
            screen.blit(lose_text, (90, 224))
            hero.x = 0
            hero.y = 0
            monster.x = 512
            monster.y = 0
            
            # Play again when ENTER is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    lose_sound = 0
                    level = 1
                    # Put monster back in random position
                    hero.x = random.randint(35, 445)
                    hero.y = random.randint(35, 413)
                    monster.x = random.randint(35, 445)
                    monster.y = random.randint(35, 413)
                    hero.show = True
                    goblin_two.x = 512
                    goblin_two.y = 480
                    goblin_two.show = False
                    goblin_three.x = 512
                    goblin_three.y = 480
                    goblin_three.show = False

        # Show monster as long as hero does not catch
        if monster.show == True:        
            screen.blit(monster_image, (monster.x, monster.y))

        # When catch a monster, play sound effect, put text, end game
        else:
            if win_sound == 0:
                win.play()
                win_sound = 1
            screen.blit(win_text, (140, 224))
            goblin.x = 512
            goblin.y = 480
            goblin_two.x = 512
            goblin_two.y = 480
            goblin_three.x = 512
            goblin_three.y = 480
            
            # Play again when ENTER is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    win_sound = 0
                    level += 1
                    if level >= 2:
                        goblin_two.show = True
                    if level >= 3:
                        goblin_two.show = True
                        goblin_three.show = True

                    # Put monster back in random position
                    monster.x = random.randint(35, 445)
                    monster.y = random.randint(35, 413)
                    goblin.x = random.randint(35, 445)
                    goblin.y = random.randint(35, 413)
                    goblin_two.x = random.randint(35, 445)
                    goblin_two.y = random.randint(35, 413)
                    goblin_three.x = random.randint(35, 445)
                    goblin_three.y = random.randint(35, 413)
                    monster.show = True
                    goblin.show = True
        
        # Show goblins
        if goblin.show == True:
            screen.blit(goblin_image, (goblin.x, goblin.y))
        
        if goblin_two.show == True:
            screen.blit(goblin_image, (goblin_two.x, goblin_two.y))

        if goblin_three.show == True:
            screen.blit(goblin_image, (goblin_three.x, goblin_three.y))
        
        # Game display
        pygame.display.update()
        clock.tick(60)
    
    pygame.quit()

if __name__ == '__main__':
    main()