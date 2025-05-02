from fastapi import APIRouter
from app.agents.bible_agent import BibleAgent

router = APIRouter()

@router.post("/query")
async def get_verses_for_query(content: str):
    """Receives a topic and returns the suggested verses."""
    response = BibleAgent().human_message(content)
    return response