"""Object oriented programming demo."""


class Animal:
    """Base class for all Animals.

    :var name: str
    :var age: int
    :var position: 0

    Methods:
    - move_up
        - moves up one.
        - prints old and new pos.
    - move_down
        - moves down one.
        - prints old and new pos.
    - move_to
        - moves to given pos.
        - prints old and new pos.

    """

    # Class variables.
    hair = None
    scales = None

    def __init__(self, name: str, age: int) -> None:
        # Instance variable.
        self.name = name
        self.age = age
        self.position = 0

    def __repr__(self):
        """Return the class name and instance variables when printing the instance."""
        return f'{self.__class__} {self.__dict__}'

    def move_up(self) -> None:
        """Increment position. Print string with old and new position."""
        self.position += 1
        print(f'{self.name} moved from {self.position -1} to {self.position}')

    def move_down(self) -> None:
        """Decrement position. Print string with old and new position"""
        self.position -= 1
        print(f'{self.name} moved from {self.position + 1} to {self.position}')

    def move_to(self, pos: int) -> None:
        """Move to given position. Print string with old and new position.

        :var pos: int The position to move to.
        """
        old = self.position
        self.position = pos
        print(f'{self.name} moved from {old} to {self.position}')


class Mammal(Animal):
    """Base for Mammals. Inherits from Animal.

    Class variables:
    - hair: True

    Methods:
    - speak:
        - Override in child class.

    """

    hair = True

    def speak(self) -> str:
        """Method intended to be overridden by child class."""
        return 'Please, give me a voice.'


class Reptile(Animal):
    """Base class for Reptiles. Inherits from Animal.

    Class variables:
    - scales: True

    Methods:
    - speak:
        - returns a str.

    """

    scales = True

    def speak(self) -> str:
        """What a reptile would say."""
        return f'{self.name} says "Hiss."'


class Human(Mammal):
    """Class for making people. Inherits from Mammal.

    Class variables:
    - species: str

    :var hobby: str

    Methods:
    - speak:
        - returns a str.
    _ do_hobby:
        - returns a str.

    """

    genus = 'homo'

    def __init__(self, name: str, age: int, hobby: str = None):
        # Call super to instantiate parent class instance variables.
        super().__init__(name, age)  # Pass parent variables to super.
        # Instantiate a specific Human instance variable.
        self.hobby = hobby

    def speak(self) -> str:
        """A basic human phrase."""
        # Begin with a base phrase.
        phrase = f'My name is {self.name}, I am {self.age} years old'

        # Add hobbies if given.
        if self.hobby:
            phrase += f', and I like to do {self.hobby}.'

        # Add this if no hobbies given.
        else:
            phrase += f', and I am boring.'

        return phrase

    def do_hobby(self) -> str:
        """Do the hobby!"""
        if self.hobby:
            return f'I am doing {self.hobby}, it is fun!'
        else:
            return f'I do not have a hobby.'


class Doggo(Mammal):
    """Class for making doggos. Inherits from Mammal.

    Class variables:
    - species: str

    Methods:
    - speak:
        - returns a str.

    """

    genus = 'canis'

    def speak(self) -> str:
        """What any dog would say."""
        return f"{self.name} says 'I think you're so heckin' great! Woof.'"

    @staticmethod
    def fetch() -> str:
        """Do a fetch."""
        return f'I will get that for you!'


class Iguana(Reptile):
    """Iguanas don't do much. Inherits from Reptile.

    Class variables:
    - species: str

    Methods:
    - hide:
        - returns a str.

    """

    genus = 'iguana'

    def hide(self) -> str:
        """What an iguana do."""
        return f'{self.name} is hiding. {self.name} is a great pet!'


if __name__ == "__main__":
    pass
