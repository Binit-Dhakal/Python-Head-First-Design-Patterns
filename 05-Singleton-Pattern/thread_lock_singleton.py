from threading import Thread, Lock


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            """
            The First Thread to acquire this lock, reaches the conditional,
            goes inside and creates a Singleton instance. Once it leaves The
            lock block, a thread that might have been waiting for the lock
            realease may enter the section. But wont create a new object.
            """
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == "__main__":
    process1 = Thread(target=test_singleton, args=("Foo"))
    process2 = Thread(target=test_singleton, args=("Boo"))
    process1.start()
    process2.start()
