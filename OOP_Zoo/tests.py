from animals import Animal, Doggo, Iguana, Human
import unittest


class TestAnimals(unittest.TestCase):

    def setUp(self) -> None:
        self.anim = Animal('Anim', 40)
        self.dog = Doggo('Watson', 11)
        self.lizi = Iguana('Lizi', 3)
        self.human = Human('Human', 40, 'Coding')

    def test_init(self):
        self.assertTrue(isinstance(self.anim, Animal))
        self.assertEqual(self.anim.name, 'Anim')
        self.assertEqual(self.anim.age, 40)
        self.assertEqual(self.human.name, 'Human')

    def test_move_up(self):
        self.assertEqual(self.anim.position, 0)
        self.anim.move_up()
        self.assertEqual(self.anim.position, 1)

    def test_move_down(self):
        self.assertEqual(self.anim.position, 0)
        self.anim.move_down()
        self.assertEqual(self.anim.position, -1)

    def test_speak(self):
        self.assertEqual(self.dog.speak(), f"{self.dog.name} says 'I think you're so heckin' great! Woof.'")
        self.assertEqual(self.human.speak(), f'My name is {self.human.name}, I am {self.human.age} years old, '
                                             f'and I like to do {self.human.hobby}.')

    def test_hiss(self):
        self.assertEqual(self.lizi.speak(), f'{self.lizi.name} says "Hiss."')

    def test_hair(self):
        self.assertTrue(self.dog.hair)
        self.assertFalse(self.lizi.hair)

    def test_scales(self):
        self.assertTrue(self.lizi.scales)
        self.assertFalse(self.dog.scales)


if __name__ == "__main__":
    unittest.main()
