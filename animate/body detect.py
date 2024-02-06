import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Ball")

# Set up the ball
ball_radius = 20
ball_color = (255, 0, 0)  # Red
ball_position = [width // 2, height // 2]
ball_speed = [5, 5]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the ball
    ball_position[0] += ball_speed[0]
    ball_position[1] += ball_speed[1]

    # Bounce off the walls
    if ball_position[0] <= 0 or ball_position[0] >= width:
        ball_speed[0] = -ball_speed[0]
    if ball_position[1] <= 0 or ball_position[1] >= height:
        ball_speed[1] = -ball_speed[1]

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (int(ball_position[0]), int(ball_position[1])), ball_radius)

    # Update the display
    pygame.display.flip()

    # Control the frames per second (FPS)
    pygame.time.Clock().tick(30)
