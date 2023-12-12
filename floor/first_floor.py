from utils.def_data_classes.node import DefNode
from floor.common import CommonForFloor


class FirstFloor(CommonForFloor):
    def create_front_site(self) -> None:
        self.create_back_site_without_door_with_offset(offset_y=11)

        front_door_corners_of_the_opening = [DefNode(15.75, 11, -0.15),
                                             DefNode(19.25, 11, -0.15),
                                             DefNode(19.25, 11, -2.75),
                                             DefNode(15.75, 11, -2.75)]
        self.create_window_with_glass(corners_of_the_opening=front_door_corners_of_the_opening)

    def __call__(self) -> None:
        self.create_base_with_offset()
        self.create_first_left_side_with_offset()
        self.create_front_site()
        self.create_area_for_stairs_with_offset()
        self.create_first_left_side_with_offset(offset_x=25)
        self.create_back_site_with_offset()
