class Advert:
    def __init__(self, mapping):
        # check if 'title' in keys
        title_flag = False

        for key in mapping:
            if not isinstance(key, str):
                raise TypeError("keys have to be strings")
            if key == 'title':
                title_flag = True
            if key == 'price' and mapping[key] < 0:
                raise ValueError("price have to be >= 0")

            # if mapping[key] is dict we will create another class,
            # that stores values of this
            if isinstance(mapping[key], dict):
                # create a class, which stores inner dict
                class_storer = type(key, (), mapping[key])
                self.__dict__[key] = class_storer
            else:
                self.__dict__[key] = mapping[key]

        if not title_flag:
            raise RuntimeError("no 'title' key in mapping")

    @property
    def price(self):
        if 'price' not in self.__dict__:
            return 0

    def __repr__(self):
        return f"{self.title} | {self.price} ₽"


ad = Advert({"title": 'example', 'price': 100, 'location': {'address': 'Alise in the mirror 12', 'house': 26}})
print(ad.location.house)
print(ad)
