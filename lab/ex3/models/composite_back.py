from .component import Component


class Composite(Component):
    def __init__(self, comp_id, manufacturer, price):
        super().__init__(comp_id, manufacturer, price)
        self.__component_dict = dict()

    def add_component(self, component):
        self.__component_dict[component.id] = component

    def remover_component(self, comp_id):
        if comp_id in self.__component_dict:
            del self.__component_dict[comp_id]

    def do_operation(self):
        final_price = self.price
        print(f"Jestem komponentem {self.manufacturer}  moje elementy to:")
        for comp in self.__component_dict.values():
            comp.do_operation()
            final_price+= comp.price
        print(f"cena ogóółem {final_price}")

    def get_children(self):
        return self.__component_dict.values()
