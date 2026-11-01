from abc import ABC, abstractmethod

class CanBeShipped(ABC):
    # Methods
    @abstractmethod
    def calculate_shipping_cost(self):
        pass