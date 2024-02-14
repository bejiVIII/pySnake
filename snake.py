import pygame
import random

def main():
 
    WIDTH = 800
    HEIGHT = 800 

    blockWidth = 40
    blockHeight = 40

    RANGE = (blockWidth, WIDTH - blockWidth // 2, blockWidth)
   
    length = 2
    pygame.init()
    pygame.font.init()

    Font=pygame.font.SysFont('timesnewroman',  30)
    pygame.display.set_caption("Sanek")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    
    snake_dir = (blockWidth, 0)
    foodX = random.randrange(*RANGE)
    foodY = random.randrange(*RANGE)

    snake = pygame.rect.Rect([0, 0, blockWidth, blockHeight])
    snakeBody = [snake.copy()]

    time = 0;
    score = length

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
        
        #TODO: check conditions
        if keys[pygame.K_UP] and snake_dir != (0, blockHeight):
            snake_dir = (0, -blockHeight)

        if keys[pygame.K_DOWN] and snake_dir != (0, -blockHeight):
            snake_dir = (0, blockHeight)

        if keys[pygame.K_RIGHT] and snake_dir != (-blockWidth, 0):
            snake_dir = (blockWidth, 0)

        if keys[pygame.K_LEFT] and snake_dir != (blockWidth, 0):
            snake_dir = (-blockWidth, 0)

        if time > 100:
           snake.move_ip(snake_dir)
           snakeBody.append(snake.copy())
           snakeBody = snakeBody[-length:]

           time = 0
         
        text = Font.render('Score: ' + str(score), True, (0, 255, 0))
        screen.blit(text, (0, 0))

        if foodX == snake.x and foodY == snake.y:
            length += 1
            score += 1
            print(score)

            foodX = random.randrange(*RANGE)
            foodY = random.randrange(*RANGE)
            
            check = True 
            while check:
                for segment in snakeBody:
                    print(segment)
                    if segment.x == foodX or segment.y == foodY:
                        foodX = random.randrange(*RANGE)
                        foodY = random.randrange(*RANGE)
                    else:
                        check = False

        #TODO: check snake collision with itself 
        #TODO: snake reaches the end of the screen

        #draw
        for segment in snakeBody:
            pygame.draw.rect(screen, "green", segment)
        
        rectFood = pygame.Rect(foodX, foodY, blockWidth, blockHeight)
        pygame.draw.rect(screen, "red", rectFood)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
