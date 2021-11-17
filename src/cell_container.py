from __future__ import annotations
from typing import Iterable, TypeVar, Union, Tuple
from cell import Cell


_T = TypeVar("_T")


class CellContainer(set):
    """
        A `set` specifically created for containing `Cell`s.
    """
    
    def __init__(self, iterable: Iterable[_T] = ...) -> None:
        super().__init__()
    
    def add(self, element: Cell, extents: Tuple[int, int]) -> None:
        if element is None:
            return
        if isinstance(element, Cell):
            x, y = element.position
            ex, ey = extents
            if x >= 0 and y >= 0 and x <= ex and y <= ey:
                super().add(element)
    
    def get_cell_at_position(self, position: Tuple[int, int]) -> Union[Cell, None]:
        for c in self:
            if c.position == position:
                return c
        return None

    def get_neighbors(self, position: Tuple[int, int], cell_size: int, extents: Tuple[int, int]) -> CellContainer:
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
        
        cc.add(t, extents)
        cc.add(b, extents)
        cc.add(l, extents)
        cc.add(r, extents)
        cc.add(tl, extents)
        cc.add(tr, extents)
        cc.add(bl, extents)
        cc.add(br, extents)
        
        return cc