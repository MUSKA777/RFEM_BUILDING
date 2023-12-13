from dataclasses import dataclass, field
from typing import Optional
from RFEM.BasicObjects.material import Material


@dataclass
class GradeS355:
    name: str = "Grade S355"
    E = 205000  # Modulus of elasticity N/mm2
    G = 78846.2  # Shear modulus N/mm2
    v = 0.3  # Poisson's ratio
    specific_weight = 78.50  # kN/m3
    mass_density = 78.50  # kN/m3
    coefficient_of_thermal_ex = 0.000012  # 1/°C


@dataclass
class C20Slash25:
    name: str = "C20/25 | EN 1992-1-1:2004/A1:2014"
    E = 30000  # Modulus of elasticity N/mm2
    G = 12500  # Shear modulus N/mm2
    v = 0.2  # Poisson's ratio
    specific_weight = 25  # kN/m3
    mass_density = 2500  # kN/m3
    coefficient_of_thermal_ex = 0.00001  # 1/°C


@dataclass
class B500S_A:
    name: str = "B500S(A)"
    E = 200000  # Modulus of elasticity N/mm2
    G = 76923.1  # Shear modulus N/mm2
    v = 0.3  # Poisson's ratio
    specific_weight = 78.50  # kN/m3
    mass_density = 7850.00  # kN/m3
    coefficient_of_thermal_ex = 0.00001  # 1/°C


@dataclass
class MaterialName:
    grade_s355 = GradeS355()
    c20_slash_25 = C20Slash25()
    b500s_a = B500S_A()


@dataclass
class MaterialType:
    steel: str = "Steel"
    basic: str = "Basic"
    reinforcing_steel: str = "Reinforcing Steel"
    concrete: str = "Concrete"


@dataclass
class MaterialModel:
    isotropic_linear_elastic = "Isotropic | Linear Elastic"
    surface_orthotropic_linear_elastic = "Orthotropic | Linear Elastic (Surfaces)"
    solids_orthotropic_linear_elastic = "Orthotropic | Linear Elastic (Solids)"


# ClassVar
@dataclass
class DefMaterial:
    id: int
    material_name: MaterialName.__name__
    material_type: MaterialType.__name__
    material_model: MaterialModel.__name__
    name: Optional[str] = field(default=None)

    def __post_init__(self):
        self.name = f"{self.id} - {self.material_name} | {self.material_model}"

    def create_material(self):
        Material(self.id, self.material_name.name)


@dataclass
class AllMaterial:
    grade_S355_isotropic_linear_elastic: DefMaterial = DefMaterial(
        id=1,
        material_name=MaterialName.grade_s355,
        material_type=MaterialType.concrete,
        material_model=MaterialModel.isotropic_linear_elastic)

    c20_slash_25_isotropic_linear_elastic: DefMaterial = DefMaterial(
        id=2,
        material_name=MaterialName.c20_slash_25,
        material_type=MaterialType.concrete,
        material_model=MaterialModel.isotropic_linear_elastic)

    b500s_a_isotropic_linear_elastic: DefMaterial = DefMaterial(
        id=3,
        material_name=MaterialName.b500s_a,
        material_type=MaterialType.reinforcing_steel,
        material_model=MaterialModel.isotropic_linear_elastic)
