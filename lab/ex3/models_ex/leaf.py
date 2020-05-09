from .component import Component


class Leaf(Component):
    def __init__(self, comp_id):
        super().__init__(comp_id)

    def do_operation(self):
        print("{0}I\'m inside a leaf {1}".format(self.prefix, self.id))
