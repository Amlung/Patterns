from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass

class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 19:
            print("Found the node 19")

class TreeNode:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data, " ",end = ''),
        if self.right:
            self.right.PrintTree()

class SubjectTree(Subject):
    _state: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self,x) -> None:
        self._state = x
        print("Node:", x)
        self.notify()

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.nodes_sorted = []
        self.index = -1
        self._inorder(root)
        self._state: int = None
        self._observers: List[Observer] = []

    def print_t(self):
        print(self.nodes_sorted,)
    
    def _inorder(self, root):
        if not root:
            return
        self.nodes_sorted.append(root.data)
        self._inorder(root.left)    
        self._inorder(root.right)

    def next(self) -> int:
        self.index += 1
        return self.nodes_sorted[self.index]

    def hasNext(self) -> bool:  
        return self.index + 1 < len(self.nodes_sorted)   

if __name__ == "__main__":
    root = TreeNode(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)

    root.PrintTree()
    print()
    new_iterator = BSTIterator(root)
    new_iterator.print_t()
    
    subject = SubjectTree()
    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    while (new_iterator.hasNext()):
        subject.some_business_logic(new_iterator.next())

