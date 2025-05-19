from pydantic import BaseModel
from typing import Optional, Dict, Any, List

class BookCreateModel(BaseModel):
    title: str
    author: str
