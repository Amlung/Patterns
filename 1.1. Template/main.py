from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def template_method(self):
        self.ac_op1()
        self.ac_op2()
        self.ac_op3()
        self.ro1()
        self.ro2()

    def ac_op1(self):
        print("ac_op1")

    def ac_op2(self):
        print("ac_op2")

    def ac_op3(self):
        print("ac_op3")

    @abstractmethod
    def ro1(self):
        pass

    @abstractmethod
    def ro2(self):
        pass


class Class1(AbstractClass):
    def ro1(self):
        print("c1_ro1")

    def ro2(self):
        print("c1_ro2")


class Class2(AbstractClass):
    def ro1(self):
        print("c2_ro1")

    def ro2(self):
        print("c2_ro2")



def client_code(abstract_class: AbstractClass):
    abstract_class.template_method()


if __name__ == "__main__":
    print("Class1:")
    client_code(Class1())
    print("")

    print("Class2:")
    client_code(Class2())