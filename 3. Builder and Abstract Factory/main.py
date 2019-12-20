from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any

class Builder(ABC):
  
    @abstractproperty
    def product(self):
        pass

    @abstractmethod
    def produce_part_a(self):
        pass

    @abstractmethod
    def produce_part_b(self):
        pass

    @abstractmethod
    def produce_part_c(self):
        pass


class Builder1(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._product = ProductA1()

    @property
    def product(self) -> ProductA1:
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")

class Director:
   
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

class AbstractFactory(ABC):
   
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class Factory1(AbstractFactory):
    
    def create_product_a(self) -> ProductA1:
        return ProductA1()

    def create_product_b(self) -> ProductB1:
        return ProductB1()


class Factory2(AbstractFactory):
    
    def create_product_a(self) -> ProductA2:
        return ProductA2()

    def create_product_b(self) -> ProductB2:
        return ProductB2()


class AbstractProductA(ABC):

    def __init__(self):
        self.parts = []

    def add(self, part: Any):
        self.parts.append(part)

    def list_parts(self):
        print(f"Product parts: {', '.join(self.parts)}", end="")

    @abstractmethod
    def useful_function_a(self):
        pass

class ProductA1(AbstractProductA):
    def useful_function_a(self):
        print("The result of the product A1.")


class ProductA2(AbstractProductA):
    def useful_function_a(self):
        print("The result of the product A2.")

class AbstractProductB(ABC):
    
    def __init__(self):
        self.parts = []

    def add(self, part: Any):
        self.parts.append(part)

    def list_parts(self):
        print(f"Product parts: {', '.join(self.parts)}", end="")

    @abstractmethod
    def useful_function_b(self):
        pass

class ProductB1(AbstractProductB):
    def useful_function_b(self):
        print("The result of the product B1.")

class ProductB2(AbstractProductB):
    def useful_function_b(self):
        print("The result of the product B2.")

def create_product(factory: AbstractFactory) -> None:
    
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_a.useful_function_a()}")
    print(f"{product_b.useful_function_b()}")

    #print(f"{product_b.useful_function_b()}")
    #print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
   
    print("Client: Testing client code with the first factory type:")
    create_product(Factory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    create_product(Factory2())

    print("\n")

    director = Director()
    builder = Builder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_product()
    builder.product.list_parts()
    print("\n")
    print("Standard full featured product: ")
    director.build_full_product()
    builder.product.list_parts()

    print("\n")

    print("Custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()