from abc import ABC, abstractmethod
from lab.ex2.models.wash_carbody.bodycar_wash_lib import with_waxing, without_waxing


class AbstractCarbodyWash(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def wash_carbody(self, car):
        pass


class WithWax(AbstractCarbodyWash):
    def __init__(self):
        super().__init__()

    def wash_carbody(self, car):
        with_waxing(car)


class WithoutWax(AbstractCarbodyWash):
    def __init__(self):
        super().__init__()

    def wash_carbody(self, car):
        without_waxing(car)
