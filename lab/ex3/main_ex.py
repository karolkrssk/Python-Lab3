from models_ex.composite import Composite
from models_ex.leaf import Leaf


def main():
    leaf_1 = Leaf(1)
    leaf_2 = Leaf(2)
    leaf_3 = Leaf(3)
    leaf_4 = Leaf(4)

    composite_1 = Composite(1)
    composite_1.add_component(leaf_1)

    composite_2 = Composite(2)
    composite_1.add_component(composite_2)

    composite_3 = Composite(3)
    composite_3.add_component(leaf_2)
    composite_3.add_component(leaf_3)
    composite_2.add_component(composite_3)

    composite_4 = Composite(4)
    composite_4.add_component(leaf_4)
    composite_2.add_component(composite_4)

    composite_1.do_operation()

if __name__ == '__main__':
    main()
