# Inheritance

## Definition/ Overview
 In most class-based object-oriented languages, an object created through inheritance, a "child object", acquires all the properties and behaviors of the "parent object" (with the exception of: constructors, destructor, overloaded operators and friend functions of the base class). 

 Inheritance can be used when you observe a 'kind-of' or 'is-a' relationship between classes. You can say, for example, that "a dog is an animal" or "a dog is a kind of animal".
 
 Inheritance allows programmers to create classes that are built upon existing classes, to specify a new implementation while maintaining the same behaviors (realizing an interface), to reuse code and to independently extend original software via public classes and interfaces.

Sources:

 - _[Wikipedia, 'Inheritance'](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming))_

 - _[Isaac Computer Science, Inheritance and Polymorphism](https://isaaccomputerscience.org/concepts/prog_oop_inheritance_polymorphism?examBoard=all&stage=all)_

# Polymorphism

## Definition/ Overview
Polymorphism refers to the ability of a method to exhibit different behaviours depending on the object on which the method is invoked.

> "Do X for a collection of various types of objects, where X is different depending on the type of object"

A novice OOP programmer will most likely encounter polymorphism when a method, inherited from a parent (super-) class, has its implementation changed to better suit the child (sub-) class. This process is called *overriding*.

The significance of polymorphism is that the object itself knows which implementation of a method to use.


Sources:

 - _[AP Computer Science, UTexas](https://www.cs.utexas.edu/~scottm/ap/pasadena/APinheritanceInterfacesPoly.pdf)_

 - _[Isaac Computer Science, Inheritance and Polymorphism](https://isaaccomputerscience.org/concepts/prog_oop_inheritance_polymorphism?examBoard=all&stage=all)_


# Abstraction

## Definition/ Overview

Abstraction is a process of handling complexity by hiding unnecessary information from the user. This enables the user to implement even more complex logic on top of the provided abstraction without understanding or even thinking about the hidden background/back-end complexity.

An abstract method is a method that is declared, but does not contain implementation. An abstract method in a base class identifies the functionality that should be implemented by all its subclasses. However, since the implementation of an abstract method would differ from one subclass to another, often the method body comprises just a pass statement. Every subclass of the base class will ride this method with its implementation. A class containing abstract methods is called abstract class.

Sources:

 - _[GreatLearning, 'Abstraction in Python'](https://www.mygreatlearning.com/blog/abstraction-in-python/)_


# Encapsulation

## Definition/ Overview