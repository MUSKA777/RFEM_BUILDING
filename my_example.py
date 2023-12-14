from dataclasses import dataclass


@dataclass
class VS:
    v: float  # value
    s: float  # scale factor

    def scaled_value(self):
        return self.v * self.s


@dataclass
class Container:
    a: VS = VS(1, 1)
    b: float = 1


c1 = Container()
c2 = Container()

print(c1)
print(c2)

c1.a.v = -999
c1.b = -999

print(c1)
print(c2)
