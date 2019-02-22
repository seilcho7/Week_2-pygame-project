import pygame
import random

# Character class sets initial position and movement of hero and monster
class Character():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction_x = 0
        self.direction_y = 0

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
        print(speed, "speed")
        print(number, "number")
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

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    
    # Load background image
    background_image = pygame.image.load('images/background.png').convert_alpha()
    
    # Load hero image
    hero_image = pygame.image.load('images/hero.png')

    # Load monster image
    monster_image = pygame.image.load('images/monster.png')

    # Game initialization
    # Set initial location of hero
    hero = Hero(240, 224)
    
    # Set initial location of monster
    monster = Monster(241, 112)
    # monster_two = Character(241, 112)
    # monster_three = Character(241, 112)
    # monster_four = Character(241, 112)
    # monster_five = Character(241, 112)
    # monster_six = Character(241, 112)

    change_dir_countdown = 60


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

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True

        

        # Game logic
        hero.move(hero.direction_x, hero.direction_y)
        monster.move()
        # monster_two.moving()
        # monster_three.moving()
        # monster_four.moving()
        # monster_five.moving()
        # monster_six.moving()
        change_dir_countdown -= 1
        
        # When countdown hit 0, monster change to random direction and speed
        if change_dir_countdown == 0:
            monster.change_direction(random.randint(0, 3), random.randint(0, 5))
        #     # monster_two.change_direction(random.randint(0, 3), random.randint(2, 5))
        #     # monster_three.change_direction(random.randint(0, 3), random.randint(2, 5))
        #     # monster_four.change_direction(random.randint(0, 3), random.randint(2, 5))
            change_dir_countdown = 60

        
        # Draw background
        screen.fill(blue_color)
        screen.blit(background_image, [0, 0])
        screen.blit(hero_image, [hero.x, hero.y])
        screen.blit(monster_image, [monster.x, monster.y])
        # screen.blit(monster_image, [monster_two.x, monster_two.y])
        # screen.blit(monster_image, [monster_three.x, monster_three.y])
        # screen.blit(monster_image, [monster_four.x, monster_four.y])
        # screen.blit(monster_image, [monster_five.x, monster_five.y])
        # screen.blit(monster_image, [monster_six.x, monster_six.y])
        
        # Game display
        pygame.display.update()
        clock.tick(60)
    
    pygame.quit()

if __name__ == '__main__':
    main()