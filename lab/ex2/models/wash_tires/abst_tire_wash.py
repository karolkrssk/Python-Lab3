from abc import ABC, abstractmethod
from lab.ex2.models.wash_tires.tire_wash_lib import bubbles, nobubbles


class AbstractTireWash(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def wash_tires(self, car):
        pass


class WithBubbles(AbstractTireWash):
    def __init__(self):
        super().__init__()

    def wash_tires(self, car):
        bubbles(car)


class WithoutBubbles(AbstractTireWash):
    def __init__(self):
        super().__init__()

    def wash_tires(self, car):
        nobubbles(car)
