from dataclasses import dataclass
from utils.skeleton import get_node_grid
from utils.def_data_classes.node import AllNodes
from utils.def_data_classes.line import AllLines
from utils.def_data_classes.surface import AllSurfaces
from utils.def_data_classes.opening import AllOpening
from utils.def_data_classes.material import AllMaterial
from utils.def_data_classes.thickness import AllThicknesses
from utils.def_data_classes.section import AllSections
from utils.def_data_classes.member import AllMembers
from typing import Type, Any

@dataclass
class AllBasicObjects:
    all_nodes: Any = AllNodes()
    all_lines: Any = AllLines()
    all_surfaces: Any = AllSurfaces()
    all_openings: Any = AllOpening()
    all_materials: Any = AllMaterial()
    all_thicknesses: Any = AllThicknesses()
    all_sections: Any = AllSections()
    all_members: Any = AllMembers()
