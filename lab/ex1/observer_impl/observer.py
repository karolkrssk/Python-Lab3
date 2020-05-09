from abc import ABC, abstractmethod


class Observer(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def update(self, *args, **kwargs):
        pass


class FirstObserver(Observer):
    def __init__(self):
        super.__init__()

    def update(self, *args, **kwargs):
        print("first observer")
        if args:
            print(args)
        if kwargs:
            print(kwargs)


class SecondObserver(Observer):
    def __init__(self):
        super.__init__()

    def update(self, *args, **kwargs):
        print("second observer")
        if args:
            print(args)

