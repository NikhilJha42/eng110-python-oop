# eng110-python-oop

## This is a repository created for learning OOP in Python.

Some code is duplicated from my Python repository, and the concept of classes discussed here are used for the unit testing 
section in that repository.

Consult the Python documentation for further resources and information.

## What is OOP?
__Object Oriented Programming__ is the concept of storing data and functionality within objects as opposed to __Functional Programming__, where data and functionality are separate. It is important to 
note that that one is not inherently better - OOP requires a larger investment of time in setting up. However, OOP is usually better for more complex 
applications as it makes for cleaner code that's easier to refactor and is more easily scalable, 
saving time (and therefore cost) in the long term. 

Before reading further, it is first important to note that OOP in Python is achieved using classes.

## Classes in Python
```python
class Rectangle():

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2*self.width + 2*self.height
```

It is conventional in Python to define the class with a Capitalised name.

The `__init__` defines attributes (the data) for the class - in this case, 
when an instance of the `Rectangle` class is created, the user will need to input a width and height. The `get_area` and `get_perimeter` 
methods can then be called to find the area and perimeter of the rectangle.

## Four pillars of OOP.
- __Abstraction__: Reducing complexity through shared understanding.
  
This is about hiding unneccessary details about the functionality of the class - a class may have multiple methods 
which should not be explicitly called, but are used as part of a method that is. As an analogy, think about making a phone call - you dial 
a number and press the call button. Underneath the surface, multiple processes are being run to connect you to the number so that you can speak, 
but you don't see these as it isn't neccessary to understand them in order for you to make the call.
- __Encapsulation__: Reducing complexity through a high degree of usability.

The concept of storing all relevant information within an object so it can be used with easy-to-understand methods.
- __Inheritance__: Creating superclasses and using them to initialise subclasses.

We can use classes to initialise specialised subclasses (and often we refer to the more general class as a superlass).
Here is an example in Python:
```python
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
```
In the `Square` subclass, we take in a `length` parameter and pass it to both `width` and `height` in the `Rectangle` superclass.

Note that we might define new methods in a subclass, and that we may specialise even further (e.g., starting with a `Veichle` superclass, 
defining `Car` and `Lorry` subclasses, and then specifying subclasses of these with make and model details.)
- __Polymorphism__: Define same/similar methods to be used across different classes.

The best way to understand this is to use the above examples; in the `Rectangle` and `Square` classes - the `get_area` and `get_perimeter` methods 
can be used in both. In the `Veichle` example, there are methods common to both cars and lorries that can be defined and then used in both.