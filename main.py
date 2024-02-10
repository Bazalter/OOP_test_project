import random


class Meta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls.id_ = 1


class IdCounter(metaclass=Meta):
    def __init__(self):
        self.id_ = self.__class__.id_
        self.__class__.id_ += 1


class Password:

    def __init__(self, password):
        self.password = None
        self.set_password(password)

    @staticmethod
    def check(password):
        if not isinstance(password, str):
            raise TypeError()

        if len(password) < 8 and password.isalnum():
            raise ValueError()

        if password not in [i.get('password') for i in User.base]:
            raise ValueError('Пароль неверный')

    def set_password(self, password):
        self.check(password)
        self.password = password


class Product(IdCounter):
    def __init__(self, name, price, rating):
        super().__init__()
        self._name = name
        self.price = None
        self.rating = None

    def is_valid(self, value_price, value_rating):
        if not isinstance(value_price, (int, float)):
            return ValueError()
        if not isinstance(value_rating, (int, float)):
            return ValueError()

    def set_price_rating(self, price, rating):
        self.is_valid(price, rating)
        self.price = price
        self.rating = rating

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name},{self.price}, {self.rating})"

    def __str__(self):
        return f"{self.id_}_{self._name}"


class Cart:
    def __init__(self):
        self.cart = []

    def __len__(self):
        return len(self.cart)

    def add_cart(self, id_product):
        self.cart.append(id_product)

    def remove_cart(self, id_product):
        self.cart.remove(id_product)

    def __str__(self):
        return f'{self.cart}'


class User(IdCounter, Password):
    username = None
    password = None
    base = [{'name': "q1", 'password': "1234567gfd"}, {'name': "q2", 'password': "1234567gfd"}]

    def __init__(self, username, password):
        super().__init__()
        self.user_cart = Cart()
        self.set_username(username)
        self.set_password(password)

    @staticmethod
    def check_username(username):
        if username not in [i.get('name') for i in User.base]:
            raise ValueError('Пользователь не найден')

    def set_username(self, username):
        self.check_username(username)
        self._username = username

    def __repr__(self):
        return f'{self.__class__.__name__}: ({self._username}, Пароль: password1)'

    def __str__(self):
        return f'{self.id_}_password1'


class Store:
    def __init__(self, list_product):
        a = input('Введите имя:  ')
        b = input('Введите пароль:  ')
        self.user = User(a, b)
        self.user_cart = Cart()
        self.list_product = list_product

    def add_product(self):
        added_product = random.choice(self.list_product)
        self.user_cart.add_cart(added_product)

    def cart_view(self):
        if self.user_cart is None:
            return print('Корзина пуста')
        else:
            return print(f'В корзине: {str(self.user_cart)}')


if __name__ == '__main__':

    product_list_name = ["банан", "мандарин", "яблоко", "свекла", "помидор", "огурец", "капуста", "авакадо", "дыня", "арбуз"]
    product_list = [{'name': i, 'price': random.randint(10, 450), 'rating': random.randint(1, 5)}
                    for i in product_list_name]


    # store = Store(product_list)     #{'name': "q1", 'password': "1234567gfd"}, {'name': "q2", 'password': "1234567gfd"}  логины
    # store.add_product()
    # store.add_product()
    # store.add_product()
    # store.cart_view()

    user_1 = User('q1', '1234567gfd')
    user_2 = User('q2', '1234567gfd')
    # user_3 = User('q3', '213454ygfd')
    print(user_1)
    print(user_2)
    print(user_2.password)
    print(product_list)

    cart_test = Cart()
    print(cart_test)
    cart_test.add_cart(10)
    cart_test.add_cart(5)
    print(cart_test.cart)
    cart_test.remove_cart(10)
    print(cart_test)


