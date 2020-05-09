from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, comp_id, prefix=" "):
        super().__init__()
        self.__id = comp_id
        self.__prefix = prefix

    @property
    def id(self):
        return self.__id

    @property
    def prefix(self):
        return self.__prefix

    @prefix.setter
    def prefix(self, value):
        self.__prefix = value

    @abstractmethod
    def do_operation(self):
        print("\t", end="")

    def get_children(self):
        return []
