from RFEM.BasicObjects.node import Node
from typing import Optional

class MNode:

    def __init__(self,
                 no: Optional[int],
                 coordinate_X: float = 0.0,
                 coordinate_Y: float = 0.0,
                 coordinate_Z: float = 0.0,
                 ):
        self.coordinate_X = coordinate_X
        self.coordinate_Y = coordinate_Y
        self.coordinate_Z = coordinate_Z
        Node(no=no if no else self.get_max_no_of_node(),
             coordinate_X=coordinate_X,
             coordinate_Y=coordinate_Y,
             coordinate_Z=coordinate_Z)

    def add_node(self,
                 no: Optional[int],
                 coordinate_X: float = 0.0,
                 coordinate_Y: float = 0.0,
                 coordinate_Z: float = 0.0):
        Node(no=no if no else self.get_max_no_of_node(),
             coordinate_X=coordinate_X,
             coordinate_Y=coordinate_Y,
             coordinate_Z=coordinate_Z)
        return



    def get_max_no_of_node(self) -> int:
        pass



