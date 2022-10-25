from advert import Advert


def test_example1():
    iphone_ad_dict = {
        "title": "iPhone X",
        "price": 100,
        "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }
    iphone_advert = Advert(iphone_ad_dict)
    assert iphone_advert.title == "iPhone X"
    assert iphone_advert.price == 100
    assert iphone_advert.location.address == "город Самара, улица Мориса Тореза, 50"
    assert iphone_advert.location.metro_stations == ["Спортивная", "Гагаринская"]
    print(iphone_advert)


def test_example2():
    corgi_ad_dict = {
        "title": "Вельш-корги",
        "price": 1000,
        "class_": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }
    corgi_advert = Advert(corgi_ad_dict)
    assert corgi_advert.title == "Вельш-корги"
    assert corgi_advert.price == 1000
    assert corgi_advert.class_ == "dogs"
    assert corgi_advert.location.address == "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
    print(corgi_advert)


def run_tests():
    test_example1()
    test_example2()


if __name__ == "__main__":
    run_tests()
