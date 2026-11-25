from abc import ABC, abstractmethod
from datetime import datetime


class MenuItem(ABC):
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    @abstractmethod
    def calculatePrice(self):
        pass


class Pizza(MenuItem):
    def __init__(self, name, base_price, size):
        super().__init__(name, base_price)
        self.size = size

    def calculatePrice(self):
        if self.size.lower() == "большая":
            return self.base_price * 1.3
        return self.base_price

    def __str__(self):
        return f"{self.name} ({self.size})"


class Drink(MenuItem):
    def __init__(self, name, base_price, isIce):
        super().__init__(name, base_price)
        self.isIce = isIce

    def calculatePrice(self):
        return self.base_price

    def __str__(self):
        if self.isIce:
            return f"{self.name} со льдом"
        return self.name


class ComboSet(MenuItem):
    def __init__(self, name, items):
        super().__init__(name, 0)
        self.items = items

    def calculatePrice(self):
        total = sum(item.calculatePrice() for item in self.items)
        return total * 0.85

    def __str__(self):
        return self.name


class PaymentStrategy(ABC):
    @abstractmethod
    def collectPayment(self, amount):
        pass


class CardPayment(PaymentStrategy):
    def __init__(self, expiry_date):
        self.expiry_date = expiry_date

    def collectPayment(self, amount):
        try:
            expiry = datetime.strptime(self.expiry_date, "%m/%Y")
            current = datetime.now()

            if expiry.year < current.year or (
                expiry.year == current.year and expiry.month < current.month
            ):
                print("Ошибка: срок действия карты истек.")
                return False

            print(f"Оплата картой успешно выполнена: {amount:.2f} сом")
            return True

        except ValueError:
            print("Неверный формат срока действия карты.")
            return False


class CashPayment(PaymentStrategy):
    def collectPayment(self, amount):
        print(f"Оплата наличными: {amount:.2f} сом")
        print("Оплата успешно принята.")
        return True


class Order:
    __statuses = [
        "Новый",
        "Оплачен",
        "Готовится",
        "Готов",
        "Доставлен"
    ]

    def __init__(self):
        self.__items = []
        self.__status = self.__statuses[0]

    @property
    def status(self):
        return self.__status

    def addItem(self, item):
        if self.__statuses.index(self.__status) >= 2:
            raise Exception("Нельзя добавить блюдо: заказ уже готовится.")

        if not isinstance(item, MenuItem):
            raise TypeError("Можно добавлять только позиции MenuItem.")

        self.__items.append(item)
        print(f"Добавлено в корзину: {item}")

    def getTotalCost(self):
        return sum(item.calculatePrice() for item in self.__items)

    def showOrder(self):
        print("\n========== ВАШ ЗАКАЗ ==========")

        if not self.__items:
            print("Корзина пуста.")
            return

        for item in self.__items:
            print(f"{item} — {item.calculatePrice():.2f} сом")

        print(f"Итого: {self.getTotalCost():.2f} сом")
        print(f"Статус: {self.__status}")

    def pay(self, paymentMethod):
        if self.__status != "Новый":
            print("Заказ уже оплачен или находится на другом этапе.")
            return

        if not self.__items:
            print("Нельзя оплатить пустой заказ.")
            return

        amount = self.getTotalCost()

        if paymentMethod.collectPayment(amount):
            self.__status = "Оплачен"

    def nextStep(self):
        current_index = self.__statuses.index(self.__status)

        if current_index == len(self.__statuses) - 1:
            print("Заказ уже доставлен.")
            return

        self.__status = self.__statuses[current_index + 1]
        print(f"Новый статус заказа: {self.__status}")


class Restaurant:
    def __init__(self):
        self.order = Order()

    def showMenu(self):
        print("\n========== МЕНЮ ==========")
        print("1. Пицца Маргарита (маленькая) — 500 сом")
        print("2. Пицца Пепперони (большая) — 800 сом + 30%")
        print("3. Кола — 150 сом")
        print("4. Кола со льдом — 150 сом")
        print("5. Комбо-набор — скидка 15%")
        print("6. Показать корзину")
        print("7. Оплатить картой")
        print("8. Оплатить наличными")
        print("9. Следующий этап заказа")
        print("0. Выход")

    def start(self):
        while True:
            self.showMenu()
            choice = input("\nВыберите действие: ")

            try:
                if choice == "1":
                    self.order.addItem(
                        Pizza("Маргарита", 500, "маленькая")
                    )

                elif choice == "2":
                    self.order.addItem(
                        Pizza("Пепперони", 800, "большая")
                    )

                elif choice == "3":
                    self.order.addItem(
                        Drink("Кола", 150, False)
                    )

                elif choice == "4":
                    self.order.addItem(
                        Drink("Кола", 150, True)
                    )

                elif choice == "5":
                    combo = ComboSet(
                        "Комбо-набор",
                        [
                            Pizza("Маргарита", 500, "маленькая"),
                            Drink("Кола", 150, True)
                        ]
                    )
                    self.order.addItem(combo)

                elif choice == "6":
                    self.order.showOrder()

                elif choice == "7":
                    expiry = input("Введите срок действия карты (MM/YYYY): ")
                    self.order.pay(CardPayment(expiry))

                elif choice == "8":
                    self.order.pay(CashPayment())

                elif choice == "9":
                    self.order.nextStep()

                elif choice == "0":
                    print("Спасибо за заказ!")
                    break

                else:
                    print("Неверный выбор.")

            except Exception as error:
                print(f"Ошибка: {error}")


restaurant = Restaurant()
restaurant.start()