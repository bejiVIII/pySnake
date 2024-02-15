import pygame
import random

length = 1
score = length

#TODO   
def check():
    #right
    if snake.x + blockWidth >= WIDTH and snake_dir == (blockWidth, 0):
        print("right")
        snake.x = 0 - blockWidth
    #left
    if snake.x <= 0 and snake_dir == (-blockWidth, 0):
        print("left")
        snake.x = WIDTH
    #down
    if snake.y + blockHeight >= HEIGHT and snake_dir == (0, blockHeight):
        print("down")
        snake.y = 0 - blockHeight
    #up
    if snake.y <= 0 and snake_dir == (0, -blockHeight):
        print("up")
        snake.y = HEIGHT 

WIDTH = 800 
HEIGHT = 800 

blockWidth = 40
blockHeight = 40

RANGE = (blockWidth, WIDTH - blockWidth // 2, blockWidth)
pygame.init()
pygame.font.init()

Font=pygame.font.SysFont('timesnewroman',  30)
pygame.display.set_caption("Sanek")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

snake_dir = (0, 0)
snake = pygame.rect.Rect([0, 0, blockWidth, blockHeight])
snake.x = random.randrange(*RANGE)
snake.y = random.randrange(*RANGE)

snakeBody = []
food = pygame.rect.Rect([0, 0, blockWidth, blockHeight])


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
    
    #TODO: check conditions
    if keys[pygame.K_UP] and snake_dir != (0, blockHeight):
        snake_dir = (0, -blockHeight)

    if keys[pygame.K_DOWN] and snake_dir != (0, -blockHeight):
        snake_dir = (0, blockHeight)

    if keys[pygame.K_RIGHT] and snake_dir != (-blockWidth, 0):
        snake_dir = (blockWidth, 0)

    if keys[pygame.K_LEFT] and snake_dir != (blockWidth, 0):
        snake_dir = (-blockWidth, 0)

    #check()
    
    if snake.x >= WIDTH or snake.x < 0 or snake.y < 0 or snake.y >= HEIGHT:
        length = 1
        score = length
        snakeBody = [snake.copy()]
        snake.x = random.randrange(*RANGE)
        snake.y = random.randrange(*RANGE)
        snake_dir = (0, 0)
        foodX = random.randrange(*RANGE)
        foodY = random.randrange(*RANGE)
        
    if time > 100:
       snake.move_ip(snake_dir)
       snakeBody.append(snake.copy())
       snakeBody = snakeBody[-length:]

       time = 0
     
    text = Font.render('Score: ' + str(score), True, (0, 255, 0))
    screen.blit(text, (0, 0))

    if food.x == snake.x and food.y == snake.y:
        length += 1
        score += 1

        food.x = random.randrange(*RANGE)
        food.y = random.randrange(*RANGE)
        
    #TODO: check directions (snake can go into himself when score = 2)

    snake_eating_itself = pygame.Rect.collidelist(snake, snakeBody[:-1]) !=-1
    if snake_eating_itself:
        length = 1
        score = length
        snakeBody = [snake.copy()]
        snake_dir = (0, 0)
        snake.x = random.randrange(*RANGE)
        snake.y = random.randrange(*RANGE)
        food.x = random.randrange(*RANGE)
        food.y = random.randrange(*RANGE)
 
    food_spawn_in_snake = pygame.Rect.collidelist(food, snakeBody) !=-1
    if food_spawn_in_snake:
        food.x = random.randrange(*RANGE)
        food.y = random.randrange(*RANGE)
               
    #draw
    for segment in snakeBody:
        pygame.draw.rect(screen, "green", segment)
    
    pygame.draw.rect(screen, "red", food)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
