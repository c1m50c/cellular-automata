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
WIDTH, HEIGHT = 640, 640
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
CELL_SIZE: int = 32

# Simulation Variables #
iterations: int = 0
show_grid: bool = True
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
    x -= CELL_SIZE // 2
    y -= CELL_SIZE // 2
    x = CELL_SIZE * round(x / CELL_SIZE)
    y = CELL_SIZE * round(y / CELL_SIZE)
    return (x, y)


def simulate():
    global iterations
    global cells
    
    new_cells = CellContainer()
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            neighbors = cells.get_neighbors((x, y), CELL_SIZE)
            n: int = len(neighbors)
            cell: Cell = cells.get_cell_at_position((x, y))
            
            if cell:
                if n == 2 or n == 3:
                    if x >= 0 and y >= 0 and x <= WIDTH and y <= HEIGHT:
                        new_cells.add(Cell(position=(x, y)))
            elif n == 3 and not cell: # Cell Revives
                if x >= 0 and y >= 0 and x <= WIDTH and y <= HEIGHT:
                    new_cells.add(Cell(position=(x, y)))
    cells = new_cells
    iterations += 1


def main():
    global show_grid
    pygame.display.set_caption("Cellular Automata")
    simulating: bool = False
    
    while True:
        SCREEN.fill(BACKGROUND_COLOR)
        draw_cells()
        
        if show_grid:
            draw_grid()
        
        x, y = get_cell_at_mouse_pos()
        
        if simulating:
            CLOCK.tick(12)
            simulate()
            if len(cells) == 0:
                print(f"Ending the Simulation with {iterations} Iterations.")
                simulating = False
        else:
            selected_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(SCREEN, SELECTED_CELL_COLOR, selected_rect, 2)
        
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return
        
        if not simulating and event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == 1: # Left Mouse Button Down
                if x >= 0 and y >= 0 and x <= WIDTH and y <= HEIGHT:
                    print(f"Placing Cell @ {x, y}")
                    cells.add(Cell(position=(x, y)))
            elif event.button == 3: # Right Mouse Button Down
                cell = cells.get_cell_at_position((x, y))
                if cell:
                    print(f"Removing Cell @ {x, y}")
                    cells.remove(cells.get_cell_at_position((x, y)))
        elif not simulating and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                print("Clearing Grid...")
                cells.clear()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print(f"Ending the Simulation with {iterations} Iterations.")
                simulating = False
            elif event.key == pygame.K_SPACE:
                print("Toggling the Simulation...")
                simulating = not simulating
            elif event.key == pygame.K_g:
                print("Toggling Grid Display...")
                show_grid = not show_grid
        
        pygame.display.flip()


if __name__ == "__main__":
    main()