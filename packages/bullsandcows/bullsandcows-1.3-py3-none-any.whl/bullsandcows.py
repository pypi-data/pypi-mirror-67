"""
bullsandcows v1.3
Python 3.6
"""

from random import sample
from time import time


class bullsandcows:
    """
    Object instantiation.
    User can pass a bool value to either enable or disable the anti-cheat, which is automatically enabled if left blank.
    """
    def __init__(self,anticheat:bool=True):
        self.__starttime = time()
        self.__stoptime = None
        self.__attempts = 0
        self.__number = "".join(map(str,sample(range(1,10),4)))
        self.__stopped = False
        self.__won = False
        self.__nocheat = anticheat

        """These are only uncommented for testing purposes."""
        # self.__number = "1234"
        # print(self.__number)

    """
    Property method for returning and setting the anti-cheat status post-instantiation.
    Sample usage for disabling the anti-cheat and printing its status after creating a bullsandcows() object:

        game = bullsandcows()
        game.anticheat = False
        print(game.anticheat)

    """
    @property
    def anticheat(self): # Getter that returns the anti-cheat status in bool.
        return self.__nocheat

    @anticheat.setter
    def anticheat(self,value:bool): # Setter that allows the user to enable or disable the anti-cheat.
        self.__nocheat = value

    """
    Getter methods for returning private data since they are protected from external modification.
    """
    def get_number(self): # Returns the generated random number in str.
        if self.__nocheat and not self.__stopped:
            raise Exception("Game is still in progress.")
        return str(self.__number)

    def get_attempts(self): # Returns the total number of attempts used in int.
        return self.__attempts

    def get_stopped_bool(self): # Returns the game stopping indicator value in bool.
        return self.__stopped

    def get_won_bool(self): # Returns the game winning indicator value in bool.
        return self.__won

    """
    Gets the total time spent by the player and converts it to minutes and seconds.
    Function variable returns in order:
    1. Minutes (int),
    2. seconds which is reset to 0 every 60 seconds (int).
    """
    def get_time(self):
        nowtime = self.__stoptime if self.__stopped else time()
        seconds = int(nowtime-self.__starttime)
        minutes = int(seconds//60)
        seconds -= (minutes*60)
        return int(minutes),int(seconds)

    """
    Gets and verifies a user's guess.
    Function variable returns in order:
    1. Number of bulls (int),
    2. number of cows (int).
    """
    def guess(self,value:str):
        if self.__stopped: # If the user has already stopped the game, this blocks them from resuming it.
            raise Exception("The game has already ended.")
        value = value.replace(" ","")
        if value.casefold() == "quit" or value.casefold() == "exit" or value.casefold() == "stop" or value.casefold() == "halt":
            self.__stopped = True
            self.__stoptime = time()
            return 0,0
        if len(value) != 4:
            raise Exception("Number must contain exactly four digits.")
        try: # Tries to put each individual entered character into four separate int variables.
            aa,bb,cc,dd = int(value[0]),int(value[1]),int(value[2]),int(value[3])
        except ValueError: # If str-to-int conversion fails, meaning one or more invalid characters were entered.
            raise Exception("Invalid characters found.")
        if aa == bb or aa == cc or aa == dd or bb == cc or bb == dd or cc == dd:
            raise Exception("Duplicates found.")

        bulls,cows = 0,0
        for i in value:
            for j in self.__number:
                if i == j:
                    if value.index(i) == self.__number.index(j): # Same position.
                        bulls += 1
                    else:
                        cows += 1

        self.__attempts += 1
        if bulls == 4:
            self.__won = True
            self.__stopped = True
            self.__stoptime = time()
        return bulls,cows
