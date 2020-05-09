from .component import Component


class Computer_case(Component):
    def __init__(self, comp_id, manufacturer, price):
        super().__init__(comp_id, manufacturer, price)
        self.__component_dict = dict()

    def add_component(self, component):
        self.__component_dict[component.id] = component

    def remover_component(self, comp_id):
        if comp_id in self.__component_dict:
            del self.__component_dict[comp_id]

    def do_operation(self, mb_components_price):
        final_price = self.price
        final_price += mb_components_price
        print(50 * "-")
        print(f"Twój komputer: \nObudowa:{self.manufacturer} cena:{self.price}zł")
        for comp in self.__component_dict.values():
            comp.do_operation()
            final_price += comp.price
        print(50 * "+")
        print(f"Cena ogółem {final_price}zł")
        print(50 * "+")

    def get_children(self):
        return self.__component_dict.values()
