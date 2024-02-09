b = {'name': "q1", 'password': "1234567gfd"}
class IdCounter:
    id_ = 0
    def __init__(self, id_):
        self.id_ =id_
        self.count()


    def count():
        count += 1
        pass


class Password:
    def __init__(self, password):
        self.password = None

    def check(self, password):
        if not isinstance(self.password, str):
            raise TypeError()
        if len(self.password) < 8 and not self.password.isalnum():
            raise TypeError()

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.check(password)
        self.__password = password


class Product(IdCounter):
    def __init__(self, name, price, rating):
        # super().__init__(id_)
        # self.id_ = id_
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


class Cart(Product):
    product_list = ["банан", "мандарин", "яблоко", "свекла", "помидор", "огурец", "капуста"]
    def __init__(self):
        super().__init__(self._name)
        self.cart = []
    def add_cart(self):
        self.cart.append(self._name)
    def remove_cart(self):
        self.cart.remove(self._name)


class User(Password):
    def __init__(self, username, password):
        super().__init__(password)
        # self.id_ = id_
        self.username = None
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username


    def __repr__(self):
        return f"{self.__class__.__name__}({self.username},password1)"

    def __str__(self):
        return f"{self.username},password1"


class Store(User, Cart):
    def __init__(self, username, password, cart):
        super(User).__init__(username, password)
        super(Cart).__init__(cart)

    def add_cart(self):
        self.cart.append(self.name)
        return self.cart

    def remove_cart(self):
        self.cart.remove(self.name)
        return self.cart

if __name__ == '__main__':
    c = input("Введите логин:")
    d = input("Введите пароль:")
    a = User(c, d)
    a.password.check()
    if a.password == b['password'] and a.username == b['name']:
        print(self.cart)
    else:
        raise ValueError("Неверный логин или пароль")



