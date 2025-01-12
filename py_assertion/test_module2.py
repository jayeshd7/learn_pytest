class TestModule2:
    def test_case1(self):
        self.name = "john"
        for letter in self.name:
            assert letter.islower()

    def test_case2(self):
        assert type(1.3) == float

    def test_strings(self):
        self.id = "123"
        self.name = "john"
        self.email = "john@gmail.com"
        assert self.id.isnumeric()
        assert self.name.isalpha()
        for letter in self.email:
            if letter == "@" or letter == ".":
                assert letter.isascii()
            else:
                assert letter.isprintable()
