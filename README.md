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
class Headphones:
    
    def __init__(self, style:str, colour:str):
        self.style = style
        self.colour = colour
        self.on = False

    def switch(self):
        self.on = not(self.on) # Switches headphone on/off
```

It is conventional in Python to define the class with a Capitalised name.

The `__init__` defines attributes (the data) for the class - in this case, 
when an instance of the class is created, the user will need to input a 
style and a colour as strings, and the headphones start as being switched off.

In the above class, `switch` is a method that can be called on the class; for example:

```python
item_1 = Headphones("Over-ear", "green")
item_1.switch() # switches headphones on
item_1.switch() # switches headphones off
```
## Four pillars of OOP.
- __Abstraction__: Reducing complexity through shared understanding.
  
This is about hiding unneccessary details about the functionality of the class - a class may have multiple methods 
which should not be explicitly called, but are used as part of a method that is. As an analogy, think about making a phone call - you dial 
a number and press call. Underneath the surface, multiple processes are being run to connect you to the number so that you can speak, 
but you don't see these as it isn't neccessary to understand them in order for you to make the call.
- __Encapsulation__: Reducing complexity through a high degree of usability.
- __Inheritance__: Creating superclasses and using them to initialise subclasses.
- __Polymorphism__: Define same/similar methods to be used across different classes.