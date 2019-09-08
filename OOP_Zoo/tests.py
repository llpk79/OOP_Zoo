import unittest
from animals import Animal, Doggo, Iguana


class TestAnimals(unittest.TestCase):

    def setUp(self) -> None:
        self.anim = Animal('Anim', 40)
        self.dog = Doggo('Watson', 11)
        self.lizi = Iguana('Lizi', 3)

    def test_init(self):
        self.assertTrue(isinstance(self.anim, Animal))
        self.assertEqual(self.anim.name, 'Anim')
        self.assertEqual(self.anim.age, 40)

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
