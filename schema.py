from datetime import datetime
from dataclasses import dataclass, field

@dataclass
class Quote: 
    quote: str
    author: str
    created_at: datetime = field(default_factory=datetime.now)

    def display(self): 
        return f"{self.quote} - {self.author}"