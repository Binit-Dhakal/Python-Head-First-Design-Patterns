class SingletonClassOne:
    _instance = None

    def __init__(self):
        raise RuntimeError("Call get_instance() instead")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            print("Creating new instance for First")
            cls._instance = cls.__new__(cls)
        return cls._instance


class SingletonClassTwo:
    _instance = None

    def __new__(cls):  # new is the static method
        if cls._instance is None:
            print("Creating new instance for Second")
            cls._instance = super(SingletonClassTwo, cls).__new__(cls)
        return cls._instance


# using MetaClass to acheive Singleton
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonThree(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value


def run():
    s1 = SingletonClassOne.get_instance()
    s2 = SingletonClassOne.get_instance()

    # will raise error if they are not same instance
    assert id(s1) == id(s2)

    # see the difference in how they are intialized
    t1 = SingletonClassTwo()
    t2 = SingletonClassTwo()

    # will raise error if t1 and t2 are not same instance
    assert id(t1) == id(t2)

    # Using metaclass approach.
    th1 = SingletonThree(12)
    th2 = SingletonThree(15)

    assert id(th1) == id(th2)


if __name__ == "__main__":
    run()
