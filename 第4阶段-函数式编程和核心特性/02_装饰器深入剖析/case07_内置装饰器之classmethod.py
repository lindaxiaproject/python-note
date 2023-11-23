class Person:
    @classmethod
    def say_hello(cls):
        print(f"我是{cls.__name__}")
        print("hello world!")


if __name__ == '__main__':
    Person.say_hello()
