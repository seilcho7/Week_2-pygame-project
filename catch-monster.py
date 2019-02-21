import pygame

def main():
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    
    # Load background image
    background_image = pygame.image.load('images/background.png')
    
    # Load hero image
    hero_image = pygame.image.load('images/hero.png')

    # Load monster image
    monster_image = pygame.image.load('images/monster.png')

    # Game initialization
    # Set initial location of hero
    hero_x = 240
    hero_y = 224
    
    # Set initial location of monster
    monster_x = 241
    monster_y = 112

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.fill(blue_color)
        screen.blit(background_image, [0, 0])
        screen.blit(hero_image, [hero_x, hero_y])
        screen.blit(monster_image, [monster_x, monster_y])
        
        # Game display
        pygame.display.update()
        clock.tick(60)

        # Monster move to right and wrap around to the left edge 
        # of the screen if he goes off the right side
        if he goes off screen
        monster_x += 1
        if monster_x > 512:
            monster_x = 1

    pygame.quit()

if __name__ == '__main__':
    main()
