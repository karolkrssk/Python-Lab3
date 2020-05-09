from observer_impl.subject import Subject
from observer_impl.observer import FirstObserver, SecondObserver


def main():
    subject1 = Subject()
    subject1.add_observer(FirstObserver)
    subject1.add_observer(SecondObserver)

    subject1.notify("pierwszy update",b=7)
    subject1.notify("drugi update", b=7)
    subject1.notify("trzeci update", b=7)


if __name__ == '__main__':
    main()
