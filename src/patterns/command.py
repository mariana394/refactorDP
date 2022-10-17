# Patron de diseño: COMMAND

import abc
from patterns import print_report as p
from patterns import csv_utils

class Command(abc.ABC):

    def execute(self):
        raise Exception("I am an interface")


class createOneCommand(Command):

    def __init__(self, type, link):
        self.type = type
        self.rides = csv_utils.parse_file(link)

    def execute(self):
        obj = p.get_report(self.type, self.rides)
        obj.create_content()
        return obj

class createTwoCommand(Command):

    def __init__(self, type, type2, link):
        self.type = type
        self.type2 = type2
        self.rides = csv_utils.parse_file(link)
        

    def execute(self):
        object1 = p.get_report(self.type, self.rides)
        object1.create_content()
        object2 = p.get_report(self.type2, self.rides)
        object2.create_content()

        return object1, object2