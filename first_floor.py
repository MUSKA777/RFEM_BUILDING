from utils.skeleton import get_node_grid
from utils.def_data_classes.node import AllNodes, DefNode
from utils.def_data_classes.line import AllLines
from utils.def_data_classes.surface import AllSurfaces
from utils.def_data_classes.opening import AllOpening
from utils.def_data_classes.material import AllMaterial
from utils.def_data_classes.thickness import AllThicknesses
from RFEM.BasicObjects.surface import Surface
from utils.def_data_classes.line import DefLine, AllLines, get_line_id_using_coordinates
from utils.def_data_classes.common import get_new_max_id
from RFEM.enums import SurfaceGeometry, SurfaceLoadDistributionDirection

class FirstFloor:
    def __init__(self, all_nodes: AllNodes,
                 all_lines: AllLines,
                 all_surfaces: AllSurfaces,
                 all_opening: AllOpening,
                 all_material: AllMaterial,
                 all_thicknesses: AllThicknesses):
        self.all_nodes = all_nodes
        self.all_lines = all_lines
        self.all_surfaces = all_surfaces
        self.all_opening = all_opening
        self.all_material = all_material
        self.all_thicknesses = all_thicknesses

    def create_basic(self) -> None:
        base_of_building = self.all_surfaces.create_surface_by_nodes(
            corners_of_the_surface=[DefNode(0, 0, 0),
                                    DefNode(25, 0, 0),
                                    DefNode(25, 11, 0),
                                    DefNode(0, 11, 0)],

            all_lines=self.all_lines,
            all_nodes=self.all_nodes,
            thickness=self.all_thicknesses.uniform_d_300_c20slash25.id,
        )
        self.all_surfaces.copy_and_offset(def_surface=base_of_building,
                                          all_lines=self.all_lines,
                                          all_nodes=self.all_nodes,
                                          offset_z=-3.34)

    def create_sides_without_windows(self) -> None:
        left_side = self.all_surfaces.create_surface_by_nodes(
            corners_of_the_surface=[DefNode(0, 0, 0),
                                    DefNode(0, 0, -3.34),
                                    DefNode(0, 11, -3.34),
                                    DefNode(0, 11, 0)],

            all_lines=self.all_lines,
            all_nodes=self.all_nodes,
            thickness=self.all_thicknesses.uniform_d_300_c20slash25.id,
        )
        self.all_surfaces.copy_and_offset(left_side,
                                          all_lines=self.all_lines,
                                          all_nodes=self.all_nodes,
                                          offset_x=25)


    def create_front_site_without_door(self, coordinate_y: int) -> None:
        self.all_surfaces.create_surface_by_nodes(
            corners_of_the_surface=[DefNode(0, coordinate_y, 0),
                                    DefNode(0, coordinate_y, -3.34),
                                    DefNode(25, coordinate_y, -3.34),
                                    DefNode(25, coordinate_y, 0)],

            all_lines=self.all_lines,
            all_nodes=self.all_nodes,
            thickness=self.all_thicknesses.uniform_d_300_c20slash25.id,
        )
        window_01 = self.all_opening.create_opening_by_nodes(
            corners_of_the_opening=[DefNode(0.75, coordinate_y, -1.23),
                                    DefNode(4.25, coordinate_y, -1.23),
                                    DefNode(4.25, coordinate_y, -2.75),
                                    DefNode(0.75, coordinate_y, -2.75)],
            all_nodes=self.all_nodes,
            all_lines=self.all_lines
        )
        window_glass_01 = self.all_surfaces.create_load_distribution_by_nodes(
            corners_of_the_surface=[DefNode(0.75, coordinate_y, -1.23),
                                    DefNode(4.25, coordinate_y, -1.23),
                                    DefNode(4.25, coordinate_y, -2.75),
                                    DefNode(0.75, coordinate_y, -2.75)],
            all_nodes=self.all_nodes,
            all_lines=self.all_lines
        )

        for _offset_x in [5, 10, 20]:
            self.all_opening.copy_and_offset(def_opening=window_01,
                                             all_lines=self.all_lines,
                                             all_nodes=self.all_nodes,
                                             offset_x=_offset_x)
            self.all_surfaces.copy_and_offset(def_surface=window_glass_01,
                                              all_lines=self.all_lines,
                                              all_nodes=self.all_nodes,
                                              offset_x=_offset_x)

    def create_front_site(self) -> None:
        self.create_front_site_without_door(coordinate_y=11)

        self.all_opening.create_opening_by_nodes(
            corners_of_the_opening=[DefNode(15.75, 11, -0.15),
                                    DefNode(19.25, 11, -0.15),
                                    DefNode(19.25, 11, -2.75),
                                    DefNode(15.75, 11, -2.75)],
            all_nodes=self.all_nodes,
            all_lines=self.all_lines
        )

    def create_back_site(self) -> None:
        self.create_front_site_without_door(coordinate_y=0)
        self.all_opening.create_opening_by_nodes(
            corners_of_the_opening=[DefNode(15.75, 0, -1.23),
                                    DefNode(15.75, 0, -2.75),
                                    DefNode(19.25, 0, -2.75),
                                    DefNode(19.25, 0, -1.23)],
            all_nodes=self.all_nodes,
            all_lines=self.all_lines
        )

    def __call__(self, *args, **kwargs):
        self.create_basic()
        self.create_sides_without_windows()
        self.create_front_site()
        self.create_back_site()

        # line_01 = get_line_id_using_coordinates(all_lines=self.all_lines,
        #                                         start_coordinates=DefNode(0.75, 11, -1.23),
        #                                         end_coordinates=DefNode(4.25, 11, -1.23))
        # line_02 = get_line_id_using_coordinates(all_lines=self.all_lines,
        #                                         start_coordinates=DefNode(4.25, 11, -1.23),
        #                                         end_coordinates=DefNode(4.25, 11, -2.75))
        # line_03 = get_line_id_using_coordinates(all_lines=self.all_lines,
        #                                         start_coordinates=DefNode(4.25, 11, -2.75),
        #                                         end_coordinates=DefNode(0.75, 11, -2.75))
        # line_04 = get_line_id_using_coordinates(all_lines=self.all_lines,
        #                                         start_coordinates=DefNode(0.75, 11, -2.75),
        #                                         end_coordinates=DefNode(0.75, 11, -1.23))
        # boundary_lines_no = f"{line_01} {line_02} {line_03} {line_04}"
        # Surface.LoadDistribution(
        #     no=get_new_max_id(all_ids=self.all_surfaces.all_ids),
        #     boundary_lines_no=boundary_lines_no,
        #     load_transfer_direction=SurfaceLoadDistributionDirection.LOAD_TRANSFER_DIRECTION_IN_BOTH,
        #     loaded_lines=boundary_lines_no
        # )


