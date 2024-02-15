from dataclasses import dataclass
from dataclasses import field

from datetime import datetime

@dataclass
class Score:
    name: str
    value: int
    updatedAt: datetime = field(default_factory = datetime.now)
