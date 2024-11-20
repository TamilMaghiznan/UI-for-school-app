import pygame
import json
import os

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FONT_SIZE = 30
JSON_FILE = "Database/homework_data.json"

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 122, 255)
LIGHT_GRAY = (220, 220, 220)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Homework Manager with Rectangles")
font = pygame.font.Font(None, FONT_SIZE)

# Load or initialize homework data
if os.path.exists(JSON_FILE):
    with open(JSON_FILE, "r") as file:
        homework_data = json.load(file)
else:
    homework_data = {"homeworks": []}

def save_homework_data():
    with open(JSON_FILE, "w") as file:
        json.dump(homework_data, file, indent=4)

def draw_multiline_text_with_rect(surface, text, start_pos, line_height, text_color=BLACK, rect_color=LIGHT_GRAY, padding=10):
    """
    Render multiline text on a Pygame surface with a rectangle below the text.
    """
    lines = text.split('\n')  # Split text into lines by \n
    x, y = start_pos

    # Calculate the rectangle's size
    rect_width = max(font.size(line)[0] for line in lines) + padding * 2
    rect_height = (line_height * len(lines)) + padding * 2
    rect = pygame.Rect(x - padding, y - padding, rect_width, rect_height)

    # Draw the rectangle
    pygame.draw.rect(surface, rect_color, rect)

    # Draw each line of text
    for line in lines:
        text_surface = font.render(line, True, text_color)
        surface.blit(text_surface, (x, y))
        y += line_height  # Move down for the next line

    # Return the height of the rectangle for further positioning
    return rect_height + padding

def main():
    running = True

    while running:
        screen.fill(WHITE)

        # Display homework text with rectangles
        y_offset = 20
        draw_multiline_text_with_rect(screen, "Homework List:", (20, y_offset), FONT_SIZE + 5, text_color=BLACK, rect_color=WHITE)
        y_offset += FONT_SIZE + 20

        for hw in homework_data["homeworks"]:
            rect_height = draw_multiline_text_with_rect(screen, hw, (20, y_offset), FONT_SIZE + 5)
            y_offset += rect_height + 10  # Space between homeworks

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
