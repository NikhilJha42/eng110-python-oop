# Use multiple classes to define new instances, i.e., don't use the class
# Dog to create a dolphin.

# class Dog:
#
#     def __init__(self, name, colour):
#         self.animal_kind = "canine"
#         self.name = name
#         self.colour = colour
#         self.bark()
#
#     def bark(self):
#         return "woof"
#
# fido = Dog("Lucky", "Brown")

# Use underscore or double underscore to signal that an attribute should not be changed.
# class MethodExamples:
#
#     def __init__(self):
#         self._this_can_be_accessed_easily = "Hi, I'm easily found"
#
#     def get_this_can_be_accessed_easily(self):
#         return self._this_can_be_accessed_easily
#
#     def set_this_can_be_accessed_easily(self, value_to_be_set):
#         self._this_can_be_accessed_easily = value_to_be_set
#
# x = MethodExamples()
#
# print(x.get_this_can_be_accessed_easily())
# x.set_this_can_be_accessed_easily("I have changed")
# print(x.get_this_can_be_accessed_easily())

class Dog:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"A {self.age} year old dog."

    def __format__(self, format_spec):
        if format_spec == "dog":
            return f"A {self.age + 7} dog years old Dog"
        else:
            return self.__str__()

fido = Dog(5)
print((f"{fido}"))
print(f"{fido:dog}")