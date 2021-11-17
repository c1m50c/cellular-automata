from __future__ import annotations
from typing import Iterable, TypeVar, Union, Set, Tuple
from cell import Cell


_T = TypeVar("_T")


class CellContainer(set):
    """
        A `set` specifically created for containing `Cell`s.
    """
    
    def __init__(self, iterable: Iterable[_T] = ...) -> None:
        super().__init__()
    
    def add(self, element: _T) -> None:
        if element is None:
            return
        if isinstance(element, Cell):
            super().add(element)
    
    def get_cell_at_position(self, position: Tuple[int, int]) -> Union[Cell, None]:
        for c in self:
            if c.position == position:
                return c
        return None

    def get_neighbors(self, position: Tuple[int, int], cell_size: int) -> CellContainer:
        cc: CellContainer = CellContainer()
        x, y = position
        
        t: Cell = self.get_cell_at_position(position=(x, y + cell_size)) # Top
        b: Cell = self.get_cell_at_position(position=(x, y - cell_size)) # Bottom
        l: Cell = self.get_cell_at_position(position=(x + cell_size, y)) # Left
        r: Cell = self.get_cell_at_position(position=(x - cell_size, y)) # Right
        
        tl: Cell = self.get_cell_at_position(position=(x - cell_size, y + cell_size)) # Top Left
        tr: Cell = self.get_cell_at_position(position=(x + cell_size, y + cell_size)) # Top Right
        bl: Cell = self.get_cell_at_position(position=(x - cell_size, y - cell_size)) # Bottom Left
        br: Cell = self.get_cell_at_position(position=(x + cell_size, y - cell_size)) # Bottom Right
        
        cc.add(t)
        cc.add(b)
        cc.add(l)
        cc.add(r)
        cc.add(tl)
        cc.add(tr)
        cc.add(bl)
        cc.add(br)
        
        return cc