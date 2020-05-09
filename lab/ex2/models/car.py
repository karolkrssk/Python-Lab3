class Car:

    def __init__(self, tire_wash_strategy, carbody_wash_strategy):
        self.__tire_wash_strategy = tire_wash_strategy
        self.__carbody_wash_strategy = carbody_wash_strategy

    def __call__(self, car_model, wheel_diameter):
        self.__carbody_wash_strategy.wash_carbody(car_model)
        self.__tire_wash_strategy.wash_tires(wheel_diameter)
