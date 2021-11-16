from __future__ import annotations
from typing import Tuple, Any


class Cell:
    """
        Cell class for simulating cellular automata.
        
        ## Fields
        ```py
        position: Tuple[int, int] = (0, 0) # Position of the Cell within the grid.
        ```
    """
    
    position: Tuple[int, int]
    
    __slots__ = "position", "material_id"
    
    def __init__(self, position: Tuple[int, int] = (0, 0)) -> None:
        """
            Cell class for simulating cellular automata.
            
            ## Parameters
            ```py
            position: Tuple[int, int] = (0, 0) # Position of the Cell within the grid.
            ```
        """
        
        self.position = position
    
    def __eq__(self, other: Cell) -> bool:
        return self.position == other.position

    def __ne__(self, other: Cell) -> bool:
        return self.position != other.position
    
    def __hash__(self) -> int:
        return self.position.__hash__()
    
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f"({self.position})"