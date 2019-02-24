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
    overfont = pygame.font.SysFont(None, 40)
    win_text = textfont.render('Hit ENTER to play again!', 1, (0, 0, 0))
    lose_text = textfont.render('You lose! Hit ENTER to play again.', 1, (0, 0, 0))
    caught_text = textfont.render('You caught all the monsters!', 1, (0, 0, 0))
    over_text = overfont.render('Game Over', 1, (0, 0, 0))
    again_text = textfont.render('Hit ENTER to play again!', 1, (0, 0, 0))
     
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
    
    # Background music loops
    music.play(-1)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Catch Monsters')
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
    goblin_b = Goblin(512, 480)
    goblin_c = Goblin(512, 480)
    goblin_d = Goblin(512, 480)
    goblin_e = Goblin(512, 480)
    goblin_f = Goblin(512, 480)
    goblin_g = Goblin(512, 480)
    goblin_h = Goblin(512, 480)
    goblin_i = Goblin(512, 480)
    goblin_j = Goblin(512, 480)
    
    # Show image only when True
    hero.show = True
    monster.show = True
    goblin.show = True
    goblin_b.show = False
    goblin_c.show = False
    goblin_d.show = False
    goblin_e.show = False
    goblin_f.show = False
    goblin_g.show = False
    goblin_h.show = False
    goblin_i.show = False
    goblin_j.show = False

    # Count for monster and goblin change_direction function
    change_dir_countdown = 30

    # Set count for collision to occur
    free_count = 0
    free_countdown = 80

    stop_game = False
    while not stop_game:
        # Set level text to update every level
        if level < 6:
            level_text = levelfont.render(('Level %d' % level), 1, (255, 255, 255))
        
        # When arrow keys are pressed down, move hero character to direction of arrow
        for event in pygame.event.get():
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
        Goblin.fence(goblin_b)
        Goblin.fence(goblin_c)
        Goblin.fence(goblin_d)
        Goblin.fence(goblin_e)
        Goblin.fence(goblin_f)
        Goblin.fence(goblin_g)
        Goblin.fence(goblin_h)
        Goblin.fence(goblin_i)
        Goblin.fence(goblin_j)

        # Event handling
        if event.type == pygame.QUIT:
            stop_game = True

        # Call function for collision
        hero.distance(monster)
        # Goblin catch hero
        if free_count == 0:
            goblin.distance(hero)
            goblin_b.distance(hero)
            goblin_c.distance(hero)
            goblin_d.distance(hero)
            goblin_e.distance(hero)
            goblin_f.distance(hero)
            goblin_g.distance(hero)
            goblin_h.distance(hero)
            goblin_i.distance(hero)
            goblin_j.distance(hero)
        # # Monster bump with goblins
        # monster.distance(goblin)
        # monster.distance(goblin_b)
        # monster.distance(goblin_c)
        # monster.distance(goblin_d)
        # monster.distance(goblin_e)
        # monster.distance(goblin_f)
        # monster.distance(goblin_g)
        # monster.distance(goblin_h)
        # monster.distance(goblin_i)
        # monster.distance(goblin_j)
        # # Goblins bump each other
        # goblin.distance(goblin_b)
        # goblin.distance(goblin_c)
        # goblin.distance(goblin_d)
        # goblin.distance(goblin_e)
        # goblin.distance(goblin_f)
        # goblin.distance(goblin_g)
        # goblin.distance(goblin_h)
        # goblin.distance(goblin_i)
        # goblin.distance(goblin_j)
        # goblin_b.distance(goblin_c)
        # goblin_b.distance(goblin_d)
        # goblin_b.distance(goblin_e)
        # goblin_b.distance(goblin_f)
        # goblin_b.distance(goblin_g)
        # goblin_b.distance(goblin_h)
        # goblin_b.distance(goblin_i)
        # goblin_b.distance(goblin_j)
        # goblin_c.distance(goblin_d)
        # goblin_c.distance(goblin_e)
        # goblin_c.distance(goblin_f)
        # goblin_c.distance(goblin_g)
        # goblin_c.distance(goblin_h)
        # goblin_c.distance(goblin_i)
        # goblin_c.distance(goblin_j)
        # goblin_d.distance(goblin_e)
        # goblin_d.distance(goblin_f)
        # goblin_d.distance(goblin_g)
        # goblin_d.distance(goblin_h)
        # goblin_d.distance(goblin_i)
        # goblin_d.distance(goblin_j)
        # goblin_e.distance(goblin_f)
        # goblin_e.distance(goblin_g)
        # goblin_e.distance(goblin_h)
        # goblin_e.distance(goblin_i)
        # goblin_e.distance(goblin_j)
        # goblin_f.distance(goblin_g)
        # goblin_f.distance(goblin_h)
        # goblin_f.distance(goblin_i)
        # goblin_f.distance(goblin_j)
        # goblin_g.distance(goblin_h)
        # goblin_g.distance(goblin_i)
        # goblin_g.distance(goblin_j)
        # goblin_h.distance(goblin_i)
        # goblin_h.distance(goblin_j)
        # goblin_i.distance(goblin_j)

        # Game logic
        if level < 6:
            hero.move(hero.direction_x, hero.direction_y)
            monster.move()
            goblin.move()
            if level >= 2:
                goblin_b.move()
                goblin_c.move()
            if level >= 3:
                goblin_d.move()
                goblin_e.move()
            if level >= 4:
                goblin_f.move()
                goblin_g.move()
            if level >= 5:
                goblin_h.move()
                goblin_i.move()
                goblin_j.move()
        
        # Every loop, change_dir_countdown decrease by 1
        change_dir_countdown -= 1

        # Hero does not die as long as free_count is 1
        free_countdown -= 1
        if free_countdown == 0:
            free_count = 0
        
        # When countdown hit 0, monster change to random direction and speed
        if level < 6:
            if change_dir_countdown == 0:
                monster.change_direction(random.randint(0, 3), random.randint(0, 5))
                goblin.change_direction(random.randint(0, 3), random.randint(0, 3))
                if level >= 2:
                    goblin_b.change_direction(random.randint(0, 3), random.randint(0, 3))
                    goblin_c.change_direction(random.randint(0, 3), random.randint(0, 3))
                if level >= 3:
                    goblin_d.change_direction(random.randint(0, 3), random.randint(0, 3))
                    goblin_e.change_direction(random.randint(0, 3), random.randint(0, 3))
                if level >= 4:
                    goblin_f.change_direction(random.randint(0, 3), random.randint(0, 3))
                    goblin_g.change_direction(random.randint(0, 3), random.randint(0, 3))
                if level >= 5:
                    goblin_h.change_direction(random.randint(0, 3), random.randint(0, 3))
                    goblin_i.change_direction(random.randint(0, 3), random.randint(0, 3))
                    goblin_j.change_direction(random.randint(0, 3), random.randint(0, 3))

                change_dir_countdown = 30
        
        # Draw background
        screen.blit(background_image, (0, 0))

        # Show level on top left
        screen.blit(level_text, (5, 5))
        
        # Show hero as long as it is alive
        if hero.show == True:
            screen.blit(hero_image, (hero.x, hero.y)) 
        
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
                    free_count += 1
                    free_countdown = 80
                    lose_sound = 0
                    level = 1
                    change_dir_countdown = 30
                    print(change_dir_countdown)
                    # Put monster back in random position
                    hero.x = random.randint(35, 445)
                    hero.y = random.randint(35, 413)
                    monster.x = random.randint(35, 445)
                    monster.y = random.randint(35, 413)
                    hero.show = True
                    goblin.direction_x = 0
                    goblin.direction_y = 0
                    goblin_b.x = 512
                    goblin_b.y = 480
                    goblin_b.show = False
                    goblin_c.x = 512
                    goblin_c.y = 480
                    goblin_c.show = False
                    goblin_d.x = 512
                    goblin_d.y = 480
                    goblin_d.show = False
                    goblin_e.x = 512
                    goblin_e.y = 480
                    goblin_e.show = False
                    goblin_f.x = 512
                    goblin_f.y = 480
                    goblin_f.show = False
                    goblin_g.x = 512
                    goblin_g.y = 480
                    goblin_g.show = False
                    goblin_h.x = 512
                    goblin_h.y = 480
                    goblin_h.show = False
                    goblin_i.x = 512
                    goblin_i.y = 480
                    goblin_i.show = False
                    goblin_j.x = 512
                    goblin_j.y = 480
                    goblin_j.show = False

        # Show monster as long as hero does not catch
        if monster.show == True:        
            screen.blit(monster_image, (monster.x, monster.y))

        # When catch a monster, play sound effect, put text, end game
        else:
            if level <= 5:
                if win_sound == 0:
                    win.play()
                    win_sound = 1
                screen.blit(win_text, (140, 224))
                goblin.x = 512
                goblin.y = 480
                goblin_b.x = 512
                goblin_b.y = 480
                goblin_c.x = 512
                goblin_c.y = 480
                goblin_d.x = 512
                goblin_d.y = 480
                goblin_e.x = 512
                goblin_e.y = 480
                goblin_f.x = 512
                goblin_f.y = 480
                goblin_g.x = 512
                goblin_g.y = 480
                goblin_h.x = 512
                goblin_h.y = 480
                goblin_i.x = 512
                goblin_i.y = 480
                goblin_j.x = 512
                goblin_j.y = 480
                if level == 5:
                    level += 1
            
            # Play again when ENTER is pressed
            # Each level, increase goblin by 1
            # Goblins stop for a while before moving when starting new game
            if level <= 5:   
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        free_count += 1
                        free_countdown = 80
                        win_sound = 0
                        level += 1
                        change_dir_countdown = 30
                        monster.show = True
                        monster.x = random.randint(35, 445)
                        monster.y = random.randint(35, 413)
                        goblin.show = True
                        goblin.x = random.randint(35, 445)
                        goblin.y = random.randint(35, 413)
                        goblin.direction_x = 0
                        goblin.direction_y = 0
                        if level >= 2:
                            goblin_b.show = True
                            goblin_b.x = random.randint(35, 445)
                            goblin_b.y = random.randint(35, 413)
                            goblin_b.direction_x = 0
                            goblin_b.direction_y = 0
                            goblin_c.show = True
                            goblin_c.x = random.randint(35, 445)
                            goblin_c.y = random.randint(35, 413)
                            goblin_c.direction_x = 0
                            goblin_c.direction_y = 0
                            if level >= 3:
                                goblin_d.show = True
                                goblin_d.x = random.randint(35, 445)
                                goblin_d.y = random.randint(35, 413)
                                goblin_d.direction_x = 0
                                goblin_d.direction_y = 0
                                goblin_e.show = True
                                goblin_e.x = random.randint(35, 445)
                                goblin_e.y = random.randint(35, 413)
                                goblin_e.direction_x = 0
                                goblin_e.direction_y = 0
                                if level >= 4:
                                    goblin_f.show = True
                                    goblin_f.x = random.randint(35, 445)
                                    goblin_f.y = random.randint(35, 413)
                                    goblin_f.direction_x = 0
                                    goblin_f.direction_y = 0
                                    goblin_g.show = True
                                    goblin_g.x = random.randint(35, 445)
                                    goblin_g.y = random.randint(35, 413)
                                    goblin_g.direction_x = 0
                                    goblin_g.direction_y = 0
                                    if level >= 5:
                                        goblin_h.show = True
                                        goblin_h.x = random.randint(35, 445)
                                        goblin_h.y = random.randint(35, 413)
                                        goblin_h.direction_x = 0
                                        goblin_h.direction_y = 0
                                        goblin_i.show = True
                                        goblin_i.x = random.randint(35, 445)
                                        goblin_i.y = random.randint(35, 413)
                                        goblin_i.direction_x = 0
                                        goblin_i.direction_y = 0
                                        goblin_j.show = True
                                        goblin_j.x = random.randint(35, 445)
                                        goblin_j.y = random.randint(35, 413)
                                        goblin_j.direction_x = 0
                                        goblin_j.direction_y = 0
                                                                   
        # Show goblins
        if goblin.show == True:
            screen.blit(goblin_image, (goblin.x, goblin.y))
        if goblin_b.show == True:
            screen.blit(goblin_image, (goblin_b.x, goblin_b.y))
        if goblin_c.show == True:
            screen.blit(goblin_image, (goblin_c.x, goblin_c.y))
        if goblin_d.show == True:
            screen.blit(goblin_image, (goblin_d.x, goblin_d.y))
        if goblin_e.show == True:
            screen.blit(goblin_image, (goblin_e.x, goblin_e.y))
        if goblin_f.show == True:
            screen.blit(goblin_image, (goblin_f.x, goblin_f.y))
        if goblin_g.show == True:
            screen.blit(goblin_image, (goblin_g.x, goblin_g.y))
        if goblin_h.show == True:
            screen.blit(goblin_image, (goblin_h.x, goblin_h.y))
        if goblin_i.show == True:
            screen.blit(goblin_image, (goblin_i.x, goblin_i.y))
        if goblin_j.show == True:
            screen.blit(goblin_image, (goblin_j.x, goblin_j.y))
        
        # Game over text after beating level 10
        # Ask player to player to press ENTER to play again
        if level == 6:
            level_text = levelfont.render('Game Over', 1, (255, 255, 255))
            screen.blit(level_text, (5, 5))
            screen.blit(caught_text, (120, 180))
            screen.blit(over_text, (180, 220))
            screen.blit(again_text, (140, 270))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    level = 0
        
        # Game display
        pygame.display.update()
        clock.tick(60)
    
    pygame.quit()

if __name__ == '__main__':
    main()