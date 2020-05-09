import progressbar
from time import sleep
import logging
class Subject:
    def __init__(self):
        self.__obs_list = []

    def add_observer(self, obs):
        self.__obs_list.append(obs)

    def notify(self, *args, **kwargs):
        print("\nAktualizowano dane: zaczynam informowanie obserwatorów")

        for obs in progressbar.progressbar(self.__obs_list):
            print("\ninformuje obserwatora ")
            obs.update(self, *args, **kwargs)
            sleep(2)