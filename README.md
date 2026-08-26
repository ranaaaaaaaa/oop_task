# OOP Task

This project covers abstract classes, duck typing, and inheritance in Python.

**Abstract classes** use `ABC` + `@abstractmethod` to force subclasses to implement
certain methods otherwise instantiation raises a `TypeError` instead of silently
allowing a broken object. A class can be partially abstract (some methods abstract,
some concrete) or fully abstract (all methods abstract, Python's equivalent of an
interface, since it has no dedicated `interface` keyword).

**Duck typing** means Python checks an object's behavior (does it have the method
being called?) rather than its declared type as in no shared parent or inheritance
required, unlike polymorphism/overriding. This avoids the rigidity of `isinstance`
type-checks.

A `Garage` class manages cars with private attributes (`__capacity`, `__spots`) for
encapsulation, supporting `add_car()`, `park_car()`, `remove_car()`, and
`display_available_spots()`.

An `ElectricCar(Car, Battery)` class demonstrates multiple inheritance, calling
`Car.__init__(self, ...)` and `Battery.__init__(self, ...)` directly instead of
`super()`, since `super()` always resolves to the same class in the MRO regardless
of how many times it's called.
