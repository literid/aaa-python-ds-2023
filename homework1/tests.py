from CountVectorizer import CountVectorizer


def test_empty_init():
    vectorizer = CountVectorizer()
    assert vectorizer.vocabulary == {}
    assert vectorizer.get_feature_names() == []


def test_empty_corpus():
    corpus = []
    vectorizer = CountVectorizer()
    term_matrix = vectorizer.fit_transform(corpus)
    assert term_matrix == []
    assert vectorizer.vocabulary == {}
    assert vectorizer.get_feature_names() == []


def test_token_sep():
    token_sep = ","
    corpus = [
        token_sep.join(["one", "two", "three", "two", "one"])
    ]
    vectorizer = CountVectorizer(token_sep=token_sep)
    term_matrix = vectorizer.fit_transform(corpus)
    assert term_matrix == [[2, 2, 1]]
    assert vectorizer.vocabulary == {"one": 0,
                                     "two": 1,
                                     "three": 2
                                     }
    assert vectorizer.get_feature_names() == ["one", "two", "three"]


def test_example1():
    corpus = [
        "one two three two one"
    ]
    vectorizer = CountVectorizer()
    term_matrix = vectorizer.fit_transform(corpus)
    assert term_matrix == [[2, 2, 1]]
    assert vectorizer.vocabulary == {"one": 0,
                                     "two": 1,
                                     "three": 2
                                     }
    assert vectorizer.get_feature_names() == ["one", "two", "three"]


def test_example2():
    corpus = [
        "one two three two one",
        "four"
    ]
    vectorizer = CountVectorizer()
    term_matrix = vectorizer.fit_transform(corpus)
    assert term_matrix == [[2, 2, 1, 0],
                           [0, 0, 0, 1]]
    assert vectorizer.vocabulary == {"one": 0,
                                     "two": 1,
                                     "three": 2,
                                     "four": 3
                                     }
    assert vectorizer.get_feature_names() == ["one", "two", "three", "four"]


def test_example3():
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste"
    ]
    vectorizer = CountVectorizer()
    term_matrix = vectorizer.fit_transform(corpus)
    assert term_matrix == [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                           [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    assert vectorizer.get_feature_names() == ["crock", "pot", "pasta", "never", "boil", "again", "pomodoro", "fresh",
                                              "ingredients", "parmesan", "to", "taste"]


def run_tests():
    test_empty_init()
    test_empty_corpus()
    test_token_sep()
    test_example1()
    test_example2()
    test_example3()


if __name__ == "__main__":
    run_tests()
