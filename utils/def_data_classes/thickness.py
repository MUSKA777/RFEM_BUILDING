from dataclasses import dataclass, field
from utils.def_data_classes.material import AllMaterial
from typing import Optional
from RFEM.BasicObjects.thickness import Thickness

@dataclass
class ThicknessType:
    uniform: str = "Uniform"
    stiffness_matrix = "Stiffness Matrix"


@dataclass
class DefThickness:
    id: int
    thickness_type: ThicknessType.__name__
    material: AllMaterial.__name__
    uniform_thickness_d: float  # m
    name: Optional[str] = field(default=None)

    def __post_init__(self):
        self.name = f"{self.id} - {self.thickness_type} | d : {self.uniform_thickness_d} | {self.material.name}"

    def create_thickness(self):
        Thickness(no=self.id,
                  # name=self.thickness_type,
                  material_no=self.material.id,
                  uniform_thickness_d=self.uniform_thickness_d)


@dataclass
class AllThicknesses:
    uniform_d_300_c20slash25: DefThickness = DefThickness(
        id=1,
        thickness_type=ThicknessType.uniform,
        material=AllMaterial.c20_slash_25_isotropic_linear_elastic,
        uniform_thickness_d=0.300
    )

    uniform_d_220_c20slash25: DefThickness = DefThickness(
        id=2,
        thickness_type=ThicknessType.uniform,
        material=AllMaterial.c20_slash_25_isotropic_linear_elastic,
        uniform_thickness_d=0.220
    )
    uniform_d_240_c20slash25: DefThickness = DefThickness(
        id=3,
        thickness_type=ThicknessType.uniform,
        material=AllMaterial.c20_slash_25_isotropic_linear_elastic,
        uniform_thickness_d=0.240
    )


