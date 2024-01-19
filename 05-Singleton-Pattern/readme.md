# Singleton Pattern

Singleton Pattern is a software design pattern that restricts the instantiation of a class to singular instance. What this means in layman term is callingclass initializer multiple time in singleton pattern will return same class instance.

The main feature of Singleton pattern is:

- Ensure they have only one instance
- Provide early access to that instance
- Control their instantiation

## Singleton Pattern in Other Languages

In other languages we acheive Singleton pattern by declaring constructor as private and declaring a classmethod "getInstance()" that will instantiate theclass(if not already instantiated). This will ensure that we will have only one instance and also allow lazy instantiation. We might run into thread problem in other language so appropriate measure as per language should be taken for dealing with that so we dont end up with two instance of same class.

## Singleton Pattern in Python

In python, We can create singleton pattern in two ways:

- Raise RuntimeError when calling **init** in class and making a classmethod "instance" that will create new instance if not already created or else return same instance of class. For creating the instance of class inside "instance" method, we will use **new** magic method.
- More pythonic Implementation will be to override **new** method in class and instantiate the object using `cls._instance = super(MyClass, cls).__new__(cls)`. This will let us not raise exception in **init** when called and we can instantiate our class using `my_class = MyClass()`.
- Using MetaClass in python. Metaclass are classes that create other classes. We can use **call** method in metaclass, that is called when we attempt to create an instance of the class(e.g. MyClass()). This controls object creation at class level. (Different from instance **call**() which is customizes behavior when instance is 'called' as a function)

## Thread-Safe Singleton

Python's GIL only allows one thread to execute python bytecode at a time. However it doesn't prevent multiple thread from running concurrently within theinterpreter. This means multiple thread can still try to access and modify shared object, including singleton instance.
So we need to ensure thread safety:

- Using Locks(eg: Threading.Lock)
- Metaclass with thread-safe **call** methods
- Double checking locking pattern

## Better Approach in Python(as per docs)

If the design forces you to offer global access to singleton object then we should use "The Global Object Pattern".
Modules are "singletons" in Python as 'import' only creates a single copy of each module; subsequent imports of same name keep returning the same module object. So we can use this feature for singleton pattern. We can define a class and instantiate it in the module and then import it. This way, the imported module will have the same object across all imported modules.

But I personally see some caveats in this method that doesn't align with defination of Singleton:

- Singleton explicitly enfore single instantiation but Global objects can be overriden as there is nothing that is stopping it from doing so.
- Singleton often are lazy intialized(delaying instance creation until its first needed), potentially improving performance but Global objects are eagerly initialized when the module is imported.

### Cons of Singleton pattern

- Violates Single Responsibility Principle. The patterns solves two problem at a time(making singleton possible and handling its usual responsibility). But I think this is kind of removed when using the Metaclass in python as metaclass will handle making class singleton part and the class can handle its usual responsibility.
- The patterns need special treatment in multithreaded environment.

##### Sources:

- https://python-patterns.guide/gang-of-four/singleton/
- https://python-patterns.guide/python/module-globals/
- https://en.wikipedia.org/wiki/Singleton_pattern
- Head First Design Pattern book
- https://refactoring.guru/design-patterns/singleton/python/example
