from __future__ import annotations
from typing import Tuple, Any


class Cell:
    """
        Cell class for simulating cellular automata.
        
        ## Fields
        ```py
        position: Tuple[int, int] = (0, 0) # Position of the Cell within the grid.
        material_id: int = 0 # ID of the Cell's material.
        ```
    """
    
    position: Tuple[int, int]
    material_id: int
    
    __slots__ = "position", "material_id"
    
    def __init__(self, position: Tuple[int, int] = (0, 0), material_id: int = 0) -> None:
        """
            Cell class for simulating cellular automata.
            
            ## Parameters
            ```py
            position: Tuple[int, int] = (0, 0) # Position of the Cell within the grid.
            material_id: int = 0 # ID of the Cell's material.
            ```
        """
        
        self.position = position
        self.material_id = material_id
    
    def __setattr__(self, name: str, value: Any) -> None:
        if name == "material_id" and isinstance(value, int):
            if value >= 0:
                self.material_id = value
            else:
                raise AttributeError(f"Cannot set attribute {name} to a non-positive integer.")
        elif name == "position" and isinstance(value, Tuple[int, int]):
            self.position = value
        else:
            raise AttributeError(f"Attribute {name} was either not found or of invalid type.")
    
    def __eq__(self, other: Cell) -> bool:
        return self.material_id == other.material_id and self.position == other.position

    def __ne__(self, other: object) -> bool:
        return self.material_id != other.material_id and self.position != other.position
    
    def __hash__(self) -> int:
        return self.position.__hash__() + self.material_id.__hash__()
    
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f"({self.material_id} @ {self.position})"