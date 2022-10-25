try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping


class ColorizerMixin:
    repr_color_code = 33

    def __str__(self):
        repr_msg = self.__repr__()
        return f"\033[1;{self.repr_color_code};40m{repr_msg}"


class Advert(ColorizerMixin):
    def __init__(self, mapping: Mapping):
        # check if 'title' in keys
        if "title" not in mapping:
            raise RuntimeError("no 'title' key in mapping")

        for key in mapping:
            if not isinstance(key, str):
                raise TypeError("keys have to be strings")
            if key == "price":
                price_value = mapping[key]
                self._price_value_check(price_value)
                price_key = "_price"
                self.__dict__[price_key] = price_value
                continue

            # if mapping[key] is dict we will create another class,
            # that stores values of this
            if isinstance(mapping[key], Mapping):
                # create a class, which stores inner dict
                class_storer = type(key, (), mapping[key])
                self.__dict__[key] = class_storer
            else:
                self.__dict__[key] = mapping[key]

    def _price_value_check(self, price_value):
        if not isinstance(price_value, (int, float)):
            raise ValueError("price have to be int or float")
        if price_value < 0:
            raise ValueError("price have to be >= 0")

    @property
    def price(self):
        if "_price" not in self.__dict__:
            return 0
        else:
            return self._price

    @price.setter
    def price(self, price_value: float):
        self._price_value_check(price_value)
        self._price = price_value

    def __repr__(self):
        return f"{self.title} | {self.price} ₽"
