from typing import Tuple


class Cell:
    """
        Cell class for simulating cellular automata.
        
        ## Fields
        ```py
        position: Tuple[int, int] = (0, 0) # Position of the Cell within the grid.
        ```
    """
    
    position: Tuple[int, int]
    
    __slots__ = "position"
    
    def __init__(self, position: Tuple[int, int] = (0, 0)) -> None:
        """
            Cell class for simulating cellular automata.
            
            ## Parameters
            ```py
            position: Tuple[int, int] = (0, 0) # Position of the Cell within the grid.
            ```
        """
        
        self.position = position