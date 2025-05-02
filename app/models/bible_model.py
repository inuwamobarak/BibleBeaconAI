from pydantic import BaseModel
from typing import List

class BibleRequest(BaseModel):
    translation: str
    book: int
    chapter: int
    verses: List[int]