from models.processor import Processor
# from models.composite_back import Composite
from models.memory import Memory
from models.powersupply import Powersupply
from models.motherboard import Motherboard
from models.computercase import Computer_case


def main():
    PC = Computer_case(comp_id=1, manufacturer="BeQuiet!", price=299)
    plyta1 = Motherboard(comp_id=2, manufacturer="Gigabyte", price=399)

    procesor1 = Processor(comp_id=3, manufacturer="intel", model="i5-8600", price=999)
    procesor2 = Processor(comp_id=4, manufacturer="AMD", model="Ryzen 5 1600", price=999)
    ram1 = Memory(comp_id=5, manufacturer="Corsair", price=390, memory_type="DDR4", capacity=16)
    ram2 = Memory(comp_id=6, manufacturer="GoodRam", price=300, memory_type="DDR4", capacity=16)
    powersupply1 = Powersupply(comp_id=7, manufacturer="BeQuiet!", price=290, ps_size=600)

    plyta1.add_component(procesor1)
    plyta1.add_component(ram1)
    plyta1.add_component(ram2)
    PC.add_component(powersupply1)
    PC.add_component(plyta1)


    PC.do_operation(plyta1.mb_components_price())


if __name__ == '__main__':
    main()
