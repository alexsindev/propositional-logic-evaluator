from abc import ABC, abstractmethod

class PropExpression(ABC):
    @abstractmethod
    def run(self) -> bool:
        pass

    @abstractmethod
    def prefix(self) -> str:
        pass

# leaf nodes
class PropTrue(PropExpression):
    def run(self) -> bool:
        return True

    def prefix(self) -> str:
        return "t"

class PropFalse(PropExpression):
    def run(self) -> bool:
        return False

    def prefix(self) -> str:
        return "f"



    