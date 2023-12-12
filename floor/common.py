from utils.def_data_classes.node import AllNodes, DefNode
from utils.def_data_classes.surface import AllSurfaces, DefLoadDistribution
from utils.def_data_classes.opening import AllOpening, DefOpening
from utils.def_data_classes.material import AllMaterial
from utils.def_data_classes.thickness import AllThicknesses
from utils.def_data_classes.line import AllLines
from utils.def_data_classes.section import AllSections
from utils.def_data_classes.member import AllMembers
from typing import List, Tuple


class CommonForFloor:
    def __init__(self, all_nodes: AllNodes,
                 all_lines: AllLines,
                 all_surfaces: AllSurfaces,
                 all_opening: AllOpening,
                 all_material: AllMaterial,
                 all_thicknesses: AllThicknesses,
                 all_sections: AllSections,
                 all_members: AllMembers):
        self.all_nodes = all_nodes
        self.all_lines = all_lines
        self.all_surfaces = all_surfaces
        self.all_opening = all_opening
        self.all_material = all_material
        self.all_thicknesses = all_thicknesses
        self.all_sections = all_sections
        self.all_members = all_members

    @staticmethod
    def get_corners_of_the_surface_with_offset(corners_of_the_surface: List[DefNode],
                                               offset_x: float = 0.0,  # m
                                               offset_y: float = 0.0,  # m
                                               offset_z: float = 0.0, ) -> List[DefNode]:
        new_corners_of_the_surface = []
        for _value in corners_of_the_surface:
            new_corners_of_the_surface.append(DefNode(_value.coordinate_x + offset_x,
                                                      _value.coordinate_y + offset_y,
                                                      _value.coordinate_z + offset_z))
        return new_corners_of_the_surface

    def create_first_left_side_with_offset(self,
                                           offset_x: float = 0.0,  # m
                                           offset_y: float = 0.0,  # m
                                           offset_z: float = 0.0, ) -> None:
        corners_of_the_surface = [DefNode(0, 0, 0),
                                  DefNode(0, 0, -3.34),
                                  DefNode(0, 11, -3.34),
                                  DefNode(0, 11, 0)]
        new_corners_of_the_surface = self.get_corners_of_the_surface_with_offset(
            corners_of_the_surface=corners_of_the_surface,
            offset_x=offset_x,
            offset_y=offset_y,
            offset_z=offset_z
        )
        self.all_surfaces.create_surface_by_nodes(
            corners_of_the_surface=new_corners_of_the_surface,
            all_lines=self.all_lines,
            all_nodes=self.all_nodes,
            thickness=self.all_thicknesses.uniform_d_300_c20slash25.id,
        )

    def create_base_with_offset(self,
                                offset_x: float = 0.0,  # m
                                offset_y: float = 0.0,  # m
                                offset_z: float = 0.0) -> None:
        corners_of_the_surface = [DefNode(0, 0, 0),
                                  DefNode(25, 0, 0),
                                  DefNode(25, 11, 0),
                                  DefNode(0, 11, 0)]
        new_corners_of_the_surface = self.get_corners_of_the_surface_with_offset(
            corners_of_the_surface=corners_of_the_surface,
            offset_x=offset_x,
            offset_y=offset_y,
            offset_z=offset_z
        )
        self.all_surfaces.create_surface_by_nodes(
            corners_of_the_surface=new_corners_of_the_surface,
            all_lines=self.all_lines,
            all_nodes=self.all_nodes,
            thickness=self.all_thicknesses.uniform_d_300_c20slash25.id,
        )

    def create_window_with_glass(self, corners_of_the_opening: List[DefNode]) -> Tuple[DefOpening, DefLoadDistribution]:
        window = self.all_opening.create_opening_by_nodes(
            corners_of_the_opening=corners_of_the_opening,
            all_nodes=self.all_nodes,
            all_lines=self.all_lines
        )
        window_glass = self.all_surfaces.create_load_distribution_by_nodes(
            corners_of_the_surface=corners_of_the_opening,
            all_nodes=self.all_nodes,
            all_lines=self.all_lines
        )
        return window, window_glass

    def copy_and_offset_window_with_glass(self,
                                          def_opening: DefOpening,
                                          def_load_distribution: DefLoadDistribution,
                                          offset_x: float = 0.0,  # m
                                          offset_y: float = 0.0,  # m
                                          offset_z: float = 0.0,  # m
                                          ):
        self.all_opening.copy_and_offset(def_opening=def_opening,
                                         all_lines=self.all_lines,
                                         all_nodes=self.all_nodes,
                                         offset_x=offset_x,
                                         offset_y=offset_y,
                                         offset_z=offset_z)
        self.all_surfaces.copy_and_offset(def_surface=def_load_distribution,
                                          all_lines=self.all_lines,
                                          all_nodes=self.all_nodes,
                                          offset_x=offset_x,
                                          offset_y=offset_y,
                                          offset_z=offset_z)

    def create_back_site_without_door_with_offset(self,
                                                  offset_x: float = 0.0,  # m
                                                  offset_y: float = 0.0,  # m
                                                  offset_z: float = 0.0,  # m
                                                  ) -> None:
        corners_of_the_back_surface = [DefNode(0, 0, 0),
                                       DefNode(0, 0, -3.34),
                                       DefNode(25, 0, -3.34),
                                       DefNode(25, 0, 0)]
        new_corners_of_the_back_surface = self.get_corners_of_the_surface_with_offset(
            corners_of_the_surface=corners_of_the_back_surface,
            offset_y=offset_y,
            offset_x=offset_x,
            offset_z=offset_z
        )
        self.all_surfaces.create_surface_by_nodes(
            corners_of_the_surface=new_corners_of_the_back_surface,
            all_lines=self.all_lines,
            all_nodes=self.all_nodes,
            thickness=self.all_thicknesses.uniform_d_300_c20slash25.id,
        )
        window_corners_of_the_opening = [DefNode(0.75, 0, -1.23),
                                         DefNode(4.25, 0, -1.23),
                                         DefNode(4.25, 0, -2.75),
                                         DefNode(0.75, 0, -2.75)]
        new_window_corners_of_the_opening = self.get_corners_of_the_surface_with_offset(
            corners_of_the_surface=window_corners_of_the_opening,
            offset_y=offset_y,
            offset_x=offset_x,
            offset_z=offset_z
        )
        window_01, window_glass_01 = self.create_window_with_glass(
            corners_of_the_opening=new_window_corners_of_the_opening)

        for _offset_x in [5, 10, 20]:
            self.copy_and_offset_window_with_glass(def_opening=window_01,
                                                   def_load_distribution=window_glass_01,
                                                   offset_x=_offset_x)

    def create_back_site_with_offset(self,
                                     offset_x: float = 0.0,  # m
                                     offset_y: float = 0.0,  # m
                                     offset_z: float = 0.0,  # m
                                     ) -> None:
        self.create_back_site_without_door_with_offset(offset_x=offset_x, offset_y=offset_y, offset_z=offset_z)
        back_window_corners_of_the_opening = [DefNode(15.75, 0, -1.23),
                                              DefNode(15.75, 0, -2.75),
                                              DefNode(19.25, 0, -2.75),
                                              DefNode(19.25, 0, -1.23)]
        new_back_window_corners_of_the_opening = self.get_corners_of_the_surface_with_offset(
            corners_of_the_surface=back_window_corners_of_the_opening,
            offset_x=offset_x,
            offset_z=offset_z,
            offset_y=offset_y
        )
        self.create_window_with_glass(corners_of_the_opening=new_back_window_corners_of_the_opening)

    def create_area_for_stairs_with_offset(self, offset_x: float = 0.0,  # m
                                           offset_y: float = 0.0,  # m
                                           offset_z: float = 0.0,  # m
                                           ) -> None:
        corners_of_the_left_side = [DefNode(15, 11, 0),
                                    DefNode(15, 11, -3.34),
                                    DefNode(15, 6.5, -3.34),
                                    DefNode(15, 6.5, 0)]
        new_corners_of_the_left_side = self.get_corners_of_the_surface_with_offset(
            corners_of_the_surface=corners_of_the_left_side,
            offset_x=offset_x,
            offset_z=offset_z,
            offset_y=offset_y
        )

        left_side = self.all_surfaces.create_surface_by_nodes(corners_of_the_surface=new_corners_of_the_left_side,
                                                              all_nodes=self.all_nodes,
                                                              all_lines=self.all_lines,
                                                              thickness=self.all_thicknesses.uniform_d_300_c20slash25.id
                                                              )
        self.all_surfaces.copy_and_offset(def_surface=left_side,
                                          all_lines=self.all_lines,
                                          all_nodes=self.all_nodes,
                                          offset_x=5 + offset_x)

        corners_of_the_back_side = [DefNode(15, 6.5, 0),
                                    DefNode(20, 6.5, 0),
                                    DefNode(20, 6.5, -3.34),
                                    DefNode(15, 6.5, -3.34),
                                    ]
        new_corners_of_the_back_side = self.get_corners_of_the_surface_with_offset(
            corners_of_the_surface=corners_of_the_back_side,
            offset_x=offset_x,
            offset_z=offset_z,
            offset_y=offset_y
        )

        self.all_surfaces.create_surface_by_nodes(corners_of_the_surface=new_corners_of_the_back_side,
                                                  all_nodes=self.all_nodes,
                                                  all_lines=self.all_lines,
                                                  thickness=self.all_thicknesses.uniform_d_300_c20slash25.id
                                                  )
        corners_of_the_opening_in_back_side = [DefNode(15.75, 6.5, -0.15),
                                               DefNode(19.25, 6.5, -0.15),
                                               DefNode(19.25, 6.5, -2.75),
                                               DefNode(15.75, 6.5, -2.75),
                                               ]
        new_corners_of_the_opening_in_back_side = self.get_corners_of_the_surface_with_offset(
            corners_of_the_surface=corners_of_the_opening_in_back_side,
            offset_x=offset_x,
            offset_z=offset_z,
            offset_y=offset_y
        )
        self.create_window_with_glass(corners_of_the_opening=new_corners_of_the_opening_in_back_side)
