from animals import Human, Doggo, Iguana


def main():
    paul = Human('Paul', 40)
    isabelle = Human('Isabelle', 39, hobby='yoga')
    banjo = Doggo('Banjo', 5)
    chichi = Iguana('Chichi', 3)

    print(paul.speak())
    print(isabelle.speak())
    print(banjo.speak())
    print(chichi.speak())

    paul.move_down()
    paul.move_down()

    isabelle.move_down()
    isabelle.move_to(5)

    banjo.move_up()
    banjo.move_up()

    print(f'Chichi has hair? {chichi.hair is True}')
    print(f'Chichi has scales? {chichi.scales is True}')

    print(f'{isabelle.name} is {isabelle.age} years old and {isabelle.do_hobby()}')

    print(f'{paul.name} is {paul.age} years old and {paul.do_hobby()}')
    paul.hobby = 'snowboarding'
    print(f'{paul.name} is {paul.age} years old and {paul.do_hobby()}')

    print(f'{chichi.name} is a {chichi.genus} and {chichi.hide()}')
    print(f'I am {banjo.name} and {banjo.fetch()}')

    print(paul)
    print(banjo)


if __name__ == "__main__":
    main()
