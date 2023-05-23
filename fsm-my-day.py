"""
my life: Finite-state machine
"""

from enum import Enum, auto, unique
from random import random, choice

@unique
class States(Enum):
    """
    Life states enum
    """
    sleeping = auto()
    running = auto()
    eating = auto()
    studying = auto()
    walking = auto()
    working = auto()
    training = auto()
    chilling = auto()

def prime(func):
    def wrapper(*args, **kwargs):
        v = func(*args, **kwargs)
        v.send(None)
        return v
    return wrapper

class Denis():
    """
    Denis class
    """
    def __init__(self) -> None:
        self.poliarity = 0
        self.is_raining = False
        self.nothing_doing_time = 0
        self.sleeping_state = self._sleeping_state()
        self.running_state = self._running_state()
        self.eating_state = self._eating_state()
        self.working_state = self._working_state()
        self.studying_state = self._studying_state()
        self.walking_state = self._walking_state()
        self.training_state = self._training_state()
        self.chilling_state = self._chilling_state()
        self.current_state = self._sleeping_state()

    @prime
    def _sleeping_state(self):
        """
        Sleeping state
        """
        while True:
            hour = yield
            self.change_poliarity()
            self.get_weather()
            print(f"It is {hour} o'clock. I am {States.sleeping.name}")
            if not self.is_raining and hour == 6:
                self.current_state = self.running_state
            elif hour == 7:
                self.current_state = self.eating_state

    @prime
    def _running_state(self):
        """
        Running state
        """
        while True:
            hour = yield
            print(f"It is {hour} o'clock. I am {States.running.name}")
            if hour == 7:
                self.current_state = self.eating_state

    @prime
    def _eating_state(self):
        """
        Eating state
        """
        while True:
            hour = yield
            print(f"It is {hour} o'clock. I am {States.eating.name}")
            if hour == 8:
                self.current_state = self.studying_state

    @prime
    def _working_state(self):
        """
        Working state
        """
        while True:
            hour = yield
            print(f"It is {hour} o'clock. I am {States.working.name}")
            want_to_walk = random()
            if hour == 20 and want_to_walk > 0.7:
                self.current_state = self.walking_state
            elif hour == 20 and want_to_walk <= 0.7:
                self.current_state = self.chilling_state


    @prime
    def _studying_state(self):
        """
        Studying state
        """
        while True:
            hour = yield
            print(f"It is {hour} o'clock. I am {States.studying.name}")
            self.change_poliarity()
            need_sport = random()
            if need_sport > 0.5 and hour == 14:
                self.current_state = self.training_state
            elif hour == 16:
                self.current_state = self.working_state
            

    @prime
    def _walking_state(self):
        """
        Walking state
        """
        while True:
            hour = yield
            print(f"It is {hour} o'clock. I am {States.walking.name}")
            if hour == 22:
                self.current_state = self.sleeping_state
            

    @prime
    def _training_state(self):
        """
        Training state
        """
        while True:
            hour = yield
            print(f"It is {hour} o'clock. I am {States.training.name}")
            if hour == 15:
                self.current_state = self.working_state

    @prime
    def _chilling_state(self):
        """
        Chilling state
        """
        while True:
            hour = yield
            print(f"It is {hour} o'clock. I am {States.chilling.name}")
            if hour == 22:
                self.current_state = self.sleeping_state

    def change_poliarity(self):
        """
        Change poliarity method
        """
        n = random()
        if n < 0.4:
            self.poliarity = -1
        elif n > 0.6:
            self.poliarity = 1
        else:
            self.poliarity = 0

    def get_weather(self):
        """
        Get weather method
        """
        n = random()
        if n >= 0.7:
            self.is_raining = True
        else:
            self.is_raining = False
        
    def send(self, hour):
        """
        Send method
        """
        self.current_state.send(hour)

def live_day():
    """
    Live day function
    """
    denis = Denis()
    for hour in range(1, 25):
        denis.send(hour)

live_day()