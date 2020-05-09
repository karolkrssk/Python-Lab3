from .component import Component


class Processor(Component):
    def __init__(self, comp_id, manufacturer, price, model):
        super().__init__(comp_id, manufacturer, price)
        self.__model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    def do_operation(self):
        print(f"Procesor : ID:{self.id} {self.manufacturer} {self.model} cena:{self.price}zł   ")
