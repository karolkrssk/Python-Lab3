from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, comp_id, manufacturer, price):
        super().__init__()
        self.__id = comp_id
        self.__manufacturer = manufacturer
        self.__price = price


    @property
    def price(self):
        return self.__price

    @property
    def id(self):
        return self.__id

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self,value):
        self.__manufacturer = value

    @abstractmethod
    def do_operation(self):
        print(f"{self.__id}: nazwa{self.__manufacturer}")

    def get_children(self):
        return[]