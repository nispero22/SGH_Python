#The blue car has 20,000 miles.
# The red car has 30,000 miles.


class Cars:
    type = "car"
    def __init__(self, colour, milage):
        self.colour = colour
        self.milage = milage

    # Instance method
    def __str__(self):
        return f"The {self.colour} car has {self.milage} miles"

