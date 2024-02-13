import pygame

def main():
    
    WIDTH = 800
    HEIGHT = 800 

    pygame.init()
    pygame.display.set_caption("Sanek")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    blockWidth = 40
    blockHeight = 40

    snakeX = 400;
    snakeY = 400;
    
    directionUp = False
    directionDown = False
    directionRight = True
    directionLeft = False


    time = 0;

    while running:
        
        time = time + int(clock.get_time())

        screen.fill("purple")

        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if keys[pygame.K_q]:
            running = False

        for x in range(int(WIDTH / blockWidth)):
            for y in range(int(HEIGHT / blockHeight)):
                rect = pygame.Rect(x * blockWidth, y * blockHeight, blockWidth, blockHeight)
                pygame.draw.rect(screen, "black", rect, 1)
    
        if keys[pygame.K_UP]:
            directionUp = True
            directionDown = False
            directionRight = False 
            directionLeft = False

        if keys[pygame.K_DOWN]:
            directionUp = False
            directionDown = True 
            directionRight = False 
            directionLeft = False

        if keys[pygame.K_RIGHT]:
            directionUp = False 
            directionDown = False
            directionRight = True 
            directionLeft = False

        if keys[pygame.K_LEFT]:
            directionUp = False
            directionDown = False
            directionRight = False 
            directionLeft = True

        if time > 100:
            if directionRight:
                snakeX = snakeX + blockWidth
            if directionLeft:
                snakeX = snakeX - blockWidth
            if directionUp:
                snakeY = snakeY - blockHeight
            if directionDown:
                snakeY = snakeY + blockHeight

            time = 0

        rect = pygame.Rect(snakeX, snakeY, blockWidth, blockHeight)
        pygame.draw.rect(screen, "green", rect)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
