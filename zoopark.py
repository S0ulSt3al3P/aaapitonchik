class Animal:
    def __init__(self, name, species, age, habitat, food):
        self.name = name
        self.species = species
        self.age = age
        self.habitat = habitat
        self.food = food

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Вид: {self.species}")
        print(f"Возраст: {self.age}")
        print(f"Среда обитания: {self.habitat}")
        print(f"Питание: {self.food}")

    def eat(self):
        print(f"{self.name} питается: {self.food}")


class Reptiles(Animal):
    def __init__(self, name, species, age, habitat, food,
                 body_temperature, scales):
        super().__init__(name, species, age, habitat, food)
        self.body_temperature = body_temperature
        self.scales = scales

    def bask(self):
        print(f"{self.name} греется на солнце.")

    def crawl(self):
        print(f"{self.name} передвигается ползком.")

    def info(self):
        super().info()
        print(f"Тип температуры: {self.body_temperature}")
        print(f"Чешуя: {self.scales}")


class Amphibians(Animal):
    def __init__(self, name, species, age, habitat, food,
                 skin_type, life_cycle):
        super().__init__(name, species, age, habitat, food)
        self.skin_type = skin_type
        self.life_cycle = life_cycle

    def jump(self):
        print(f"{self.name} прыгает.")

    def swim(self):
        print(f"{self.name} плавает в воде.")

    def info(self):
        super().info()
        print(f"Тип кожи: {self.skin_type}")
        print(f"Жизненный цикл: {self.life_cycle}")


class ZooShow:
    def __init__(self):
        self.reptiles = [
            Reptiles(
                "Кеша", "Игуана", 5, "Тропики",
                "Растения", "Холоднокровная", "Чешуйчатая"
            ),
            Reptiles(
                "Рокки", "Черепаха", 12, "Суша и вода",
                "Овощи", "Холоднокровная", "Панцирь"
            )
        ]

        self.amphibians = [
            Amphibians(
                "Кваша", "Лягушка", 3, "Болота",
                "Насекомые", "Влажная", "Икра - головастик - взрослая"
            ),
            Amphibians(
                "Амфи", "Саламандра", 4, "Влажные леса",
                "Насекомые", "Влажная", "Икра - личинка - взрослая"
            )
        ]

    def start(self):
        print("=" * 40)
        print("        ЗООПАРК ШОУ")
        print("=" * 40)

        print("\nВыберите программу:")
        print("1. Шоу пресмыкающихся")
        print("2. Шоу земноводных")

        choice = input("Ваш выбор: ")

        if choice == "1":
            self.reptile_show()
        elif choice == "2":
            self.amphibian_show()
        else:
            print("Неверный выбор!")
            return

        self.buy_ticket()

    def reptile_show(self):
        print("\n" + "=" * 40)
        print("       ШОУ ПРЕСМЫКАЮЩИХСЯ")
        print("=" * 40)

        for animal in self.reptiles:
            print(f"\nУчастник шоу: {animal.name} ({animal.species})")
            animal.bask()
            animal.crawl()
            animal.eat()

    def amphibian_show(self):
        print("\n" + "=" * 40)
        print("         ШОУ ЗЕМНОВОДНЫХ")
        print("=" * 40)

        for animal in self.amphibians:
            print(f"\nУчастник шоу: {animal.name} ({animal.species})")
            animal.jump()
            animal.swim()
            animal.eat()

    def buy_ticket(self):
        print("\n" + "=" * 40)
        print("           ПОКУПКА БИЛЕТА")
        print("=" * 40)

        print("1. Обычный билет — 500 сом")
        print("2. VIP-билет — 1200 сом")

        ticket = input("Выберите билет: ")

        if ticket == "1":
            price = 500
            place = "Обычное место"
        elif ticket == "2":
            price = 1200
            place = "VIP-место"
        else:
            print("Неверный тип билета!")
            return

        quantity = int(input("Количество билетов: "))

        if quantity <= 0:
            print("Количество билетов должно быть больше нуля!")
            return

        total = price * quantity

        print("\n" + "=" * 40)
        print("           ВАШ БИЛЕТ")
        print("=" * 40)
        print(f"Тип билета: {place}")
        print(f"Цена одного билета: {price} сом")
        print(f"Количество билетов: {quantity}")
        print(f"ИТОГО: {total} сом")
        print("=" * 40)
        print("Спасибо за посещение нашего зоопарка!")


zoo = ZooShow()
zoo.start()