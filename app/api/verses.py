from fastapi import APIRouter
from app.models.bible_model import BibleRequest
from app.agents.bible_agent import suggest_bible_verses

router = APIRouter()

@router.post("/")
async def get_bible_verses(request: list[BibleRequest]):
    """Receives Bible request and fetches relevant verses."""
    verses = suggest_bible_verses(request)
    return verses