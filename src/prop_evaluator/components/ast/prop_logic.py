from abc import ABC, abstractmethod

class PropExpression(ABC):
    @abstractmethod
    def run(self) -> bool:
        pass

    @abstractmethod
    def prefix(self) -> str:
        pass



    