from dataclasses import dataclass, field
from typing import List, Optional, Dict
from RFEM.BasicObjects.node import Node
from RFEM.BasicObjects.material import Material
from RFEM.BasicObjects.line import Line
@dataclass
class DefMaterial:
    id: int
    name: str
    def __post_init__(self):
        Material(
            no=self.id,
            name=self.name,
         )

@dataclass
class AllMaterials:
    all_materials:  Optional[Dict[str, DefMaterial]] = field(default=None)

@dataclass
class DefNode:
    id: int
    coordinate_X: float
    coordinate_Y: float
    coordinate_Z: float

    def __post_init__(self):
        Node(coordinate_X=self.coordinate_X,
             coordinate_Y=self.coordinate_Y,
             coordinate_Z=self.coordinate_Z,
             no=self.id)


@dataclass
class AllNodes:
    all_ids: Optional[List[int]] = field(default=None)
    all_nodes:  Optional[List[DefNode]] = field(default=None)

    def add_node(self,
                 coordinate_X: float,
                 coordinate_Y: float,
                 coordinate_Z: float,
                 id: Optional[int]):
        _id = id if (id and id not in self.all_ids) else self.all_ids.append(max(self.all_ids) + 1)
        self.all_ids = _id
        self.all_nodes = self.all_nodes.append(DefNode(coordinate_X=coordinate_X,
                                                       coordinate_Y=coordinate_Y,
                                                       coordinate_Z=coordinate_Z,
                                                       id=_id))





# @dataclass
# class AllIds:
#     materials: Optional[List[int]] = field(default=None)
#     sections: Optional[List[int]] = field(default=None)
#     thicknesses: Optional[List[int]] = field(default=None)
#     nodes: Optional[List[int]] = field(default=None)
#     lines: Optional[List[int]] = field(default=None)
#     members: Optional[List[int]] = field(default=None)
#     surfaces: Optional[List[int]] = field(default=None)
#     openings: Optional[List[int]] = field(default=None)
#
#     def add_node(self, coordinate_X: float, coordinate_Y: float, coordinate_Z: float, no: Optional[int]):
#         self.nodes = self.nodes.append(max(self.nodes)+1)
#         DefNode(coordinate_X=coordinate_X,
#                        coordinate_Y=coordinate_Y,
#                        coordinate_Z=coordinate_Z,
#                        no=no if no else max(self.nodes))








