

class MyNode:
    def __init__(self,
                 coordinate_X: float = 0.0,
                 coordinate_Y: float = 0.0,
                 coordinate_Z: float = 0.0,
                 no: int = 1,
                 ):

        self.coordinate_X = coordinate_X
        self.coordinate_Y = coordinate_Y
        self.coordinate_Z = coordinate_Z





my_node_1 = MyNode(0, 5, 5)
print(my_node_1.coordinate_Y)