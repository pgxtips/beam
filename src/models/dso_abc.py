from abc import ABC, abstractmethod
from io import TextIOWrapper 
from typing import Optional

class DSO(ABC):
    def __init__(self, src):
        self.src = src
        self.data: Optional[list] = None
        self.keys = []
        self.tag_column: Optional[str] = None
        self.content_id_column: Optional[str] = None
        self.tags = []
        self.ENTRY_LIMIT = 50000

    @abstractmethod
    def connect(self) -> Optional[TextIOWrapper]:
        pass
    
    @abstractmethod
    def load_data(self) -> Optional[TextIOWrapper]:
        pass

    @abstractmethod
    def load_tags(self) -> Optional[TextIOWrapper]:
        pass

    def set_tag_column(self, col_name: str):
        self.tag_column = col_name

    def set_content_id_column(self, col_name: str):
        self.content_id_column = col_name

    @abstractmethod
    def get_keys(self) -> Optional[list[str]]:
        pass

    @abstractmethod
    def get_data(self): 
        pass

    @abstractmethod
    def get_tags(self) -> Optional[list[str]]:
        pass

    @abstractmethod
    def get_col_data(self, col_name: str) -> Optional[list]:
        pass
