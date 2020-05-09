from .component import Component


class Memory(Component):
    def __init__(self, comp_id, manufacturer, price, memory_type, capacity):
        super().__init__(comp_id, manufacturer, price)
        self.__memory_type = memory_type
        self.__capacity = capacity

    @property
    def memory_type(self):
        return self.__memory_type

    @property
    def capacity(self):
        return self.__capacity

    def do_operation(self):
        print(
            f"Pamięc ram : ID:{self.id} {self.manufacturer} {self.memory_type} {self.capacity}GB cena:{self.price}zł   ")
