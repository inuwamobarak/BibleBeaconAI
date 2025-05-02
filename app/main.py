from fastapi import FastAPI
from app.api import verses, agent

app = FastAPI()

# Include the routes from the api folder
app.include_router(verses.router, prefix="/get-verses", tags=["Verses"])
app.include_router(agent.router, prefix="/agent", tags=["Agent"])