import pytest
from app.agents.bible_agent import process_bible_query

def test_process_bible_query():
    topic = "Jesus is the son of God"
    verses = process_bible_query(topic)
    
    assert len(verses) > 0  # Check if verses are returned
    assert "YLT" in verses[0]["translation"]  # Example check for translation