from typing import Iterable, TypeVar, Union, Tuple
from cell import Cell


_T = TypeVar("_T")


class CellContainer(set):
    """
        A `set` specifically created for containing `Cell`s.
    """
    
    def __init__(self, iterable: Iterable[_T] = ...) -> None:
        super().__init__()
    
    def add(self, element: _T) -> None:
        if isinstance(element, Cell):
            super().add(element)
    
    def get_cell_at_position(self, position: Tuple[int, int]) -> Union[Cell, None]:
        for c in self:
            if c.position == position:
                return c
        return None

    def get_neighbors(self, position: Tuple[int, int], cell_size: int) -> Tuple[Cell, Cell, Cell, Cell]:
        x, y = position
        
        t: Cell = self.get_cell_at_position(position=(x, y + cell_size)) # Top
        b: Cell = self.get_cell_at_position(position=(x, y - cell_size)) # Bottom
        l: Cell = self.get_cell_at_position(position=(x + cell_size, y)) # Left
        r: Cell = self.get_cell_at_position(position=(x - cell_size, y)) # Right
        
        return (t, b, l, r)