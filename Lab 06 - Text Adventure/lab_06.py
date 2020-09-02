
class Cafeteria:
    """
    This is a class that represents a room
    """
    def __init__(self):
        # this method sets up the variables in the class
        self.walls = blue
        self.number_of_desks = 123
        self.north = Math
        self.south = Science
        self.east = Social_Studies
        self.west = Language_Arts
class Math:
    """
    This class represents a math classroom
    """
    def __init__(self):
        self.walls = white
        self.number_of_desks = 32
        self.grade = 8
        self.south = Cafeteria
class SocialStudies:
    """
    This class represents a social studies classroom
    """
    def __init__(self):
        self.walls = green
        self.number_of_desks = 28
        self.grade = 6
        self.west = Cafeteria
class Science:
    """
    This class represents a science classroom
    """
    def __init__(self):
        self.walls = yellow
        self.number_of_desks = 37
        self.grade = 8
        self.north = Cafeteria

class LanguageArts:
    """
    This class represents a Language arts classroom
    """
    def __init__(self):
        self.walls = white
        self.number_of_desks = 31
        self.grade = 7
        self.east = Cafeteria

rooms = [Cafeteria, Math, SocialStudies, LanguageArts, Science]
print(type(rooms))
foo = []
print(type(foo))