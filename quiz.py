from minigames import toothbrush_example1, toothbrush_example2, toothbrush_example3, laundry_example1, laundry_example2, laundry_example3, deoderant_example1, deoderant_example2, deoderant_example3
import random
from ai import generate_ai
import pygame
from loader import read_settings


# Define the font and font size to use for the tips
FONT_SIZE = 24
font = pygame.font.SysFont(None, FONT_SIZE)

# Define the colors to use for the tips
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

def draw_tip(tip, x, y, color):
    # Render the tip as a Pygame surface
    tip_surface = font.render(tip, True, color)
    
    # Draw the tip on the screen
    screen.blit(tip_surface, (x, y))

def quiz_func():
    # get a random toothbrush tip, laundry tip, and deoderant tip for a total of 3 tips
    toothbrush_tips = [toothbrush_example1, toothbrush_example2, toothbrush_example3]
    laundry_tips = [laundry_example1, laundry_example2, laundry_example3]
    deoderant_tips = [deoderant_example1, deoderant_example2, deoderant_example3]
    random_toothbrush_tip = random.choice(toothbrush_tips)
    random_laundry_tip = random.choice(laundry_tips)
    random_deoderant_tip = random.choice(deoderant_tips)

    false_toothbrush_tip = generate_ai("You are a video game character giving obviously false tips on how to brush their teeth effectively.", "Give the user 3 short obviously false tips in point form on how to brush their teeth more effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")
    false_laundry_tip = generate_ai("You are a video game character giving obviously false tips on how to do laundry effectively.", "Give the user 3 short obviously false tips in point form on how to do their laundry more effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")
    false_deoderant_tip = generate_ai("You are a video game character giving obviously false tips on how to use deoderant effectively.", "Give the user 3 short obviously false tips in point form on how to use deoderant more effectively. Each tip should only be 10-15 words long. Don't include backslash n for new lines in the answer.")

    # Combine the tips into a single list
    tips = [random_toothbrush_tip] + [random_laundry_tip] + [random_deoderant_tip] + false_toothbrush_tip.split("\\n") + false_laundry_tip.split("\\n") + false_deoderant_tip.split("\\n")
    
    # Shuffle the tips
    random.shuffle(tips)
    
    # Keep track of the user's selections and score
    selected_tips = []
    score = 0
    
    # Draw the tips on the screen
    x = 50
    y = 50
    for tip in tips:
        color = WHITE
        if tip in selected_tips:
            color = BLACK
        draw_tip(tip, x, y, color)
        y += FONT_SIZE + 10
    
    # Update the Pygame display
    pygame.display.update()
    
    # Wait for the user to make selections
    while len(selected_tips) < 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the position of the mouse click
                pos = pygame.mouse.get_pos()
                
                # Check if the mouse click is on a tip
                for i, tip in enumerate(tips):
                    tip_x = x
                    tip_y = y + (FONT_SIZE + 10) * i
                    tip_width, tip_height = font.size(tip)
                    if pos[0] >= tip_x and pos[0] < tip_x + tip_width and pos[1] >= tip_y and pos[1] < tip_y + tip_height:
                        # Add the selected tip to the list of selected tips
                        if tip not in selected_tips:
                            selected_tips.append(tip)
    
    # Check the user's score
    for selected_tip in selected_tips:
        if selected_tip in [random_toothbrush_tip, random_laundry_tip, random_deoderant_tip]:
            score += 1
    
    # Print the user's score
    print(f"Score: {score}/3")

# Run the quiz
quiz_func()

# Quit Pygame
pygame.quit()