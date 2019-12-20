from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context():
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def do_some_business_logic(self):
        print("Sort the data:")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data: List):
        pass

class StrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class StrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))
