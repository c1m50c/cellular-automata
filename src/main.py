import pygame


def main():
    BACKGROUND_COLOR: tuple[int, int, int] = (26, 26, 26)
    
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Cellular Automata")
    
    while True:
        screen.fill(BACKGROUND_COLOR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()


if __name__ == "__main__":
    main()