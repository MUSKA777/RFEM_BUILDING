from utils.data_classes import AllNodes
from typing import List
class AllBasicObjects:

    def __int__(self):
        # self.all_material:
        self.all_nodes: AllNodes = AllNodes()


    def get_id_using_coordinates(self,
                                 all_elements: list,
                                 coordinate_X: float,
                                 coordinate_Y: float,
                                 coordinate_Z: float):
        pass
