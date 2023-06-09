"Lab Automata"
from random import random, randint

class DayAutomate():
    """ Day simulation using automata theory """
    def __init__(self) -> None:
        self.state = "START"
        self.hungry = False
        self.sleepy = True
        self.hour_sleep = 0
        self.exhausted = False
        self.needed_sleep = randint(5, 10)

    def watching_videos(self, hour):
        """ VIDEO state """
        print(hour, "Watching videos ...")
        if self.sleepy:
            self.state = "SLEEP"
        else:
            self.exhausted = False
            self.state = "WALK"

    def eating(self, choice, hour):
        """ EAT state """
        print(hour, "Eating ...")

        self.hungry = False
        if choice <= 0.1:
            self.state = "WALK"

        elif 0.3 < choice <= 0.5:
            self.state = "SHOP"


        else:
            self.state = "STUDY"



    def go_center(self, choice, hour):
        """ CENTER state """
        print(hour, "Walking in center ...")
        if choice <= 0.3:
            pass
        else:
            self.state = "STUDY"

    def walking(self, hour):
        """ WALK state """
        print(hour, "Walking the park ...")
        if  self.hungry:
            self.state = "EAT"
        else:
            self.state = "STUDY"

    def shooping(self, hour):
        """ SHOP state """
        print(hour, "Shopping ...")

        if self.hungry:
            self.state = "EAT"
        else:
            self.state = "STUDY"

    def sleeping(self, hour):
        """ SLEEP state """
        print(hour, "Sleeping ...")
        if self.needed_sleep == self.hour_sleep :
            self.sleepy = False
            self.hungry = True

        if self.sleepy:
            self.state = "SLEEP"
            self.hour_sleep += 1
        else:
            self.state = "EAT"

    def starting(self, choice):
        """ START state """
        if choice <= 0.1:
            self.state = "VIDEO"
        else:
            self.state = "SLEEP"

    def alarm(self, choice, hour):
        """ ALARM state """
        print(hour, "Air alarm, sitting in shelter ...")
        if choice <= 0.1:
            self.state = "SHOP"
        else:
            self.state = "STUDY"

    def rain(self, choice):
        """ RAIN state """
        print("Raining ... ")
        if choice <= 0.1:
            self.state = "VIDEO"
        else:
            self.state = "STUDY"

    def studing(self, choice, hour):
        """ STUDY state """
        print(hour, "Studing ...")
        if choice <= 0.5:
            if random() <= 0.1:
                self.hungry = True
        elif 0.5 < choice <= 0.7:
            self.state = "VIDEO"
        elif 0.7 < choice <= 0.9:
            self.state = "SHOP"
            if random() <= 0.1:
                self.hungry = True

        elif (0.9 < choice) or self.hungry:
            self.state = "EAT"
    def call(self):
        """ CALL state """
        print("Sudden call for work")
        self.state = "STUDY"


    def simulate(self):
        """ Simulate day with starting state """

        for hour in range(24):
            choice = random()

            if hour == 23:
                self.state = "SLEEP"
                self.exhausted = True
                self.sleepy = True

            if hour == 14 or hour == 19:
                self.state = "EAT"

            if random() <= 0.05:
                self.state = "ALARM"

            if random() <= 0.05 and self.state != "SLEEP":
                self.state = "RAIN"
                self.rain(choice)

            if random() <= 0.05 and hour >= 8:
                self.state = "CALL"
                self.call()


            if self.state == "START":
                self.starting(choice)

            elif self.state == "ALARM":
                self.alarm(choice, hour)

            elif self.state == "VIDEO":
                self.watching_videos(hour)


            elif self.state == "SLEEP":
                self.sleeping(hour)

            elif self.state == "EAT":
                self.eating(choice, hour)

            elif self.state == "STUDY":
                self.studing(choice, hour)

            elif self.state == "STUDY":
                self.go_center(choice, hour)

            elif self.state == "WALK":
                self.walking(hour)

            elif self.state == "SHOP":
                self.shooping(hour)
day = DayAutomate()
day.simulate()
