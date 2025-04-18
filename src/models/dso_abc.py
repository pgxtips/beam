from abc import ABC, abstractmethod
from io import TextIOWrapper 
from typing import Optional

class DSO(ABC):
    def __init__(self, src):
        self.src = src
        self.attributes = []
        self.ENTRY_LIMIT = 50000

    @abstractmethod
    def connect(self) -> Optional[TextIOWrapper]:
        pass

    @abstractmethod
    def get_attributes(self) -> Optional[list[str]]:
        pass
