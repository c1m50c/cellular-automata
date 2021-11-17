from cell_container import CellContainer
from typing import Tuple
from cell import Cell
import pygame


# Color Settings #
BACKGROUND_COLOR: Tuple[int, int, int] = (16, 16, 16)
GRID_COLOR: Tuple[int, int, int] = (64, 64, 64)
CELL_COLOR: Tuple[int, int, int] = (222, 186, 80)
SELECTED_CELL_COLOR: Tuple[int, int, int] = (248, 248, 248)

# Misc Settings #
WIDTH, HEIGHT = 1024, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
CELL_SIZE: int = 32

# Simulation Variables #
CELL_X, CELL_Y = 0, 0
cells: CellContainer[Cell] = CellContainer()


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
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            neighbors = cells.get_neighbors((x, y), CELL_SIZE)
            n: int = len(neighbors)
            cell: Cell = cells.get_cell_at_position((x, y))
            
            if n < 2 and cell: # Cell Dies
                cells.remove(cell)
            elif (n == 2 or n == 3) and cell: # Cell Survives
                continue
            elif n > 3 and cell: # Cell Dies
                cells.remove(cell)
            elif n == 3 and not cell: # Cell Revives
                cells.add(Cell(position=(x, y)))


def main():
    pygame.display.set_caption("Cellular Automata")
    simulating: bool = False
    
    while True:
        SCREEN.fill(BACKGROUND_COLOR)
        draw_cells()
        draw_grid()
        
        x, y = get_cell_at_mouse_pos()
        
        if simulating:
            simulate()
        else:
            selected_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(SCREEN, SELECTED_CELL_COLOR, selected_rect, 2)
        
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return
        
        if not simulating and event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == 1: # Left Mouse Button Down
                print(f"Placing Cell @ {x, y}")
                cells.add(Cell(position=(x, y)))
            elif event.button == 3: # Right Mouse Button Down
                cell = cells.get_cell_at_position((x, y))
                if cell:
                    print(f"Removing Cell @ {x, y}")
                    cells.remove(cells.get_cell_at_position((x, y)))
        elif not simulating and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                simulating = True
        
        pygame.display.flip()


if __name__ == "__main__":
    main()