import pygame
import random

def main():
 
    WIDTH = 800
    HEIGHT = 800 

    blockWidth = 40
    blockHeight = 40

    RANGE = (blockWidth, WIDTH - blockWidth // 2, blockWidth)
   
    length = 1
    pygame.init()
    pygame.display.set_caption("Sanek")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    
    snake_dir = (0, 0)
    foodX = random.randrange(*RANGE)
    foodY = random.randrange(*RANGE)

    snake = pygame.rect.Rect([0, 0, blockWidth, blockHeight])
    snakeBody = [snake.copy()]

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
            snake_dir = (0, -blockHeight)

        if keys[pygame.K_DOWN]:
            snake_dir = (0, blockHeight)

        if keys[pygame.K_RIGHT]:
            snake_dir = (blockWidth, 0)

        if keys[pygame.K_LEFT]:
            snake_dir = (-blockWidth, 0)

        if time > 100:
           snake.move_ip(snake_dir)
           snakeBody.append(snake.copy())
           snakeBody = snakeBody[-length:]

           time = 0

        if foodX == snake.x and foodY == snake.y:
            length += 1
            print(length)
            foodX = random.randrange(*RANGE)
            foodY = random.randrange(*RANGE)

        
        for segment in snakeBody:
            pygame.draw.rect(screen, "green", segment)
        
        #draw
        rectFood = pygame.Rect(foodX, foodY, blockWidth, blockHeight)
        pygame.draw.rect(screen, "red", rectFood)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
