from .component import Component


class Powersupply(Component):
    def __init__(self, comp_id, manufacturer, price, ps_size):
        super().__init__(comp_id, manufacturer, price)
        self.__ps_size = ps_size

    @property
    def ps_size(self):
        return self.__ps_size

    def do_operation(self):
        print(f"Zasilacz : ID:{self.id} {self.manufacturer} {self.ps_size}W cena:{self.price}zł   ")
