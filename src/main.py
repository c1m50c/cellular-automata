from typing import Tuple, Set
from cell import Cell
import pygame


BACKGROUND_COLOR: Tuple[int, int, int] = (26, 26, 26)
GRID_COLOR: Tuple[int, int, int] = (248, 248, 248)
CELL_COLOR: Tuple[int, int, int] = (0, 255, 128)
SELECTED_CELL_COLOR: Tuple[int, int, int] = (255, 0, 0)

WIDTH, HEIGHT = 1024, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CELL_SIZE: int = 32


cells: Set[Cell] = set()


def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            rect_cell = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(SCREEN, GRID_COLOR, rect_cell, 1)


def draw_cells():
    for c in cells:
        x, y = c.position
        rect_cell = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        SCREEN.fill(CELL_COLOR, rect_cell)


def get_cell_at_mouse_pos() -> Tuple[int, int]:
    x, y = pygame.mouse.get_pos()
    x = CELL_SIZE * round(x / CELL_SIZE)
    y = CELL_SIZE * round(y / CELL_SIZE)
    return (x, y)


def simulate():
    pass


def main():
    pygame.display.set_caption("Cellular Automata")
    simulating: bool = False
    
    while True:
        SCREEN.fill(BACKGROUND_COLOR)
        draw_cells()
        draw_grid()
        
        if simulating:
            simulate()
        
        x, y = get_cell_at_mouse_pos()
        selected_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(SCREEN, SELECTED_CELL_COLOR, selected_rect, 2)
        
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return
        
        if not simulating:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Left Mouse Button Down
                print(f"Placing Cell @ {x, y}")
                cells.add(Cell(position=(x, y)))
        
        pygame.display.flip()


if __name__ == "__main__":
    main()