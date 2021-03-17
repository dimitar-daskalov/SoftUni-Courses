# LSP (Liskov Substitution Principle)

from abc import ABC, abstractmethod


class Robot(ABC):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def sensors_count(self):
        pass


class Android(Robot):
    def sensors_count(self):
        return 4


class Chappie(Robot):
    def sensors_count(self):
        return 6


def count_robot_sensors(robots: list):
    summed_sensors = 0
    for robot in robots:
        summed_sensors += robot.sensors_count()
    print(summed_sensors)


robots = [Android('Robocop'), Chappie('XIX')]
count_robot_sensors(robots)