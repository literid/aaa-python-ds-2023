class Advert:
    def __init__(self, mapping):
        # check if 'title' in keys
        title_flag = False

        for key in mapping:
            if not isinstance(key, str):
                raise TypeError("keys have to be strings")

            if key == 'title':
                title_flag = True

            self.__dict__[key] = mapping[key]

        if not title_flag:
            raise RuntimeError("no 'title' key in mapping")


ad = Advert({"title": 'example', 'price': 100})
print(ad.price)
