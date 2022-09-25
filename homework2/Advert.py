try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping


class ColorizerMixin:
    repr_color_code = 33

    def __repr__(self):
        return f"\033[1;{self.repr_color_code};40m{self.title} | {self.price} ₽"


class Advert(ColorizerMixin):
    def __init__(self, mapping):
        # check if 'title' in keys
        title_flag = False

        for key in mapping:
            if not isinstance(key, str):
                raise TypeError("keys have to be strings")
            if key == 'title':
                title_flag = True
            if key == 'price':
                price_value = mapping[key]
                if not isinstance(price_value, (int, float)):
                    raise ValueError("price have to be int or float")
                if price_value < 0:
                    raise ValueError("price have to be >= 0")
                price_key = '_price'
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

        if not title_flag:
            raise RuntimeError("no 'title' key in mapping")

    @property
    def price(self):
        if '_price' not in self.__dict__:
            return 0
        else:
            return self._price


ad = Advert({"title": 'example', 'price': 100, 'location': {'address': 'Alise in the mirror 12', 'house': 26}})
print(ad.location.address)
print(ad)
