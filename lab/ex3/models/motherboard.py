from .component import Component


class Motherboard(Component):
    def __init__(self, comp_id, manufacturer, price):
        super().__init__(comp_id, manufacturer, price)
        self.__component_dict = dict()

    def add_component(self, component):
        self.__component_dict[component.id] = component

    def remover_component(self, comp_id):
        if comp_id in self.__component_dict:
            del self.__component_dict[comp_id]

    def mb_components_price(self):
        mb_parts_price = 0
        for comp in self.__component_dict.values():
            mb_parts_price += comp.price
        return mb_parts_price

    def do_operation(self):

        print(f"Producent płyty głownej: {self.manufacturer} cena:{self.price}zł \nPodzespoły na płycie głównej:")
        print(50 * "-")
        for comp in self.__component_dict.values():
            comp.do_operation()
        print(50 * "-")
        print(f"Cena płyty głównej z podzespołami {self.mb_components_price() + self.price}zł")

    def get_children(self):
        return self.__component_dict.values()
