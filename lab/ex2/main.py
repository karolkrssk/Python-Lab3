from models.car import Car
from models.wash_tires.abst_tire_wash import WithBubbles, WithoutBubbles
from models.wash_carbody.abst_carbody_wash import WithWax,WithoutWax



def main():
    car_1 = Car(tire_wash_strategy=WithoutBubbles(),carbody_wash_strategy=WithWax())
    car_1(car_model="Fiat Punto", wheel_diameter="16")

    car_2 = Car(WithBubbles(), WithoutWax() )
    car_2(car_model="Volkswagen Passat", wheel_diameter="16")

if __name__ == '__main__':
    main()